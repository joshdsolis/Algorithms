#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  final_list = [[] for n in 3**n]
  base_list = [['rock'],['paper'],['scissors']]
  def recurse(list, n):
    final_list = [[] for n in 3**n]
    for i in range(3**n):
      final_list[i] += list[i]
    return recurse(final_list, n)
  if n == 1:
    return base_list
  else:
    return recurse(base_list, n)


  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')