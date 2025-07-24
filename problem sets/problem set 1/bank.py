def main():
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(f"${amount:}")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello") == True:
        return 0
    elif greeting.startswith("h") == True and greeting.startswitch("hello") == False:
        return 20
    else:
        return 100

main()
