import math
from math import  ceil
import functools
from functools import reduce
import random
PRIMELISTLENGTH = 10000
def findprimes(n): #find all positive primes up to n inclusive
		   #using Sieve of Archimedes
	primelist = [2]
	if n<2:
		return []
	else:
		startlist=range(2,n+1)
		for x in startlist:
			xIsPrime=True # Assume prime  
			stopper=ceil(x**0.5)
			for y in primelist:
				if y<=stopper:
					if x%y ==0:
						xIsPrime=False
				else:
					break
			if xIsPrime:
				primelist.append(x)
	return primelist    	


basicprimelist=findprimes(PRIMELISTLENGTH)

def isPrime(n):
	if n in basicprimelist:
		return True
	elif n < 1000:
		return False
	else: 
		primelist=findprimes(n)
		if n in primelist:
			return True
		else: return False

def factors(n):
	"""Return a list of prime factors, including duplicates, for any natural number. 0 and 1 return an empty list."""
	#chokelength = ceil(n**0.5)
	if n <= PRIMELISTLENGTH: 
		primelist= basicprimelist[:]
	else:
		primelist = findprimes(n)
	factorlist=[]
	mynumber=n
	checkfactor=primelist[0]
	while len(primelist) > 0:
		if n<=1:
			break
		if mynumber%checkfactor==0:
			mynumber=mynumber/checkfactor
			factorlist.append(checkfactor) 
		#	print len(primelist)
		else:
			del primelist[0]
			if len(primelist)>0:
				checkfactor = primelist[0]
	#	if isPrime(mynumber):
	##		break
	return factorlist
 
def totient(n):
	"""Return Euler's totient for any natural number, that is, return the number of numbers modulo n that have a multiplicative inverse."""
	if isPrime(n):
		return n-1
	else:
		return reduce(lambda x, y: x*y, map(lambda x: x-1, factors(n)))	

def largeRandomPrime(magnitude):
	start=int(ceil(random.random()*10**magnitude))
	while 1:
		if isPrime(start):
			return start
		else:
			start +=1

def uniques(listX):
	result = []
	for x in listX:
		if x not in result:
			result.append(x)
	return result

def shorter(list1, list2):
	if len(list1) < len(list2):
		return list1
	else:	return list2

def longer(list1, list2):
	if len(list1) > len(list2):
		return list1
	else:	return list2

def common (list1, list2):
	result =[]
	for x in uniques(list1):
		check1 = filter(lambda y: y == x, list1)
		check2 = filter(lambda y: y == x, list2)
		for y in shorter(check1, check2):
			result.append(y)
	return result

def merge(list1, list2):
	result =[]
	for x in uniques(list1):
		check1 = filter(lambda y: y == x, list1)
		check2 = filter(lambda y: y == x, list2)
		for y in longer(check1, check2):
			result.append(y)
	return result



def gcd(n, m):
	result = 1
	for x in common(factors(n), factors(m)):
		result *=x
	return result		
