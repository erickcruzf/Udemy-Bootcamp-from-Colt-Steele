def make_song(num=99, drink='soda'):
    count=0
    while num-1 > count:
        yield '{} bottles of {} on the wall.'.format(num-count,drink)
        count += 1
    yield 'Only 1 bottle of {} left!'.format(drink)
    yield 'No more {}!'.format(drink)
    raise StopIteration

#Exemplos
#default_song = make_song(5)
#print(next(default_song))
#print(next(default_song))
#print(next(default_song))
#print(next(default_song))
#print(next(default_song))
#print(next(default_song))
#print(next(default_song))
