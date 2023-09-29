# Overview
# This file provide function CompStrVal to compare two numbers 
# s1, s2 represented by string.

# Functionality
# The program is able to receive extremely large input value
# The program checks validity of user's input

# Limitation
# The program can't handle symbol representation of number, 
#   such as "inf"
# The program's helper function is visible to user. it lacks of privacy.
# This program is not adaptable to change. Increasing its functionality 
#   requires a lot of effort.


    

# compare s1 and s2
# return 1 if s1 > s2, 0 if s1 = s2, -1 otherwise
def CompStrVal(s1: str, s2: str):
    # check validity
    try:
        assert _validVal(s1) and _validVal(s2)
    except Exception as e:
        print(f"invalid input")

    # Handle negative numbers
    neg1, neg2 = s1.startswith("-"), s2.startswith("-")
    s1, s2 = s1.lstrip("-"), s2.lstrip("-")

    dot_index1, dot_index2 = s1.find("."), s2.find(".")
    s1_int, s1_float = (s1[:dot_index1], s1[dot_index1+1:]) if dot_index1 != -1 else (s1, "")
    s2_int, s2_float = (s2[:dot_index2], s2[dot_index2+1:]) if dot_index2 != -1 else (s2, "")

    # Compare integer parts
    result_int = _compInt(s1_int, s2_int)
    # Compare decimal parts if integer parts are equal
    result_float = _compDec(s1_float, s2_float) if result_int == 0 else 0

    # Determine the overall comparison result
    result = result_int if result_int != 0 else result_float

    # Adjust the result for negative numbers
    if neg1 and not neg2 and s1 != "0" and s2 != "0":
        return -1
    elif not neg1 and neg2 and s1 != "0" and s2 != "0":
        return 1
    elif neg1 and neg2:
        return -result

    return result


# return true if the input value is valid, false otherwise
def _validVal(s: str):

    if len(s) == 0:
        return False
    
    # multiple "."
    if s.count(".") > 1 :
        return False
    
    # invalid "-"
    if s.count("-") > 1:
        return False
    if s.count("-") == 1 and not s.startswith("-"):
        return False
    
    s = s.lstrip("-")
    
    # beginning with 0 but not a float
    if len(s) > 1 and s.startswith("0") and not s.startswith("0."):
        return False
    
    # check s contains valid decimal
    dot_index = s.find(".")
    if dot_index == -1:
        return s.isdecimal()
    else:
        return s[:dot_index].isdecimal() \
                and (s[dot_index+1:] + "0").isdecimal() 
                # add "0" in case of empty substring


# return 1 if s1 > s2,0 if s1 = s2, -1 if s1 < s2
# s1, s2 behind the decimal
def _compDec(s1: str, s2: str):
    for i in range(min(len(s1), len(s2))):
        if int(s1[i]) > int(s2[i]):
            return 1
        elif int(s1[i]) < int(s2[i]):
            return -1 

    # same previous value, compare length
    if len(s1) == len(s2):
        return 0
    elif len(s1) > len(s2):
        return 1
    else:
        return -1


# return 1 if s1 > s2, 0 if s1 = s2, -1 if s1 < s2
# s1, s2 are integer part
def _compInt(s1: str, s2: str):

    if len(s1) > len(s2):
        return 1
    elif len(s1) < len(s2):
        return -1
    
    for i in range(min(len(s1), len(s2))):
        if int(s1[i]) > int(s2[i]):
            return 1
        elif int(s1[i]) < int(s2[i]):
            return -1 
    
    return 0







   
