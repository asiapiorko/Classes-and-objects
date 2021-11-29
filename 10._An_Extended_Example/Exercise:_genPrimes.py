# Exercise: genPrimes
# 5/5 points (graded)
# ESTIMATED TIME TO COMPLETE: 10 minutes

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 9, 11, ...



def genPrimes():
    first_number = 2 #first number
    second_number = 3 #second number
    while True:
        next = first_number + second_number
        first_number = first_number
        second_number = next
        yield next
