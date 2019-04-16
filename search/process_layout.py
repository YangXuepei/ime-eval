best_for_now = {'a': 5, 'c': 16, 'b': 15, 'e': 11, 'd': 8, 'g': 4, 'f': 18, 'i': 14, 'h': 1, 'k': 17, 'j': 13, 'm': 9, 'l': 13, 'o': 3, 'n': 6, 'q': 17, 'p': 7, 's': 12, 'r': 18, 'u': 10, 't': 16, 'w': 15, 'v': 7, 'y': 2, 'x': 9, 'z': 2}

def print_the_layout(layout):
    result  = {}
    for i in range(1,19):
        result[i] = ''
    for i in layout:
        result[layout[i]] += i + ' '

    print result[1],'\t\t',result[2],'\t\t',result[3],'\t\t\t',result[10], '\t\t', result[11], '\t\t', result[12]
    print result[4],'\t\t',result[5],'\t\t',result[6],'\t\t\t',result[13], '\t\t', result[14], '\t\t', result[15]
    print result[7],'\t\t',result[8],'\t\t',result[9],'\t\t\t',result[16], '\t\t', result[17], '\t\t', result[18]

#print_the_layout(l)