string = "stressed"
length = len(string)
_string = [string[length - i] for i in range(1, length + 1)]
print("".join(_string))
answer = ""
for i in range(length):
  answer += _string[i]

print(answer)