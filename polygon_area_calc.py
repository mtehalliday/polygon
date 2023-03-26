#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 16:05:17 2023

@author: matthewhalliday
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, new_width):
        self.width = new_width
        
    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (2 * self.height + 2 * self.width)
    
    def get_diagonal(self):
        return (self.height**2 + self.width**2)**0.5
    
    def get_picture(self):
        star_pic = ""
        if self.height > 50 or self.width > 50: 
            string = "Too big for picture."
            return string
        for i in range(self.height):
            star_pic += (self.width * "*"  + "\n")      
        return star_pic
            
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def get_amount_inside(self, given_quad):
        count = 0
        if given_quad.width > self.width or given_quad.height > self.height:
            return count
        fit_width = self.width // given_quad.width
        fit_height = self.height // given_quad.height
        count = fit_height * fit_width
        return count
    
    
class Square(Rectangle):    
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length
    
    def set_side(self, new_side_length):
        self.width = new_side_length
        self.height = new_side_length

    def set_width(self, new_side_length):
        self.set_side(new_side_length)

    def set_height(self, new_side_length):
        self.set_side(new_side_length)       
    def __str__(self):
        return f"Square(side={self.width})"
    
rect = Rectangle(10, 5)
rect.set_width(7)
rect.set_height(3)
actual = rect.get_picture()
expected = "*******\n*******\n*******\n"

print(actual)
print()
print(expected)
#unittest.assertEqual(actual, expected, 'Expected message: "Too big for picture."')   
print("length of actual: " + str(len(expected)))
print("length of expected: " + str(len(expected)))

"""
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
"""
"""
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
"""
"""
sq = Square(5)

shape = Rectangle(5,10)
    
#print(shape.get_area())
#print(shape.get_picture())


#print(rect.get_picture())
print("amount inside: " + str(shape.get_amount_inside(sq)))
 """       