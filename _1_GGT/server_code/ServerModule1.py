import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

# Euklid recursive
@anvil.server.callable
def ggt_euklid_recursive(a: int, b: int) -> int:    
  if b == 0: 
    return a
  else: 
    return ggt_euklid_recursive(b, a % b)

# Euklid iterative
@anvil.server.callable
def ggt_euklid(a, b):
  if a == 0:
    return b
  else:
    while b != 0:
      if a > b:
        a = a - b
      else:
        b = b - a
    return a
    
