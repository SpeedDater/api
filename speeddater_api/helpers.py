from rest_framework.pagination import PageNumberPagination
import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class PageNumberPagination25(PageNumberPagination):
    '''
    Standard DRF PageNumberPagination, with default page size of 25.
    '''
    page_size = 25


def num_digits(number):
    '''
    Returns the number of digits in number.
    '''
    return int(number / 10)


def first_n_digits(num, n):
    '''
    Returns the first n digits in number.
    '''
    return num // 10 ** (int(math.log(num, 10)) - n + 1)
