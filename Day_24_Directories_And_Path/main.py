# file = open("text.txt")
# contents = file.read()
# print(contents)
# file.close()
#
# with open("text.txt") as file:
#     contents2 = file.read()
#     print(contents2)

# Rewrite file
with open("text.txt", mode="w") as file:
    file.write("Hello World")

# Add to the file
with open('text.txt', mode='a') as file:
    file.write('\n I am an iOS Developer!')


