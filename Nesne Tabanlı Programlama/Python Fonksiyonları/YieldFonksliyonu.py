def sayi_uret():
    for i in range(1,6):
        yield i**2


generator = sayi_uret()

iterator = iter(generator)

print(next(iterator))

print(next(iterator))



