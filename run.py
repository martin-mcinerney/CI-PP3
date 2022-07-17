def show_board(hit, miss, comp): 
    print('           Battleships\n')
    print('     0  1  2  3  4  5  6  7  8  9')

    place = 0
    for x in range(10):
        row = ''
        for y in range(10):
            ch = ' _ '
            if place in miss:
                ch = ' x '
            elif place in hit:
                ch = ' o '
            elif place in comp:
                ch = ' O '
            
            row = row + ch
            place = place + 1
        print(x, " ", row)

hit = [23,24,25]
miss = [45, 32, 76]
comp = [1,2]

show_board(hit, miss, comp )