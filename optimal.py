# Diego Mendez
# 801-17-4052
import sys
from parse import parse

"""
NOTE: our memory array is our PHYSICAL MEMORY and each element would be a page number (int)
1. optimal: this function implements the optimal replacement page algorithm. Its arguments are:
   pages: this array will contain all of our pages. We get all of our pages using the parse function from parse.py,
   size: size of the memory array

   When encountered with a page fault, this algorithm tries to find the furthest page in the pages array and replace it with the 
   page that we want to insert. This algorithm is not applicable to the real world because an operating system cannot anticipate which 
   instructions are going to come in the near future. 
"""
def optimal(pages, size):
    memory = []
    faults = 0

    for i in range(0, len(pages)):
        page = pages[i]
        if len(memory) != size and page not in memory:
            memory.append(page)
            faults += 1
        else:
            if page not in memory:
                isSame = True
                memoryIndex = 0
                furthestIndex = -1

                # while the memory array stays the same, keep going
                # this outer loop would traverse the memory array
                while isSame and memoryIndex < len(memory):
                    elem = memory[memoryIndex]
                    notFound = True
                    j = i
                    # this inner loop checks for the farthest page in the pages array
                    while notFound and j < len(pages):
                        tempPage = pages[j]
                        if elem == tempPage:
                            tempIndex = j
                            furthestIndex = tempIndex if tempIndex > furthestIndex else furthestIndex
                            notFound = False
                        j += 1

                    if notFound:
                        memory[memoryIndex] = page
                        isSame = False
                        faults += 1
                    memoryIndex += 1

                if isSame:
                    val = pages[furthestIndex]
                    for i in range(0, len(memory)):
                        elem = memory[i]
                        if elem == val:
                            memory[i] = page
                            faults += 1

    return faults


def main():
    with open(sys.argv[2], 'r') as f:
        contents = f.readlines()
  
    pages = parse(contents)
    size = int(sys.argv[1])
    faults = optimal(pages, size)
    print(faults, "faults using optimal page replacement algorithm")


if __name__ == "__main__":
    main()