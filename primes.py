"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes>0:
        currentprime =2
        while number_of_primes>len(list):
            multiples=False
            for i in range(currentprime+1):
                if i>1 and currentprime%i==0 and not currentprime==i:
                    multiples=True
                if currentprime==i and multiples==False:
                    list.append(currentprime)
            currentprime=currentprime+1
    else:
        raise ValueError(f'The number of primes you inserted : {number_of_primes} cannot be smaller than 1')
    return list
