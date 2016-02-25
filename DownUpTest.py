# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 17:13:12 2015

@author: Navegantes
"""

import cv2
import JPEGcodec as jpg
#import numpy as np

filename = '../imgtst/flyingfish.jpg'
img = cv2.imread(filename,1)
#ymg = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
qually = 95

enc = jpg.Encoder(filename, qually, '420')
print '- Outcomes'
enc.Outcomes()

#POSSIVEL IMPLEMENTAR LEITURA DE ARQUIVO
#huffile = enc.filename.split('/')[-1:][0].split('.')[0] + '.huff'
#
#dec = jpg.Decoder(huffile)
#imrec = dec._run_()
#
#cv2.imshow('Original', img)
#cv2.imshow('Recuperada', imrec)
#cv2.imshow('Diferença', img-imrec)
#
#print '\n- Press <ESC> to close...'
#k = cv2.waitKey(0)    
#if k == 27:                # wait for ESC key to exit
#    cv2.destroyAllWindows()
##        
        
        
        
        
        
        
        
        
