def my_generator (n):
    i = 0
    while i < n+1:
        yield i
        i += 1
     
counter = my_generator(100)
print(list(counter))
    
def my_gen():
    for i in range(100):
        yield i
gen = my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
