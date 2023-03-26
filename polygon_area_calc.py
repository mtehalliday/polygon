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
            return print("Too big for picture.")
        for i in range(self.height):
            star_pic += (self.width * "*"  + "\n")      
        return star_pic.rstrip()
            
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"



shape = Rectangle(3,5)
    
#print(shape.get_area())
print(shape.get_picture())

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
        
        