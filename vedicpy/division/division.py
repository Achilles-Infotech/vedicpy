from ctypes import CDLL

obj= CDLL("division/division.so")


def division_by9(num: int):
    obj.division_by9(num)
