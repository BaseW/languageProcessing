def cipher(sentence):
  result = ""
  for letter in sentence:
    if letter.islower():
      letter = chr(219 - ord(letter))
    result += letter
  return result


print(cipher("I am Yugo"))
print(cipher(cipher("I am Yugo")))