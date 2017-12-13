import re


def match(word):
    pattern_array = ["CVCVC", "VCVCV", "CCVVC", "VVCCV", "CVCCV", "CCVCV",
                     "VVCVC", "VCVVC", "VCCVC", "CVVCV", "CVVCC" "NCVCV",
                     "NCVVC", "NCCVV", "NVCVC", "NVVCC", "NVCCV", "CCVNN",
                     "CVCNN", "VCCNN", "VCVNN", "VVCNN", "CVVNN"]
    if footprint(word) in pattern_array:
        return True
    else:
        return False


def footprint(word):
    footprint = ""
    for char in word:
        if char in "aeiouy":
            footprint += "V"
        elif char in "1234567890":
            footprint += "N"
        elif char in "bcdfghjklmnpqrstvwxz":
            footprint += "C"
        else:
            footprint += "X"
    return footprint
