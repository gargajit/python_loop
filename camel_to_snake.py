def main():
    camel_case = input("camelCase: ")
    snake_case = to_snake_case(camel_case)
    print("snake_case:", snake_case)


def to_snake_case(input):
    output = ""
    for s in input:
        if s.islower():
            output = output + s
        elif s.isupper():
            low = s.lower()
            output = output + '_' + low
            low = ''
    return output

main()
