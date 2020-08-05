#!/usr/bin/python

import sys
from collections import namedtuple

"""
tips:
====
 maximizing the value of a  (we know this means unordered list with no duplicate items, max value with even size 
 thinking of the Roll Dice game, input is 
 
 hints from readme:
 1. Base cases you might want to consider for a naive recursive implementation of this problem are:
   * What if there are no items left to consider?
   so, if no items available to fill our bag, we can only have 0 items_to_select, 0 total_cost, 0 total_value
   
   * What if the item I'm considering is too large to fit in my bag's remaining capacity?
2. In order to move towards one of our base cases, we'll pick up an item from the pile to consider, and add it to a copy of our bag. Now we have two versions of our bag, one with the item we're considering, and one without. All we have to do now is pick the bag that yields us a higher value. 
3. As far as caching for this problem is concerned, a simple hash table or array is not going to suffice, because each solution now depends upon two parameters: the number of items in our pile to consider, as well as the capacity of our bag. So we'll need a 2x2 matrix in order to cache our answers adequately. 
4. Here's another way we might consider tackling this problem: what if we iterated through every single element in our pile and assign each one a value given by its value/weight ratio. Then we can sort all of the items based on this assigned value such that those items with a higher value/weight ratio are at the top of our sorted list of items. From there, we can just grab off the items at the top of our list until our bag is full. What would be the runtime complexity of this scheme? Would it work in every single scenario for any pile of items?

"""

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here
    # # starting simple base case of returning items, and their capacity
    # total_value = 0
    # total_cost = Item[value]
    # return items, capacity
    my_set = set(items[Item])

    print(my_set)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    # opening and reading file done for us already here above is open, below here is read and close

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')