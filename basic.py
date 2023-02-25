# + - * / % -> done 

# x , y
quit = "";
x = int();
y = int();

def add(x,y):
    z = x+y
    return z

def subtract(x,y):
    z = x-y
    return z

def multiply(x,y):
    z = x*y
    return z

def divide(x,y):
    z = x/y
    return z

def remainder(x,y):
    z = x%y
    return z

print("Welcome to Masoom Ahmad's Calculator");
print("press enter to continue \n or press q to quit");
while(input() != "q"):
    print("please enter the first number");
    x = int(input())
    print("please enter the second number");
    y = int(input())
    print("Please enter the operation from below that you want to perform \n add -> + \n subtract -> - \n mulitply -> * \n divide -> / \n remainder -> %");
    operation = input();

    if operation == "+":
        result = add(x,y);
        print(result)
    elif operation == "-":
        result = subtract(x,y);
        print(result);
    elif operation == "*":
        result = multiply(x,y);
        print(result);
    elif operation == "/":
        result = divide(x,y);
        print(result);
    elif operation == "%":
        result = remainder(x,y);
        print(result);
