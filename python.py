def main():
    # name, house = get_student()
    student = get_student()
    # name = get_name()
    # house = get_house()
    # print(f"{name} is from {house}")
    if (
        student[0] == "padma"
    ):  # now think if we want our value to be mutable than returning tuple wont work, we need to change
        student[1] = "New Delhi"  # that to a list
    print(
        f"{student[0]} is from {student[1]}"
    )  # here we can access that tuple using index


# def get_name():
#     name = input("Name :")
#     return name


def get_student():
    name = input("Name :")
    house = input("House name:")
    return [
        name,
        house,
    ]  # If you are still using a comma you might think, it is returning two values but instead it is returning
    # a single tuple, inside of this tuple are two values. or we can just put paranthesis just to make it clear
    # to the reader that these aren't just two values...but instead only one tuple

    # WHEN WOULD YOU USE TUPLE VERSUS A LIST?
    # when you know that your values aren't gonna change, than why would use a datatype which allows them to be
    # change. It just invites mistakes and bugs down the line either by you or colleague who is interecting with
    # your code.


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
