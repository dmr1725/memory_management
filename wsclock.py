# Diego Mendez
# 801-17-4052
import sys
from parse import parse

"""
NOTE: our memory array represents the PHYSICAL MEMORY and is a circular list. Each element in the array will be a dictionary object.
      the dictionary properties of each element in the array are the following: page, reference and tolu.
      page: the page that is stored
      reference: the reference bit (True or False)
      tolu: time of last use of that page (clock)
 Ex:
     memory = [{'page': 1, 'reference': True, 'tolu': 0}]

Explanation of our 5 functions:
      
1. wsclock: this is the function that runs the wsClock algorithm and returns our faults. Important variables created in this function are
   clock, tick, memory array and faults. The functions arguments are:
   pages: this array will contain all of our pages. We get all of our pages using the parse function from parse.py,
   size: size of the memory array taken from input
   tau: fixed variable from input (will be used to check if our page is in the working set function later)

2. pageFaultTraverseClock: helper method for the wsClock function. This function returns an array. That array will contain our 
   updated memory array, tick, clock and faults. Basically this function has the core logic of the wsClock algorithm when a page fault occurs
   Its arguments are memory, page, tick, clock, size, tau, faults
   memory: this is the physical memory
   page: the page we want to insert in our physical memory
   tick: a pointer that works as our clock hand
   clock: our current virtual time
   size: size of the physical memory
   tau: fixed variable from input (will be used to check if our page is in the working set function later)
   faults: total number of page faults
   NOTE: little more detail of the thought process of this function is explained in the function (line 79)

3. getMinClockValueIndex: this function returns the index of the page with the smallest clock or 'tolu'. Its argument is the memory array

4. checkWorkingSet: this function returns a boolean value. This function checks if our current page is in the working set. 
   Its arguments are memory, tick, clock and tau

5. pageInMemory: this function also returns an array that contains a boolean value and an integer. Its purpose is to see if a given page 
   is in memory and if that page is found, return the index. Its arguments are memory and page. I needed to create this method because 
   we are looping through a dictionary
"""

def wsclock(pages, size, tau):
    memory = []
    clock = 0 # current virtual time
    tick = 0 # pointer
    faults = 0


    for page in pages:
        results = pageInMemory(memory, page)
        inMemory = results[0]
        indexOfPage = results[1]
        # page fault
        if len(memory) != size and not inMemory:
            memory.append({'page': page, 'reference': True, 'tolu': clock})
            clock += 1
            tick += 1
            faults += 1
        else:
            # page fault
            if not inMemory:
                results = pageFaultTraverseClock(memory, page, tick, clock, size, tau, faults)
                memory = results[0]
                tick = results[1]
                clock = results[2]
                faults = results[3]
            # page hit, tick doesn't update
            else:
                memory[indexOfPage]['reference'] = 1
                memory[indexOfPage]['tolu'] = clock
                clock += 1

    return faults


def pageFaultTraverseClock(memory, page, tick, clock, size, tau, faults):
    """
    isSame: True if the memory array stays the same after our loop. False if our memory array changes after our loop
    allNotReferenced: True if all the pages are referenced. False if one of the pages is not referenced
    inWorkingSet: False if our page is not in our working set. True if our page is in our working set
    minClockValueIndex: has the index of our page with our smallest 'tolu' 

    pageFaultTraverseClock(memory, page, tick, clock, size, tau, faults) -> [memory, tick, clock, faults]
    """
    isSame = True 
    inWorkingSet = False
    allNotReferenced = True
    minClockValueIndex = getMinClockValueIndex(memory)
    i = 0

    while isSame and i < size:
        # circular list: if our tick == size, we do modulo so tick be equal to 0
        tick = size % size if size== tick else tick 

        if memory[tick]['reference'] == 1:
            memory[tick]['reference'] = 0
            clock += 1
            tick += 1

        elif memory[tick]['reference'] == 0:
            allNotReferenced = False
            inWorkingSet = checkWorkingSet(memory, tick, clock, tau)
            if inWorkingSet:
                clock += 1
                tick += 1
            else:
                memory[tick]['page'] = page
                memory[tick]['tolu'] = clock
                memory[tick]['reference'] = 1
                isSame = False
                faults += 1
                clock += 1
                tick += 1
        i += 1

    # if the memory array isSame and all pages are not referenced and all of our pages are not in the working set after the loop,
    # then we replace the page that we want to insert with the page with the smallest clock value ('tolu')
    if allNotReferenced and inWorkingSet == False and isSame:
        memory[minClockValueIndex]['page'] = page
        memory[minClockValueIndex]['tolu'] = clock
        memory[minClockValueIndex]['reference'] = 1
        tick = minClockValueIndex + 1
        tick = size % size if size== tick else tick
        faults += 1
        clock += 1


    return [memory, tick, clock, faults]



def getMinClockValueIndex(memory):
    minValue = float('inf')
    index = 0

    for i in range(len(memory)):
        if memory[i]['tolu'] < minValue:
            minValue = memory[i]['tolu']
            index = i
    return index


def checkWorkingSet(memory, tick, clock, tau):
    return clock - memory[tick]['tolu'] <= tau


def pageInMemory(memory, page):
    inMemory = False
    index = -1
    i = 0
    while i < len(memory) and inMemory == False:
        if memory[i]['page'] == page:
            inMemory = True
            index = i
        i += 1
    return [inMemory, index]




def main():
    with open(sys.argv[3], 'r') as f:
        contents = f.readlines()
    
    pages = parse(contents)   
    size = int(sys.argv[1])
    tau = int(sys.argv[2])
    faults = wsclock(pages, size, tau)
    print(faults, "faults using the working set clock page replacement algorithm")

    
if __name__ == "__main__":
    main()