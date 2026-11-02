strGreeting = input("Greeting: ")

strGreeting = strGreeting.strip()
strGreeting = strGreeting[:5]
strGreeting = strGreeting.capitalize()



if strGreeting == "Hello":
    print("$0")
elif strGreeting[0] == "H":
    print("$20")
else:
    print("$100")

