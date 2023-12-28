'''
for _ in range(3):
    print("meow")


#Pythonic way
print("meow\n" * 3, end = "")
'''

'''
count = int(input("How many times you want to the cat to meow? "))
for _ in range(count):
    print("meow")
'''


# We want to take the number from the user but only 
# when the number is positive we want to run the loop
# else we keep prompting user to give a correct number
'''
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''


# create a meow function

def main():
    n = int(input("What's n? "))
    meow(n)

def meow(n):
    for _ in range(n):
        print("meow")

main()
