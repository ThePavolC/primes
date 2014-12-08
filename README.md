primes
======

Python script comparing different ways to get prime numbers.

I was wondering how much of a difference would it make to use range,xrange, or list number in descendent order, or use slightly different algorithm. 

The results
===========
Get prime numbers in range [0:10000]
```
xrange(): 0:00:02.528000 # of primes: 1229
xrange() descendent: 0:00:13.766000 # of primes: 1229
range(): 0:00:03.263000 # of primes: 1229
Different approach: 0:01:03.996000 # of primes: 1229
filter(f,range): 0:00:04.137000 # of primes: 1229
filter(f,xrange): 0:00:02.216000 # of primes: 1229
```

Get prime numbers in range [0:1000]
```
xrange(): 0:00:00.044000 # of primes: 168
xrange() descendent: 0:00:00.168000 # of primes: 168
range(): 0:00:00.054000 # of primes: 168
Different approach: 0:00:00.775000 # of primes: 168
filter(f,range): 0:00:00.044000 # of primes: 168
filter(f,xrange): 0:00:00.041000 # of primes: 168
```
