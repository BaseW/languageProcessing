def makeBiGram(sequence):
  bi_gram = []
  length = len(sequence)
  for i in range(length-1):
    bi_gram.append(sequence[i] + sequence[i + 1])
  return bi_gram


X = makeBiGram("paraparaparadise")
Y = makeBiGram("paragraph")
print(X)
print(Y)

set_x = set(X)
set_y = set(Y)
print(set_x)
print(set_y)

s_union = set_x | set_y
print(s_union)

s_intersection = set_x & set_y
print(s_intersection)

s_difference = set_x - set_y
print(s_difference)

print("se" in set_x)
print("se" in set_y)
