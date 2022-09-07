msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msgs = [msg_0,
        msg_1,
        msg_2,
        msg_3,
        msg_4,
        msg_5,
        msg_6,
        msg_7,
        msg_8,
        msg_9,
        msg_10,
        msg_11,
        msg_12]

memory = 0.0

# def change_memory(new_value):


def evaluate(x, operation, y):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y


def is_one_digit(value):
    value = float(value)
    return value.is_integer() and -10 < value < 10


def check(x, operation, y):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    x = float(x)
    y = float(y)
    if (x == 1.0 or y == 1.0) and operation == '*':
        msg = msg + msg_7
    if (x == 0 or y == 0) and operation in ['*', '+', '-']:
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def torture(possible_result):
    global memory
    is_user_sure = False
    if is_one_digit(possible_result):
        for i in range(10, 13):
            print(msgs[i])
            answer = input()
            if answer == 'y':
                if i == 12:
                    is_user_sure = True
                continue
            else:
                break
    else:
        memory = possible_result

    if is_user_sure:
        # global memory
        memory = possible_result


while True:
    print(msg_0)
    x, operation, y = input().split()
    try:
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        check(x, operation, y)
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    else:
        if operation not in ['+', '-', '*', '/']:
            print(msg_2)
            continue
        else:
            try:
                result = evaluate(x, operation, y)

            except ZeroDivisionError:
                print(msg_3)
                continue
            else:
                print(result)
                print(msg_4)
                is_result_stored = input()
                if is_result_stored == 'y':
                    torture(result)
                    print(msg_5)
                    do_continue_calculation = input()
                    if do_continue_calculation == 'y':
                        continue
                    else:
                        break
                else:
                    print(msg_5)
                    do_continue_calculation = input()
                    if do_continue_calculation == 'y':
                        continue
                    else:
                        break
