sentence = "I am an NLPer"
words = sentence.split(" ")
letters = sentence.replace(" ", "")

print(words)
print(letters)

def makeBiGram(sequence):
  bi_gram = []
  length = len(sequence)
  for i in range(length-1):
    bi_gram.append(sequence[i] + sequence[i + 1])
  return bi_gram


print(makeBiGram(words))
print(makeBiGram(letters))
