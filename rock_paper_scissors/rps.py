#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  base_list = ['rock','paper','scissors']
  final_list = []

  
  def recurse(n, list):
    if n == 0:
      final_list.append(list)
      return
    for i in base_list:
      recurse(n-1, list+[i])
  
  recurse(n, [])
  return final_list 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')