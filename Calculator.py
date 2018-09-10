#!/usr/bin/python

import sys


operators = {
    "+": {
        "prio": 0,
        "calc": lambda num1, num2: num1 + num2,
    },
    "-": {
        "prio": 0,
        "calc": lambda num1, num2: num1 - num2,
    },
    "*": {
        "prio": 1,
        "calc": lambda num1, num2: num1 * num2,
    },
    "/": {
        "prio": 1,
        "calc": lambda num1, num2: num1 / num2,
    },
}


def calc(num1, op, num2):
    c = operators[op]["calc"]
    return c(num2, num1)


def is_num(s):
    return s not in operators.keys()


def is_op(s):
    return s in operators.keys()


def read(chars, check):
    if len(chars) <= 0:
        return ""

    s = ""
    c = chars[-1]
    while check(c):
        chars.pop()
        s += c
        if len(chars) <= 0:
            break
        c = chars[-1]

    return s


def read_num(chars):
    num = read(chars, is_num)
    if len(num) <= 0:
        print("num is empty")
        sys.exit(1)
    return float(num)


def read_op(chars):
    op = read(chars, is_op)
    return op


def main():
    expstring = input('Input your expression: ')
    chars = list(expstring)
    chars.reverse()

    nums = []
    ops = []

    nums.append(read_num(chars))

    while True:
        op = read_op(chars)
        if len(op) <= 0:
            break
        prio = operators[op]["prio"]

        if len(ops) <= 0:
            ops.append(op)
        else:
            lastOp = ops[-1]
            while len(ops) > 0 and operators[lastOp]["prio"] >= prio:
                lastOp = ops.pop()
                num1 = nums.pop()
                num2 = nums.pop()
                result = calc(num1, lastOp, num2)
                nums.append(result)
            ops.append(op)

        nums.append(read_num(chars))

    while len(ops) > 0 and len(nums) > 0:
        op, num1, num2 = ops.pop(), nums.pop(), nums.pop()
        result = calc(num1, op, num2)
        nums.append(result)

    print("Result:", nums.pop())


if __name__ == '__main__':
    main()
