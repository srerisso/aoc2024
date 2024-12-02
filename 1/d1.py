# AOC 2024
# Day 1

# Part 1. Given a list of numbers, find the sum of the absolute differences between the numbers in the list.

# Read input file
# Create lists

# function extract_numbers. Extracts numbers from a file and returns them as lists
# file is formatted as two columns of numbers. Each line has two numbers separated by a space
def extract_numbers(file1):
    A = []
    B = []

    with open(file1, 'r') as file:
        for line in file:
            parts = line.strip().split()
            # print(parts)
            A.append(int(parts[0]))
            B.append(int(parts[1]))
        
    return A, B

# function order_list. Orders a list. Returns the ordered list.
def order_list(A):
    A.sort()
    return A

# function sum_list. Sums a list elements. Returns the sum
def sum_list(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    return sum

A, B = extract_numbers('d1p1.txt')
print(f"List A: {order_list(A)}")
print(f"List B: {order_list(B)}")

D = []
    
for i in range(len(A)):
    D.append(abs(A[i] - B[i]))
    
print(f"List D: {sum_list(D)}")


# Part 2

# similarity_score
# how often a number from list A appears in list B

# multiply number from list A * times that it appears in list B
# sum all the results
