from area_circle import area_of_circle
from area_rect import area_of_rect
from square import array_of_square


def main():
    # length: int = int(input("Enter length: "))
    # width: int = int(input("Enter width: "))
    # print("area_of_rect", area_of_rect(length, width))
    # radius: int = int(input("Enter radius: "))
    # print("area_of_circle", area_of_circle(radius))
    # squares = [2, 3, 4, 5, 6, 7]
    input_str = input("Enter value: ")
    items: list[str] = input_str.split()
    numbers: list[int] =[int(item) for item in items]

    print("array_of_list", array_of_square(numbers))


if __name__ == '__main__':
    main()
