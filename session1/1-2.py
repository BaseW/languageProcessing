word1 = "パトカー"
word2 = "タクシー"

array = []
for i in range(4):
  array.append(word1[i])
  array.append(word2[i])

print(array)
print("".join(array))
