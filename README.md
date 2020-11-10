Author: Diego Mendez

Requirements: Python3

NOTE: This document gives an overview of the project. For more info about each algorithm, go to each file. Each file has a more detailed 
      explanation of each algorithm and the thought process. 

This project implements three page replacement algorithms to simulate memory management for an operating system. 
The algorithms implemented are:
    1. Last In First Out
    2. Optimal Replacement Algorithm
    3. WSClock Page Replacement Algorithm (WSCRA)

The purpose of this project is to implement these algorithms and compare their efficiency. Their efficiency is measured by 
the number of page faults they return. The less the number of page faults, the more efficient is the algorithm. In this project
we're trying to minimize the number of page faults

This project contains 5 files:

    1. sequence.txt: this file contains our input with the given notation (Operation:page address). Ex: R:1 R:2 W:4 R:3 

    2. parse.py: this file contains a function called 'parse' that returns an array of the pages that we are going to use

    3. lifo.py: this file contains a function called 'lifo' that implements the Last In First Out Page Replacement Algorithm and returns the       
       number of page faults that have been encountered. This file takes in 3 arguments in the command line. Arguments are the python file,
       the number of physical memory pages, and our input file

    4. optimal.py: this file contains a function called 'optimal' that implements the Optimal Replacement Algorithm and returns the number of 
       of page faults that have been encountered. This file also takes in 3 arguments in the command line. Arguments are the python file,
       the number of physical memory pages, and our input file

    5. wsclock.py: this file contains a function called 'wscock' that implements the WSCRA and returns the number of page faults that have been 
       encountered. This file takes in 4 arguments in the command line. Arguments are the python file, number of physical memory pages, tau, and 
       our input file. 
  
  To run programs:

    1. lifo.py: 
        Standard: 
                python lifo.py <Number of physical memory pages> <access sequence file>
        Example:
                python lifo.py 10 sequence.txt

    2. optimal.py: 
        Standard:
               python optimal.py <Number of physical memory pages> <access sequence file>
        Example:
               python optimal.py 10 sequence.txt
    
    3. wsclock.py:
        Standard:
                python wsclock.py <Number of physical memory pages> <tau> <access sequence file>
        Example:
                python wsclock.py 10 5 sequence.txt
        

References:

    https://www.alltestanswers.com/python-program-that-implements-the-fifo-lru-and-optimal-page-replacement-algorithms/

    https://www.geeksforgeeks.org/program-page-replacement-algorithms-set-2-fifo/

    https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/

    https://www.youtube.com/watch?v=rmhZrLxYOCY&list=PL4KOaah3haN4qdmy6io1lW9RoQ6PFXNhh&index=6

    https://www.youtube.com/watch?v=KP8AmZU08nc&list=PL4KOaah3haN4qdmy6io1lW9RoQ6PFXNhh&index=7

    Book: Modern Operating Systems, 3/E by A. Tanenbaum
    
    Classmate: Daniel Suazo helped me understand the WSClock Page Replacement Algorithm

 