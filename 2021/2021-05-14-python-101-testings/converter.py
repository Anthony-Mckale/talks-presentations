#!/usr/bin/env python

##########################################################################################
##########################################################################################
##########################################################################################
# IF YOU ARE DOING THE NEW STARTER TRAINING
#
# DO NOT COPY THIS CODE, DO NOT "TAKE INSPIRATION FROM THIS CODE"
#
# YOU SHOULD WRITE YOUR OWN CODE AND DEVELOP YOUR OWN ALGORITHM FOR THE CONVERTERS
##########################################################################################
##########################################################################################
##########################################################################################

def to_arabic_number(roman_numeral: str) -> int:
    src_roman_numeral = roman_numeral
    # print(f"convert to_arabic_number {roman_numeral} into arabic number")
    arabic_number = 0
    numerals = {
        "M": 1000,
        "CM":  900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    # print(f"1) Check numerals in order of size {numerals}")
    for numeral in numerals:
        numeral_value = numerals[numeral]
        # print(f" 2) Check for repeated {numeral} ({numeral_value})")
        while roman_numeral.startswith(numeral):
            # print(f"  3) When found {numeral}, add {numeral_value}, remove {numeral} from current str {roman_numeral}")
            arabic_number += numeral_value
            roman_numeral = roman_numeral[len(numeral):]
            # print(f"   4) Current arabic number is {arabic_number}, numeral left to parse is {roman_numeral}")

    # print(f"to_arabic_number({src_roman_numeral}) is {arabic_number}")
    return arabic_number

def to_roman_numeral(arabic_number: int) -> str:
    src_arabic_number = arabic_number
    # print(f"convert to_roman_numeral {arabic_number} into roman numeral")
    roman_numeral = ""
    numerals = {
        "M": 1000,
        "CM":  900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    # print(f"1) Check numerals in order of size {numerals}")
    for numeral in numerals:
        numeral_value = numerals[numeral]
        # print(f" 2) Check for repeated {numeral} ({numeral_value})")
        while arabic_number >= numeral_value:
            # print(f"  3) When found {numeral}, remove {numeral_value}, add {numeral} to {roman_numeral} from current number {arabic_number}")
            roman_numeral += numeral
            arabic_number -= numeral_value
            # print(f"   4) Current numeral is {roman_numeral}, arabic number left to parse is {arabic_number}")

    # print(f"to_roman_numeral({src_arabic_number}) is {roman_numeral}")
    return roman_numeral
#
# print("""generating pseudo code for training
# =====================
#
# """)
#
# print("""
# Roman to Arabic Pseudo Code
# =====================================""")
# output = to_arabic_number('MCDIV')
# print(output)
#
# print("""
# Arabic to Roman Pseudo Code
# =====================================""")
# output = to_roman_numeral(2456)
#
# print(output)