def rules():
    print("FizzBuzz will count to 100, but call multiples of certain numbers fizz, and others buzz. YOU will provide those 2 numbers, and out comes... FizzBuzz!")

def fizzbuzz(x, y):
    for i in range(1, 101):
        if (i % x == 0) & (i % y == 0):
            print("FizzBuzz!")
        elif (i % x == 0):
            print("Fizz")
        elif (i % y == 0):
            print("Buzz!")
        else:
            print(i)
    

new = input("Welcome to FizzBuzz! Would you like to hear the rules before we start? ")

yes = ("y", "ye", "yes", "Y", "Ye", "Yes")
no = ("n", "no", "N", "No")

if new in no:
    a = int(input("Give me your first number. "))
    b = int(input("Now your second number. "))
    fizzbuzz(a, b)
elif new in yes:
    rules()
    late = input("Do you understand now? ")
    if late in yes:
        a = int(input("Give me your first number. "))
        b = int(input("Now your second number. "))
        fizzbuzz(a, b)

