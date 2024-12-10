# AOC 2024
# Day 2

# Find which levels are secure

# function extract_numbers. Extracts numbers from a file and returns them as lists.

# file is formatted as reports on each line. Each report consists of a serie of numbers that indicate the levels of security.
# A list of lists is returned. Each list contains the levels of security for a report.
def extract_numbers(file1):
    A = []

    with open(file1, 'r') as file:
        for line in file:
            parts = line.strip().split()
            partsInt = list(map(int, parts))
            # print(parts)
            A.insert(0,partsInt)
                    
    return A

# function level_security. Given a list of levels, test if security checks are passed.
#
# security checks :
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three
# def level_security(A):
#     secure = 0
#     for j in range(len(A) - 1):
#         if A[j] < A[j + 1]:
#             if A[j + 1] - A[j] > 3:
#                 secure = 0
#                 break
#             else:
#                 secure = 1
#         elif A[j] > A[j + 1]:
#             if A[j] - A[j + 1] > 3:
#                 secure = 0
#                 break
#             else:
#                 secure = 1
#         else:
#             secure = 0
#             break
#     return secure

# function level_security2. Given a list of levels, test if security checks are passed.
# Using list_increase and list_decrease functions
def level_security(A):
    secure = 0

    for j in range(len(A) - 1):
        if list_increase(A) == 1:
            if abs(A[j + 1] - A[j]) > 3:
                secure = 0
                break
            else:
                secure = 1
        elif list_decrease(A) == 1:   
            if abs(A[j] - A[j + 1]) > 3:
                secure = 0
                break
            else:
                secure = 1

    return secure

# function list_increase. Returns 1 if the list is increasing, 0 otherwise
def list_increase(A):
    j=0
    
    for j in range(len(A) - 1):
        if (A[j] > A[j + 1]) or (A[j] == A[j + 1]):
            return 0
    return 1

# function list_decrease. Returns 1 if the list is decreasing, 0 otherwise
def list_decrease(A):
    k=0
    
    for k in range(len(A) - 1):
        if (A[k] < A[k+ 1]) or (A[k] == A[k+ 1]):
            return 0
    return 1    

# listA = extract_numbers('day2_input_test.txt')
listA = extract_numbers('day2_input_test.txt')
listA.reverse()
# print(f"listA: {listA}")

# for t in map(list_increase, listA):
#     print(f"List is increasing: {t}")

# print("***")
# for u in map(list_decrease, listA):
#     print(f"List is decreasing: {u}")

i=0
count_safes = 0

for e in map(level_security, listA):
    # print(f"Lista {i+1} is Secure: {e}")
    if e == 1:
        count_safes = count_safes + 1
    i=i+1
    
print(f"Number of secure lists: {count_safes}")


# Part 2
# Problem Dampener

# Cases where the Problem Dampener can remove a level :
#   - Next element is equal than actual element (increment_list is 0). Then remove actual element.
#   - There is a difference of sign between two adjacent elements of increments_list. Then remove the element with the different sign.

#  increments_list scenarios, to be analyzed by Problem Dampener:
#
# - all negative, no increment greater than 3 => Level is secure (1)
# - all positive, no increment greater than 3 => Level is secure (1)
# - all positive, but one negative, and no increment greater than 3 => Level secure (1) when negative is deleted
# - all negative, but one positive and no increment greater than 3 => Level secure (1) when positive is deleted
# - and increment greater than 3 => can it be removed ?. NO, level is not secure (0)

# list_increments function. Given a list, returns all increments between elements
def list_increments(eleA):
    inc = []
    i = 0
    
    for i in range(len(eleA) - 1):
        inc.append(eleA[i + 1] - eleA[i])
    return inc

increments_list = []
for el in listA:
    # print(f"List increments: {list_increments(el)}")
    increments_list.append(list_increments(el))
    

# function all_incs_below_4. Given a list, returns 1 if all increments are below 3 (in absolute value), 0 otherwise
def all_incs_below_4(listA):
    below = True
    
    for i in range(len(listA) - 1):
        if abs(listA[i]) > 3:
            below = False
            break
    return below

# function any_negative. Given a list, returns 1 if there is any negative number in the list, 0 otherwise
def any_negative(lista) -> bool:
    return any(x < 0 for x in lista)

# function problem_dampener. Given a list of levels, and a list of increments of those levels, test if security checks are passed, and apply selected corrections to make levels secure
def problem_dampener(listA, increments_list):
    secure = 0
    i = 0
    secure_list = listA
    secure_increments_list = increments_list
    
    for i in range(len(increments_list)-1):
        if all_incs_below_4(increments_list[el]) == 1:
            if (list_increase(increments_list[el]) == 1) and (not(any_negative(increments_list[el]))):
                secure = 1
                secure_list[i] = listA[i]
                secure_increments_list[i] = increments_list[i]
            else:
                secure = 0
                break
            elif list_decrease(el) == 1:
                secure = 1
                secure_list[i] = listA[i]
                secure_increments_list[i] = increments_list[i]
            else:
                secure = 0
                break
        else:
            secure = 0
            break
        i += 1


    return secure_list, secure_increments_list

print(f"List A: {listA}")
print(f"Increments_list: {increments_list}")
#     print(f"List {i} increments: {list_increments(el)}")
# for el in increments_list:
#     print(f"All incs below 4 in list {i} ?: {all_incs_below_4(el)}")
#     i +=1
#     print(f"Different signs in list {i} ?: {find_different_signs(el)}")

# for el in listA:
#     print(f"List secure {i}: {problem_dampener(el)}")
#     i += 1

print(f"problem_dampener: {problem_dampener(listA, increments_list)}")

# print(f"Increments list (print2): {increments_list}")
# print(f"List A (print 2): {listA}")