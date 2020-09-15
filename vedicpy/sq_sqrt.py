from ctypes import CDLL
import os

path= os.path.abspath(os.path.join( 'vedicpy', 'C program files', 'sq_sqrt.so'))
obj= CDLL(path)


def square_ending5(num: int) -> int:
    return obj.square_ending5(num)

def square_near_powerof10(num: int) -> int:
    return obj.square_near_powerof10(num)

def square_under100(num: int) -> int:
    return obj.square_under100(num)

def square_from100_to1000(num: int) -> int:
    return obj.square_from100_to1000(num)

def perfect_sqrt_under_sqof100(num: int) -> int:
    return obj.perfect_sqrt_under_sqof100(num)
