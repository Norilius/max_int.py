size= int(input("How large is the square?: "))

# foreach row and column
for row in range(size):
    for column in range(size):
        print("*",end=" ")