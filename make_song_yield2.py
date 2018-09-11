def make_song(verses=99, beverage="soda"):
    for num in range(verses, 1, -1):
        yield "{} bottles of {} on the wall.".format(num, beverage)
    yield "Only 1 bottle of {} left!".format(beverage)
    yield "No more {}!".format(beverage)

#Exemplos
#default_song = make_song(5)
#print(next(default_song))
#print(next(default_song))
#print(next(default_song))
#print(next(default_song))
#print(next(default_song))
#print(next(default_song))
#print(next(default_song))
