# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:20:51 2023

@author: ALPTUG
"""

def bmi():
    """
    this function calculates bmi
    input = weight, height
    output = bmi 
    """
    w = int(input("Please enter your weight as kilograms:"))
    h = float(input("Please enter your height as meters:"))
    cbmi = w / h ** 2
    if cbmi < 18.5:
        print("Your BMI is {}".format(cbmi))
        print("You are under your optimal weight.")
    if cbmi > 18.5 and cbmi < 24.9:
        print("Your BMI is {}".format(cbmi))
        print("You are on your optimal weight.")
    if cbmi > 24.9:
        print("Your BMI is {}".format(cbmi))
        print("You are overweight. Contact your doctor.")
        
