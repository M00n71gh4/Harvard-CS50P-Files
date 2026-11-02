def convert(txtInput):
    strText = str(txtInput)
    strText = strText.replace(":(", "🙁")
    strText = strText.replace(":)", "🙂")
    print(strText)

def main():
    convert(input("Say something with a face: "))

main()

