running = True

print("Welcome to my calculator!")
while running:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. QUIT")
    cmd = int(input("Enter something valid : "))
    if cmd == 1:
        print("Now Adding")
        first=  int(input("Enter first number: "))
        second= int(input("Enter second number: "))
        result= first + second
        print(first, '+' , second , '=' , result)
    elif cmd == 2:
        print("Now subtracting")
        first=  int(input("Enter first number: "))
        second= int(input("Enter second number: "))
        result= first - second
        print(first, '-' , second,'=',result)
    elif cmd==3:
        print("Now multiplying")
        first=  int(input("Enter first number: "))
        second= int(input("Enter second number: "))
        result= first * second
        print(first, '*' , second ,'=',result)
    elif cmd==4:
        print("Now dividing")
        first=  int(input("Enter first number: "))
        second= int(input("Enter second number: "))
        result= first / second
        print(first, '/' , second ,'=',result)
    elif cmd == 5:
        print("Now quitting...")
        running = False
    else :
        print("Invalid Input.")
