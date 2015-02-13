#!/usr/bin/env python

from argparse import ArgumentParser
from subprocess import call
from repeat import repeat

# Victory functions take a command's output.
# If the function returns true, then we should exit the repeat loop.
# If false, then we don't have vicotry and should repeat the cmd.
def until_success_victory(cmd_exit):
  return int(cmd_exit) == 0

def unless_failure_victory(cmd_exit):
  return not (int(cmd_exit) == 0)

def repeat_victory(cmd_exit):
  return False

parser = ArgumentParser(description='A script to convert from one time format to another',)
success_group = parser.add_mutually_exclusive_group()
success_group.add_argument("--until-success", action='store_const', const=until_success_victory, dest="victory_condition")
success_group.add_argument("--unless-failure", action='store_const', const=unless_failure_victory, dest="victory_condition")
parser.add_argument("--period", default=60, type=int)
parser.add_argument("--max-tries", default=None, type=int)
parser.add_argument("--max-time", default=None, type=int)
parser.add_argument("--separator", default=None)
parser.add_argument("cmdargs", type=str, nargs="+")

def main():
  args = parser.parse_args()
  if args.victory_condition is None:
    args.victory_condition = repeat_victory
  def run_program():
    ret_val = call(args.cmdargs)
    if args.separator is not None:
      print args.separator
    return args.victory_condition(ret_val)
  success = repeat(run_program, period=args.period, max_tries=args.max_tries, max_time=args.max_time)
  if success:
    exit(0)
  else:
    exit(1)