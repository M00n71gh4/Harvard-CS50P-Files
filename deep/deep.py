strInput = input("What is the answer to the Great Question of Life? ")

strInput = strInput.lower()
strInput = strInput.strip()

if strInput == "42":
    print("Yes")
elif strInput == "forty two":
    print("Yes")
elif strInput == "forty-two":
    print("Yes")
else:
    print("No")