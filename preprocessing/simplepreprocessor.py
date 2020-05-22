# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:40:15 2020

@author: KSEKAR
"""

# Import necessary packages
import cv2

class SimplePreprocessor:
    def __init__(self,width,height,inter=cv2.INTER_AREA):
        # store the target image width,height and interpolation
        # inter -- Interpolation algo used for resizing
        self.width = width
        self.height = height
        self.inter = inter
        
    def preprocess(self,image):
        # reszie the image to a fixed size ignoring the aspect ratio
        return cv2.resize(image,(self.width,self.height),
                          interpolation=self.inter)