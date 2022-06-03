def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

d = []
e = []

for i in range(1, int(input(""))):
    if not is_prime(i):
        continue

    squared = i * i
    mult24 = (squared - 1) / 24

    d.append(int(mult24 - i))
    e.append(mult24)

    print("{}, {}, {}".format(i, mult24, int(mult24 - i)))

for l in range(1, len(d)):
    print(d[l] - d[l - 1])

for ee in range(1, len(e)):
    print(e[ee] - e[ee - 1])
