def diamondGlenn(height):
    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i + " " * spaces)

    for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i + " " * spaces)

tinggiDiamond = int(input("Enter the height of the diamond: "))
diamondGlenn(tinggiDiamond)
