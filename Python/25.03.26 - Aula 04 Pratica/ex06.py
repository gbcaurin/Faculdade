i = 1
c = 3
while i < 20:
  sc = i + (i + 1)
  sb = c + (c + 2)
  i += 1
  c += 2
s = sc / sb
print(f"{s:.2f}")