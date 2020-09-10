from ctypes import CDLL

obj= CDLL("cube_cuberoot.so")


def cube_a_number(num: int) -> int:
    return obj.cube_a_number(num)

def cube_2digit_number(num: int) -> int:
    return obj.cube_2digit_number(num)

def cuberoot_under_1000000(num: int) -> int:
    return obj.cuberoot_under_1000000(num)
