#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SupOpNumTools / Institut d'Optique

2D numerical functions

Created on 24/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""



def generate_sine(xx, yy, freq=1, alpha=0):
    return (1+np.sin(freq*(xx*np.sin(alpha)+yy*np.cos(alpha))))/2

def generate_square(xx, yy, freq=1, alpha=0):
    image = 255*(1+np.sin(freq*(xx*np.sin(alpha)+yy*np.cos(alpha))))/2
    th, im_th = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    print(th)
    return im_th