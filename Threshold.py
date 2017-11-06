# Display all Colorspaces for an input image
# Run: python Noise.py <ImgSource>

import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

def main():
    #Check if image source is provided
    if (len(sys.argv) < 2):
        print ("Please provide an input image!!")
        return
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL) #open window
    img = cv2.imread(sys.argv[1]) # read image 
    
    '''Original Image'''
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold_type = 2
    threshold_value = 128
    _,dst = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_TRUNC)
    cv2.imshow("Thresholded Image",dst)
    cv2.imwrite('./Run_Images/th.png', dst)
    cv2.waitKey(0)

    current_threshold = 128
    max_threshold = 255
    _,threshold = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY)
    cv2.imshow("Binary threshold",threshold)
    cv2.imwrite('./Run_Images/bin_th.png', threshold)
    cv2.waitKey(0)

    threshold1 = 27
    threshold2 = 125
    _, binary_image1 = cv2.threshold(gray, threshold1, max_threshold, cv2.THRESH_BINARY)
    _, binary_image2 = cv2.threshold(gray, threshold2, max_threshold, cv2.THRESH_BINARY_INV)
    band_thresholded_image = np.bitwise_and(binary_image1, binary_image2)
    cv2.imshow("Band Thresholding", band_thresholded_image)
    cv2.imwrite('./Run_Images/band_th.png', band_thresholded_image)
    cv2.waitKey(0)

    _,semi_thresholded_image = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    semi_thresholded_image = np.bitwise_and( gray, semi_thresholded_image)
    cv2.imshow("Semi Thresholding",semi_thresholded_image )
    cv2.imwrite('./Run_Images/semi_th.png',semi_thresholded_image)
    cv2.waitKey(0)

    adaptive_thresh = cv2.adaptiveThreshold(gray, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10 )
    cv2.imshow("Adaptive Thresholding",adaptive_thresh)
    cv2.imwrite('./Run_Images/adap_th.png', adaptive_thresh)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()  