try:
    with open("file.txt") as f:
        print(f)
except FileNotFoundError:
    print("File not found")