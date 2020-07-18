count = 0
with open('popular-names.txt', 'r') as f:
  for row in f:
#    print(row)
    count += 1

print(count)
