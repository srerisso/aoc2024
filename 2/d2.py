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
def level_security(A):
    secure = 0
    for j in range(len(A) - 1):
        if A[j] < A[j + 1]:
            if A[j + 1] - A[j] > 3:
                secure = 0
                break
            else:
                secure = 1
        elif A[j] > A[j + 1]:
            if A[j] - A[j + 1] > 3:
                secure = 0
                break
            else:
                secure = 1
        else:
            secure = 0
            break
    return secure

# function level_security2. Given a list of levels, test if security checks are passed.
# Using list_increase and list_decrease functions
def level_security2(A):
    secure = 0
    
    if list_increase(A) == 0 or list_decrease(A) == 0:
        secure = 0      
    else:
        for j in range(len(A) - 1):
            if abs(A[j + 1] - A[j]) > 3:
                secure = 0
                break
            else:
                secure = 1
    return secure

# function list_increase. Returns 1 if the list is increasing, 0 otherwise
def list_increase(A):
    for i in range(len(A) - 1):
        if (A[i] > A[i + 1]) or (A[i] == A[i + 1]):
            return 0
    return 1

# function list_decrease. Returns 1 if the list is decreasing, 0 otherwise
def list_decrease(A):
    for i in range(len(A) - 1):
        if (A[i] < A[i + 1]) or (A[i] == A[i + 1]):
            return 0
    return 1    

listA = extract_numbers('day2_input_test.txt')
listA.reverse()
print(f"List A: {listA}")

# for t in map(list_increase, listA):
#     print(f"List is increasing: {t}")

# print("***")
# for u in map(list_decrease, listA):
#     print(f"List is decreasing: {u}")

i=0

for e in map(level_security2, listA):
    print(f"Lista {i} is Secure: {e}")
    i=i+1
