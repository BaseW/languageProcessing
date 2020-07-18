import random

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
sentence = sentence.replace(".", "")
print(sentence)

words = sentence.split(" ")
print(words)

result = ""
for word in words:
  length = len(word)
  if length > 4:
    # 処理
    central = []
    for i in range(1, length - 1):
      central.append(word[i])
      random.shuffle(central)
    word = word[0] + "".join(central) +  word[length - 1]
  result += word + " "

print(result)
