#!python3
# Write a program that uses a for loop to ask the user to enter
# in 5 numbers.  The program will determine the sum of the 5 numbers
# and calculate the average
# You must use only 1 input statement in your program

z=0
for i in range(1, 6):
    x=int(input("Enter a number: "))
    z+=x
    y=z/5
print(f"the sum of the 5 numbers is {z} and the average is {y}")