#! python3
# collatz.py - Collatz conjecture

def collatz(num):
    if num != 1:
        if num % 2 == 0:
            num = num // 2
            print(num)
        else:
            num = (3 * num) + 1
            print(num)
        collatz(num)

def main():
    try:
        num = int(input("Enter a number: "))
        collatz(num)
    except ValueError:
        print("You must enter an integer.")

main()