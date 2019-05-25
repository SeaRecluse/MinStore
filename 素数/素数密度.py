import time

n = 10000000

def isPrime(n):
	if n == 2 or n==3:
		return n
	tmp = n % 6
	if tmp!=1 and tmp!=5:
		return 0

	limit = int(n**0.5) + 1

	for i in range(5,limit,6):
		if (n%i == 0) | (n%(i+2) == 0):
			return 0
	return n

start = time.time()
allPrimes = [i for i in range(2,n) if isPrime(i) > 0]
# print(allPrimes)
print(len(allPrimes)/n)
print(str(time.time() - start) + " s")

def isPrime2(n):
	limit = int(n**0.5) + 1

	for i in range(2,limit):
		if (n%i == 0):
			return 0
	return n

start = time.time()
allPrimes2 = [i for i in range(2,n) if isPrime2(i) > 0]
# print(allPrimes2)
print(len(allPrimes2)/n)
print(str(time.time() - start) + " s")