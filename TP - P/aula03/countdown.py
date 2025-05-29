def countdown(N):
    for i in range(N, 0, -1):
        print(i)

def main():
    N = int(input("Enter a number: "))
    countdown(N)

main()