with open('popular-names.txt', 'r') as f:
  for row in f:
    row = row.replace('\t', ' ')
    print(row)