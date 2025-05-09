print("Enter url: ")
url = input()

if url.startswith("https://"):
    print("Secure")
elif url.startswith("http://"):
    print("Not Secure")
else:
    print("Not valid url...")