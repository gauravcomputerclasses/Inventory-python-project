try:
    with open("Hello.txt") as f:
        f.read()
except FileNotFoundError:
    print("The file yor are looking for doesn't exists")