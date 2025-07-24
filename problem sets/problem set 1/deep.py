answer = input("What is the answer to the Great Question of life, the universe and Everything? ")
answer = answer.strip().lower()

if answer == "42" or answer == "forty two" or answer == " forty-two":
  print("Yes")
else:
  print("No")