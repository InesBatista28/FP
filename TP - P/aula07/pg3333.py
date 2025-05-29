with open("pg3333.txt", "r", encoding='utf-8') as file:
    dict = {}
    lines = file.readlines()
    for line in lines:
        for i in line:
            if i.isalpha():
                i = i.lower()
                if i in dict:
                    dict[i] += 1
                else:
                    dict[i] = 1

for i in dict:
    print("{} {}".format(i, dict[i]))