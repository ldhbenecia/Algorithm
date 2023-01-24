a = input()
b = input()

for i in a:
  if i in b:
    a = a.replace(i, "", 1)
    b = b.replace(i, "", 1)
    
print(len(a) + len(b))
