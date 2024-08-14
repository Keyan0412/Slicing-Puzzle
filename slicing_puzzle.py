
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
 
exam = [[1, 2, 3],
		 
		[4, 5, 6],
		 
		[7, 8, '']]
 
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

