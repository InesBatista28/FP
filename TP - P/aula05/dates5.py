def parseMDY(date):
    parts = date.split("/")   #tira os / da data
    if len(parts) == 3:
        return (parts[2], parts[0], parts[1])
    else:
        return (parts[0], 0, 0)

def yearsBetween(date1, date2):  #rever segundo if
    ano1 = date1[0]
    ano2 = date2[0]
    if ano1 > ano2:
        numero = ano1 - ano2
    else:
        numero = ano2 - ano1
    if (date2[1], date2[0]) < (date1[1], date1[0]):
        numero -= 1
    return numero


def main():
    # Test parseMDY
    print(f"{parseMDY('12/25/2024') = }")  # (2024, 12, 25)
    print(f"{parseMDY('4/25/1974') = }")   # (1974, 4, 25)
    print(f"{parseMDY('1755') = }")        # (1755, 0, 0)

    # Test yearsBetween
    print(f"{yearsBetween((1900, 6, 1), (1935, 5, 31)) = }")  # 34
    print(f"{yearsBetween((1900, 6, 1), (1935, 6, 1)) = }")   # 35
    print(f"{yearsBetween((1900, 6, 1), (1936, 5, 31)) = }")  # 35


# This program may be used as a module too
if __name__ == "__main__":
    main()

