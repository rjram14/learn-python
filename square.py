def array_of_square(squares: list[int]) -> list[int]:
    # ans = []
    # for square in squares:
    #     if square * square > 45:
    #         ans.append(square * square)
    # return ans
    return [square * square for square in squares if square * square > 35]


    # colors = ["red", "b", "c", "d"]
    # for color in colors:
    #     print("color", color)
    # for i in range(0, 4, 2):
    #     print(i)
    # i = 0
    # while i < 8:
    #     i += 1
    #
    # if a == 6:
    #     print()
    # elif a == 9:
    #     print()
    # else:
    #     print()
