#!/usr/bin/env python

import docopt
from argparse import ArgumentParser
from subprocess import call
from repeat import repeat
from sys import stdout

# Victory functions take a command's output.
# If the function returns true, then we should exit the repeat loop.
# If false, then we don't have vicotry and should repeat the cmd.
def until_success_victory(cmd_exit):
  return int(cmd_exit) == 0

def unless_failure_victory(cmd_exit):
  return not (int(cmd_exit) == 0)

def repeat_victory(cmd_exit):
  return False

def convert_or_none(constructor, i):
  if i is None:
    return None
  else:
    return constructor(i)

USAGE= \
"""
repeat - Runs command repeatedly until some condition is reached.

Usage:
    repeat [options] [--until-failure|--until-success] -- <command> [<args>...]

    Options:

  --period=<sleep>       Time between runs [default: 1].
  --max-tries=<tries>
  --max-time=<time>
  --separator=<pattern>  Printed between runs [default: ].
"""

def main():
  args = docopt.docopt(USAGE)

  if args['--until-failure']:
    victory_condition = unless_failure_victory
  elif args['--until-success']:
    victory_condition = until_success_victory
  else:
    victory_condition = repeat_victory

  sep = args['--separator']
  program = [args['<command>']] + args['<args>']
  period = int(args['--period'])

  max_tries = convert_or_none(int, args['--max-tries'])
  max_time = convert_or_none(int, args['--max-time'])

  def run_program():
    ret_val = call(program)
    stdout.write(sep)
    return victory_condition(ret_val)
  success = repeat(run_program, period=period, max_tries=max_tries, max_time=max_time)
  if success:
    exit(0)
  else:
    exit(1)
