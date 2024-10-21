def penyelesaian(n, a, b, c):
  hasil = []
  for x in range(1, n+1):
    if x % a == 0 and x % b == 0 and x % c == 0:
      hasil.append("Siap Bang Jago")
    elif x % a == 0 and x % b == 0:
      hasil.append("Siap Bang")
    elif x % a == 0 and x % c == 0:
      hasil.append("Siap Jago")
    elif x % b == 0 and x % c == 0:
      hasil.append("Bang Jago")
    elif x % a == 0:
      hasil.append("Siap")
    elif x % b == 0:
      hasil.append("Bang")
    elif x % c == 0:
      hasil.append("Jago")
    else:
      hasil.append(x)
  return hasil

# Test Case 1
n = 12
a = 2
b = 3
c = 4

hasil = penyelesaian(n, a, b, c)

print(hasil)
def penyelesaian(n, a, b, c):
  hasil = []
  for x in range(1, n+1):
    if x % a == 0 and x % b == 0 and x % c == 0:
      hasil.append("Siap Bang Jago")
    elif x % a == 0 and x % b == 0:
      hasil.append("Siap Bang")
    elif x % a == 0 and x % c == 0:
      hasil.append("Siap Jago")
    elif x % b == 0 and x % c == 0:
      hasil.append("Bang Jago")
    elif x % a == 0:
      hasil.append("Siap")
    elif x % b == 0:
      hasil.append("Bang")
    elif x % c == 0:
      hasil.append("Jago")
    else:
      hasil.append(x)
  return hasil

# Test Case 2
n = 5
a = 1
b = 1
c = 1

hasil = penyelesaian(n, a, b, c)

print(hasil)