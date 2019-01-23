#file 2 : lambda2.py
def my func(n):
	return lambda a : a * n 
	
my doubler = my func(2)
my tripler = my func(3)
dub = mydoubler(11)
trip = my tripler(12)

print("dub ",dub)
print("trip" ,trip)
