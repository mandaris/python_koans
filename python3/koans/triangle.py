#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    result = 'scalene' #default return
    
    if a == b: result = 'isosceles'
    
    if b == c: result = 'isosceles' 
    
    if a == c:
        result = 'isosceles'
        if a == b: result = 'equilateral'
    
    return result
    
    

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
