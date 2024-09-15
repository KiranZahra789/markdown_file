num_list = []
user_name = str(input("Enter your name :"))
for i in range(1,4):
     num : int = int(input(f"Enter your {i} favourite number:"))
     num_list.append(num)
print(f"\nHello , {user_name} !Lets explore your favourite number:")
for item in num_list:
    if item % 2 == 0:
        print(f"the number {item} is even")
    else:
        print(f"the number {item} is odd")

    for item in num_list:
            print(f"the number {item} and its square: ({item} , {item**2})")
    sum_of_num: int = sum(num_list)
    print(f"Amazing! the sum of your favourite numbers is {sum_of_num}")

    is_prime = True
    if sum_of_num <=1:
        is_prime = False
    for x in range (2,sum_of_num) :
        if sum_of_num % 2 ==  0:
            is_prime = False  
    if is_prime :
     print(f"Great job! the number {sum_of_num} is  a prime number.") 
    else:
        print(f"Great job! the number {sum_of_num} is not a prime number")          
