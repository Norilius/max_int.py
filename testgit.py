size= int(input("How large is the square?: "))

# foreach row and column
for row in range(size):
    for column in range(size):
        if row == 0 or row == size - 1:
        
            print("*", end=" ")
        
        elif column == 0 or column == size:
            prin("*", end=" ")
    print()