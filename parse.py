# Diego Mendez
# 801-17-4052

"""
NOTE: this function is called automatically in the files 'wsclock.py', 'optimal.py' and 'lifo.py' in their main function

1. parse: returns an array called pages and that array will contain all of our pages. This function takes in consideration that each access
   may be separated by a space or a new line. The argument of this function is:
   contents: this is what is stored in the 'sequence.txt'
"""

def parse(contents):
    pages = []
    for i in range(len(contents)):
        j = 0
        while j in range(len(contents[i])):
            character = contents[i][j]
            if contents[i][j] == 'R' or contents[i][j] == 'W' or contents[i][j] == ':' or contents[i][j] == '\n' or contents[i][j] == ' ':
                j += 1
            else:
                num = contents[i][j]
                k = j + 1
                while k <= len(contents[i])-1 and contents[i][k] != ' ':
                    num = num + contents[i][k]
                    k += 1
                j = k + 1
                pages.append(int(num))
    return pages
           
