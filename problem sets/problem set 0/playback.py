def convert(emoticons):
    emoticons = emoticons.replace(":)", "🙂")  
    emoticons = emoticons.replace(":(", "🙁")  
    return emoticons

def main():
    user_text = input("Type something: ")
    result = convert(user_text)
    print(result)

main()