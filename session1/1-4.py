sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.replace(".", "").split(" ")
print(words)

array = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dictionary = {}
for i in range(1, len(words) + 1):
  if i in array:
    dictionary[words[i-1][0]] = i
  else:
    dictionary[words[i-1][0:2]] = i

print(dictionary)
