sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence = sentence.replace(",", "").replace(".", "")

words = sentence.split(" ")
print(words)

length_list = []
dictionary = {}
for word in words:
  print("length of {} = {}".format(word, len(word)))
  dictionary[word] = len(word)
  length_list.append(len(word))

print(dictionary)
# TODO 長さの大きい順に辞書から取り出す
print(length_list)