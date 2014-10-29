from datetime import datetime
import sys

LIMIT = 1000
RESULT = []

"""
Using xrange()
"""
start = datetime.now()
numbers = xrange(2,LIMIT)
#numbers = xrange(500,5001)
RESULT = []
def is_prime(number):
    for n in xrange(2,number):
        if number == n:
            continue
        if number % n == 0:
            return False
    #print number
    return True

for number in numbers:
    if is_prime(number):
        RESULT.append(number)

end = datetime.now()
delta = end - start
print RESULT
print 'xrange():',delta, '# of primes:',len(RESULT)

#with open('primes.txt','w') as f:
#    f.write(str(RESULT));
#sys.exit("Done")

"""
Using xrange() descendent
"""
start = datetime.now()
numbers = xrange(2,LIMIT)
#numbers = xrange(500,5050)
RESULT = []
def is_prime(number):
    for n in xrange(number,1,-1):
        if number == n:
            continue
        if number % n == 0:
            return False
    return True

for number in numbers:
    if is_prime(number):
        RESULT.append(number)

end = datetime.now()

delta = end - start
print RESULT
print 'xrange() descendent:',delta, '# of primes:',len(RESULT)


"""
Using range()
"""
start = datetime.now()
numbers = range(2,LIMIT)
#numbers = range(50,500)
RESULT = []
def is_prime(number):
    for n in range(2,number):
        if number == n:
            continue
        if number % n == 0:
            return False
    return True

for number in numbers:
    if is_prime(number):
        RESULT.append(number)

end = datetime.now()

delta = end - start
print RESULT
print 'range():',delta, '# of primes:',len(RESULT)

"""
Different approach
"""
start = datetime.now()
primes = [True] * LIMIT
RESULT = []
for index,number in enumerate(primes):
    if (index < 2):
        continue
    for t_index,t_number in enumerate(primes[index:]):
        x = t_index + index
        if (x == index):
            continue
        if (x % index) == 0:
            primes[x] = False

for i,p in enumerate(primes):
    if p:
        RESULT.append(i)
print RESULT[2:]

end = datetime.now()
delta = end - start
print "Different approach:",delta, '# of primes:',len(RESULT[2:])