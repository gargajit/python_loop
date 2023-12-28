
'''
def main():
    tall = int(input("How tall you want the tower to be? "))
    create_column(tall)

#Column blocks
\'''
def create_column(n):
    for _ in range(n):
        print("#")
\'''

#Different way
def create_column(n):
    print("#\n" * n, end="")

main()
'''

# Row blocks
'''
def main():
    wide = int(input("How wide you want the slab to be? "))
    create_row(wide)

def create_row(n):
    print("?" * n)

main()
'''

# Square blocks - Normal
'''
def main():
    sq_block = int(input("Size of square block? "))
    create_block1(sq_block)
    print()
    create_block2(sq_block)

# One way
def create_block1(n):
    # For each row in square
    for _ in range(n):
        # For each brick in row
        for _ in range(n):
            # Print brick
            print("#", end="")
        #New line before new row starts
        print()

# Second way
def create_block2(n):
    for _ in range(n):
        print("#" * n)


main()
'''

# Square block - Abstraction

def main():
    sq_block = int(input("Size of square block? "))
    create_block(sq_block)

def create_block(size):
    for _ in range(size):
        create_row(size)

def create_row(width):
    print("#" * width)

main()
