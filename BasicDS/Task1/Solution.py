from Stack import Stack


def check_brackets(code: str):
    brackets = ['(', ')', '{', "}", '[', ']']
    code = code.split('')
    stack = Stack()
    for symbol in code:
        if symbol in brackets:
            stack.push(symbol)


code = input()
check_brackets(code)
