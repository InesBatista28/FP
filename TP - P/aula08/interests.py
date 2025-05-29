
def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }


    print("a) Table of common interests:")
    commoninterests = {}
    pessoas = list(interests.keys())
    for i in range(len(interests)):
        for j in range(i+1, len(interests)):
            pessoa1 = pessoas[i]
            pessoa2 = pessoas[j]
            comum = interests[pessoa1] & interests[pessoa2]
            commoninterests[(pessoa1, pessoa2)] = comum
    print(commoninterests)

    print("b) Maximum number of common interests:")
    maxCI = max(len(common) for common in commoninterests.values())
    print(maxCI)

    print("c) Pairs with maximum number of matching interests:")
    maxmatches = [pair for pair, common in commoninterests.items() if len(common) == maxCI]
    print(maxmatches)

    print("d) Pairs with low similarity:")


# Start program:
main()

