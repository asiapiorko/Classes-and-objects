# Problem 5
# 10/10 points (graded)
# Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have
# the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is
# 1*4 + 2*5 + 3*6, meaning your function should return: 32

# Hint: You will need to traverse both lists in parallel.

# This function takes in two lists of numbers and returns a number.

# def dotProduct(listA, listB):
#     '''
#     listA: a list of numbers
#     listB: a list of numbers of the same length as listA
#     '''
#     # Your code here
    
# First solution
def dotProduct(listA, listB):
    list = []
    result = 0
    
    for i in range(len(listA)):
        result = listA[i] * listB[i]
        list.append(result)
        for e in range(0, len(list)-1):
            result += list[e]
    return result
  
#Improvement

def dotProduct(listA, listB):
    result = 0
    
    for i in range(len(listA)):
        result += listA[i] * listB[i]
    return result
