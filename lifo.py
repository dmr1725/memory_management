# Diego Mendez
# 801-17-4052
import sys
from parse import parse
"""
NOTE: our memory array is our PHYSICAL MEMORY and each element would be a page number (int)
1. lifo: function that implements the Last In First Out page replacement algorithm and returs the page faults we've encountered. Its arguments are:
   pages: this array will contain all of our pages. We get all of our pages using the parse function from parse.py,
   size: size of the memory array
"""
def lifo(pages, size):
    faults = 0
    memory = []

    for page in pages:
        if len(memory) != size:
            # page fault
            if page not in memory:
                memory.append(page)
                faults += 1
        else:
            # page fault
            if page not in memory:
                memory.pop()
                memory.append(page)
                faults += 1
    return faults


def main():
    with open(sys.argv[2], 'r') as f:
        contents = f.readlines()
    
    pages = parse(contents)   
    size = int(sys.argv[1])
    faults = lifo(pages, size)
    print(faults, "faults using lifo page replacement algorithm")


if __name__ == "__main__":
    main()
