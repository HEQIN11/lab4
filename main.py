# Author: Heqin Wang hbw5248@psu.edu
# Collaborator:Arabella Harrison axh5810@psu.edu
# Collaborator:Ryan Dang rvd5465@psu.edu
# Collaborator:Abel Ismael agi5031@psu.edu
# Section: 12
# Breakout: 6

def num_of_divisors(n):
 
  s=n
  a=0

  while n>0:
    if s%n==0:
      n=n-1
      a=a+1
    else:
      n=n-1
  return a

def num_of_primes(n):
  s=0
  for i in range(n,0,-1):
    if num_of_divisors(i)==2:
      s=s+1
    


  return s

def sum_n(n):

  s=0
  while n>0:
    s=s+n
    n=n-1 
  return s

def print_n(s, n):
 
  for n in range(n,0,-1):
    if n>0:
      print(f"{s}")
  return

def run():
  num = int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  print(f"{num} has {num_of_divisors(num)} divisors.")
  print(f"There are {num_of_primes(num)} primes <= {num}.")
  line = input("Enter a string: ")
  print_n(line, num)

if __name__ == "__main__":
  run()
