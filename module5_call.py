from module5_mod import NumberCollection


def main():
    n = int(input("Enter N: "))

    collection = NumberCollection()

    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))
        collection.insert_number(number)

    x = int(input("Enter X: "))

    result = collection.search_number(x)
    print(result)


if __name__ == "__main__":
    main()