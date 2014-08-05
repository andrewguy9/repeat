from time import sleep, time

def xxrange(start, stop=None, step=1):
  i = int(start)
  step=int(step)
  while(stop is None or i <= int(stop)):
    yield i
    i=i+step

def repeat(callback, period=0, max_tries=None):
  for i in xxrange(1, max_tries):
    start_time = int(time())
    ret = callback()
    if ret:
      return True
    end_time = int(time())
    sleep_time = max(0.0, period - (end_time - start_time))
    sleep(sleep_time)
  return False

