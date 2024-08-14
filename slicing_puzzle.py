import random
import sys


def print_info():
    print("Welcome to Jan's puzzle game!\n")

    info = '''Here is a brief introduction about this game:
    There is an empty block in each puzzle.
    You can slice adjacent blocks into the empty block.
    In this way, you can change the puzzle.
    Your will be prompted to transform the puzzle into a sequenced form.\n'''
    print(info)

    print('There is an example of the sequenced form:')
    exam = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, '']
    ]
    print_matrix(exam)
    print('\n')
    print('You can use any four english letters as the operation "up, down, left, right".')


def get_letters():
    scope_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                   'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                   'y', 'z']
    scope_big = []
    for letter in scope_small:
        scope_big.append(letter.upper())
    return scope_big + scope_small


def get_keys():
    """get the keys of operation from user
    """
    print()
    scope = get_letters()
    keys = {}
    direction = ['left', 'right', 'up', 'down']
    while True:
        point = 0
        input_key = input("Enter the four letters used for left, right, up and down move.(use space to separate them)>")
        key_list = input_key.split()
        if len(key_list) != 4:
            print('\nplease input four letters(a-z, A-Z), and use space to separate them.\n')
            continue
        for key in key_list:
            if key in scope and key not in keys.values():
                keys[direction[point]] = key
                point += 1
            else:
                print("\nplease input four letters(a-z, A-Z), and make sure you have not input the same letter twice\n")
                break
        else:
            return keys


def get_setting():
    """ get the original setting from user
    """
    while True:
        type_ = input('Enter “1” for 8-puzzle, “2” for 15-puzzle or “q” to end the game>')
        if type_ == '1':
            type_ = 9
            return type_
        elif type_ == '2':
            type_ = 16
            return type_
        elif type_ == 'q':
            sys.exit()
        else:
            print('invalid input, please input "1", "2" or "q"')


def init_matrix(type_):
    """This function is used to produce a random square matrix.
    There are n numbers in this matrix.
    It will also return the position of the empty block.
    """
    row_num = col_num = int(type_ ** 0.5)
    empty = []
    random_list = [i + 1 for i in range(type_)]

    # produce a random list with n numbers
    while True:
        random.shuffle(random_list)
        if check_list(random_list):
            break

    # get the position of the empty block
    for index in range(type_):
        if random_list[index] == type_:
            row, column = divmod(index + 1, row_num)
            if column == 0:
                column = row_num
                row -= 1
            empty = [row + 1, column]

    # transfer the numbers from the list into the matrix form
    matrix = []
    random_list = random_list[::-1]
    for row in range(row_num):
        matrix.append([])
        for col in range(col_num):
            matrix[row].append(random_list.pop())
    return matrix, empty


def check_list(sample):
    """check whether the puzzle of the list can be solved
    it detects the number of reversed number pairs
    """
    reversed_number = 0
    length = len(sample)
    for i in range(length):

        # the empty block is not calculated
        if sample[i] == length:
            continue

        for j in range(i + 1, length):

            # the empty block is not compared
            if sample[j] == length:
                continue

            if sample[i] > sample[j]:
                reversed_number += 1

    # consider the difference between 8-block and 15-block
    if length % 2 == 1:
        return reversed_number % 2 == 0
    else:
        if length in sample[0: 4] or length in sample[8: 12]:
            return reversed_number % 2 == 1
        else:
            return reversed_number % 2 == 0


def init_settings(type_):
    """initialize all the game settings
    """
    print('\nA new game starts!')
    matrix, empty = init_matrix(type_)
    if type_ == 9:
        final = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    else:
        final = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
    return matrix, empty, final


def print_matrix(matrix):
    """print the puzzle in the form of matrix
    """
    print()
    for row in matrix:
        for entry in row:
            if entry == len(row) ** 2:
                entry = ''
            print(' ', '{:>3}'.format(entry), end='')
        print(' ')


def check_operation(empty, length, keys):
    """anticipate what can be done to the puzzle
    """
    # anticipate up and down
    if empty[0] == length:
        row = f"down-{keys['down']}"
    elif empty[0] == 1:
        row = f"up-{keys['up']}"
    else:
        row = f"up-{keys['up']}, down-{keys['down']}"

    # anticipate left and right
    if empty[1] == length:
        column = f"right-{keys['right']}"
    elif empty[1] == 1:
        column = f"left-{keys['left']}"
    else:
        column = f"left-{keys['left']}, right-{keys['right']}"
    return row + ', ' + column


def move(keys, matrix, empty):
    """get the operation from user and perform it
    """
    length = len(matrix)
    flag = True
    operation = input(f'Enter your move.({check_operation(empty, length, keys)})>')
    if operation == keys['left']:
        if empty[1] != length:
            target = [empty[0], empty[1] + 1]
            matrix = exchange_entry(target, empty, matrix)
            empty = target
        else:
            print("This operation cannot be performed. Please input a valid operation.")

    elif operation == keys['right']:
        if empty[1] != 1:
            target = [empty[0], empty[1] - 1]
            matrix = exchange_entry(target, empty, matrix)
            empty = target
        else:
            print("This operation cannot be performed. Please input a valid operation.")

    elif operation == keys['up']:
        if empty[0] != length:
            target = [empty[0] + 1, empty[1]]
            matrix = exchange_entry(target, empty, matrix)
            empty = target
        else:
            print("This operation cannot be performed. Please input a valid operation.")

    elif operation == keys['down']:
        if empty[0] != 1:
            target = [empty[0] - 1, empty[1]]
            matrix = exchange_entry(target, empty, matrix)
            empty = target
        else:
            print("This operation cannot be performed. Please input a valid operation.")

    else:
        print('This operation cannot be performed. Please input a valid operation')
        flag = False

    return matrix, empty, flag


def exchange_entry(position1, position2, matrix):
    """exchange content between two positions in the matrix
    """
    temp = matrix[position1[0] - 1][position1[1] - 1]
    matrix[position1[0] - 1][position1[1] - 1] = matrix[position2[0] - 1][position2[1] - 1]
    matrix[position2[0] - 1][position2[1] - 1] = temp
    return matrix


def end(step):
    print(f'Congratulations! You solved the puzzle in {step} moves!')
    while True:
        re = input('Do you want to play again?(y/n)>')
        if re == 'n':
            sys.exit()
        elif re == 'y':
            break
        else:
            print("Please input 'y' or 'n'.")


def main():
    print_info()

    # get the keys of operations
    keys = get_keys()

    while True:
        # get the type of the puzzle
        type_ = get_setting()

        # get the settings of the puzzle
        matrix, empty, final = init_settings(type_)
        step = 0

        # start the game and stop it when the puzzle is solved
        while matrix != final:
            print_matrix(matrix)
            matrix, empty, flag = move(keys, matrix, empty)
            if flag:
                step += 1
        print_matrix(matrix)
        end(step)


if __name__ == '__main__':
    main()
