def find_primes():
  list_of_primes = [2,3]
  print(1)
  print(2)
  print(3)
  current = 4
  while (True):
    prime = True
    for x in list_of_primes:
      if ((current % x) == 0):
        prime = False
    if (prime):
      list_of_primes.append(current)
      print(current)
    current += 1

find_primes()