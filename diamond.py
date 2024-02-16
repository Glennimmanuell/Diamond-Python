def diamondGlenn(height):
    if height % 2 == 0:
        height += 1

    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i + " " * spaces)
        # print(" " * spaces + "*" * i)


    for i in range(height-2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i + " " * spaces)
        # print(" " * spaces + "*" * i)

tinggiDiamond = int(input("hayo mau setinggi apa: "))
diamondGlenn(tinggiDiamond)
