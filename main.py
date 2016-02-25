# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:07:35 2015

@author: Navegantes
"""

#from matplotlib import pyplot as plt
#import numpy as np
#import HuffCoder as hf
import cv2
import JPEGcodec as jpg
from Tkinter import Tk
from tkFileDialog import askopenfilename

root = Tk()
root.withdraw()


if __name__ == '__main__':
    
    filepath = askopenfilename(parent=root, title="Choose your destiny!").__str__()
#    filepath = '../imgtst/jaca.jpg'
    img = cv2.imread(filepath,1)
    qually = 50
    mode = '420'
    
    print '\n***********************'
    print '* Encoder Initialized *'
    print '***********************'
    
    enc = jpg.Encoder(filepath, qually, mode)
    print '- Outcomes'
    enc.Outcomes()
    
    print '\n***********************'
    print '* Decoder Initialized *'
    print '***********************'
    
    huffile = 'output/' + enc.filepath.split('/')[-1:][0].split('.')[0] + '.huff'
    dec = jpg.Decoder(huffile)
    imrec = dec._run_()
    
    cv2.imshow('Imagem Original', img)
    cv2.imshow('Imagem Recuperada', imrec)
    
    luma1 = cv2.cvtColor(img, cv2.COLOR_YCR_CB2BGR)
    luma2 = cv2.cvtColor(imrec, cv2.COLOR_YCR_CB2BGR)
    imdif = (luma1[:,:,0]-luma2[:,:,0]) + 128
    cv2.imshow('Diferenca Luma', imdif)
				
    cv2.imshow('Diferenca', img-imrec)
    
    print '\n- Press <ESC> to close...'
    k = cv2.waitKey(0)    
    if k == 27:                # wait for ESC key to exit
        cv2.destroyAllWindows()
    
#plt.imshow(np.uint8(luma1[:,:,0]-luma2[:,:,0]), 'gray')
    
    
    
    
    
    
    
    

    