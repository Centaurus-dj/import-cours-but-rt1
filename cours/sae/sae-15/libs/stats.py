#!/usr/bin/env python3
#coding=utf8

### This library was made during for an SAE (SAE-15)
### It simply contains three functions:
###
### - moyenne(): calculates the mean of a list of integers / float
### - sigma(): calculates the sigma of a list of integers / float
### - plot(): creates a graphical representation of data given in a list of integers / float

import math as m
import matplotlib.pyplot as plt

def moyenne(_list: list):
  nbr = len(_list)
  _sum = 0
  for i in range(0, len(_list)):
    if isinstance(_list[i], (int, float)):
      _sum += _list[i]

  return _sum / nbr

def sigma(_list: list):
  ### 1/n∑(xi − moy(x))**2
  nbr = len(_list)
  _moyenne = moyenne(_list)
  _sum = 0

  for i in range(0, len(_list)):
    if isinstance(_list[i], (int, float)):
      _sum += (_list[i] - _moyenne)**2

  _sigma = m.sqrt((1/nbr) * _sum)

  return _sigma

def plot(_ylist: list, _xlist: list):
  """
  _ylist <list>: The list used on the Y axis of the plot
  _xlist <list>: The list used on the X axis of the plot
  """
  fig, ax = plt.subplot()
  ax.plot(_ylist, _xlist)