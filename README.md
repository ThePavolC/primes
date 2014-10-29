primes
======

Python script comparing different ways to get prime numbers.

I was wondering how much of a difference would it make to use range,xrange, or list number in descendent order, or use slightly different algorithm. 

The results
===========
Get prime numbers in range [0:10000]
```
xrange(): 0:00:02.120000 # of primes: 1229
xrange() descendent: 0:00:08.437000 # of primes: 1229
range(): 0:00:03.632000 # of primes: 1229
Different approach: 0:00:59.807000 # of primes: 1229
```

Get prime numbers in range [0:1000]
```
xrange(): 0:00:00.040000 # of primes: 168
xrange() descendent: 0:00:00.164000 # of primes: 168
range(): 0:00:00.055000 # of primes: 168
Different approach: 0:00:00.796000 # of primes: 168
```
