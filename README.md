# 601openCV

## Compile & Run Instructions:
1. Run **make** for compiling all .cpp files

2. Run **./objSource** for running each file

3. Run **make clean** for removing all object files


Corresponding binaries are:

ColorImage.cpp ---> colorimg 

Noise.cpp ---> noise	

Threshold.cpp ---> threshold

## Exercise 1

Each cvMat consists of planes (2D matrix) of pixel values difference colorSpaces like BGR, YCbCr, HSV, etc. Pixel values correspods to brighness where 0 pixel value is the darkest [black] and 255 pixel value is the lightest [white]. 

## Exercise 2

### Part 1
**./colorimg imageSource**: Output shows that each colorspace output: Red, Blue, Green, etc. is only a grayscale pixel value and have to be combined together if you need actual colors. 

**python ColorImage.py Test_images/baboon.jpg**

| Blue 				| Green 			  	| Red 				|
|:-----------------:|:---------------------:|:-----------------:|
| ![blue](/Run_Images/Blue.png) | ![green](/Run_Images/Green.png) 	| ![red](/Run_Images/Red.png) 	|

| Y 				| Cb 			  		| Cr 				|
|:-----------------:|:---------------------:|:-----------------:|
| ![y](/Run_Images/Y.png) 		| ![cb](/Run_Images/Cb.png) 		| ![cr](/Run_Images/Cr.png) 	|

| Hue 				| Saturation 			| Value 			|
|:-----------------:|:---------------------:|:-----------------:|
| ![hue](/Run_Images/Hue.png) | ![sat](/Run_Images/Saturation.png)  | ![val](/Run_Images/Value.png) |

### Part 2

Values for: **python ColorImage.py Test_images/baboon.jpg** 

| ColorSpace 	| (20,25) 	| min 	| max 	|
|:-------------:|:---------:|:-----:|:-----:|
| Blue 			| 102 		| 0 	| 255	|
| Green 		| 165 		| 0		| 234	|
| Red 			| 156		| 0		| 255   |
| Y 			| 155		| 1 	| 224	|
| Cb 			| 129 		| 70 	| 230	|
| Cr 			| 98 		| 35 	| 185	|
| Hue 			| 34 		| 0 	| 179	|
| Saturation 	| 97 		| 0 	| 255	|
| Value 		| 165		| 4 	| 255	|

## Exercise 3

### Part 1

Mean squared deviation from the original image based on various Gaussian and Salt and Pepper noise addition is given below:

| Model 	| Mean 	| Sigma	| Mean Squared Error|
|:---------:|:-----:|:-----:|:-----------------:|
| Gaussian 	| 0 	| 0 	| 0.000000 			|
| Gaussian 	| 5 	| 20 	| 54.798973 		|
| Gaussian  | 10 	| 50 	| 61.844326 		|
| Gaussian  | 20 	| 100 	| 61.447723 		|

| Model 		| pa 	| pb 	| Mean Squared Error|
|:-------------:|:-----:|:-----:|:-----------------:|
| Salt & Pepper | 0.01 	| 0.01 	| 2.052879 			|
| Salt & Pepper | 0.02 	| 0.02 	| 4.013709 			|
| Salt & Pepper | 0.03 	| 0.03 	| 5.801343 			|
| Salt & Pepper | 0.04 	| 0.04 	| 7.738173 			|


### Part 2

Mean squared deviation from the original image based on various noise addtion and filtering mechanism is given below:

**For Gaussian noise with mean=0, sigma=50**

| Filter 			| Kernel	| Mean Squared Error	|
|:-----------------:|:---------:|:---------------------:|
| Box Filter 		| (3, 3) 	| 70.988484 			|
| Gaussian Filter 	| (3, 3) 	| 69.625936 			|
| Median Filter 	| (3, 3) 	| 64.128119 			|
| Box Filter 		| (5, 5) 	| 78.017225 			|
| Gaussian Filter 	| (5, 5) 	| 76.464632 			|
| Median Filter 	| (5, 5) 	| 63.686953 			|
| Box Filter 		| (7, 7) 	| 80.924800 			|
| Gaussian Filter 	| (7, 7) 	| 73.235832 			|
| Median Filter 	| (7, 7) 	| 63.640454 			|

Median Filter seems to perform the best for Gaussian noise. Smaller kernel gives lower error.

**For Salt & Pepper noise with pa=0.01, pb=0.01**

| Filter 			| Kernel	 | Mean Squared Error	|
|:-----------------:|:----------:|:--------------------:|
| Box Filter 		| (3, 3) 	 | 71.370607 			|
| Gaussian Filter 	| (3, 3) 	 | 69.663289 			|
| Median Filter 	| (3, 3) 	 | 56.583368 			|
| Box Filter 		| (5, 5) 	 | 77.364820 			|
| Gaussian Filter 	| (5, 5) 	 | 74.038914 			|
| Median Filter 	| (5, 5) 	 | 56.578864 			|
| Box Filter 		| (7, 7) 	 | 80.537738 			|
| Gaussian Filter 	| (7, 7) 	 | 79.036938 			|
| Median Filter 	| (7, 7) 	 | 56.754785 			|

Once again Median Filter seems to perform the best for Salt and Pepper noise as well. Smaller kernel gives lower error.

## Exercise 4

### Part 1

**python Threshold.py Test_images/baboon.jpg**

| Original 			| Threshold 			| Binary Threshold 	|
|:-----------------:|:---------------------:|:-----------------:|
| ![blue](/Test_images/baboon.jpg ) | ![green](/Run_Images/th.png) 	| ![red](/Run_Images/bin_th.png) 	|

| Band Threshold 	| Semi Threshold 		| Adaptive Threshold |
|:-----------------:|:---------------------:|:------------------:|
| ![y](/Run_Images/band_th.png) | ![cb](/Run_Images/semi_th.png) | ![cr](/Run_Images/adap_th.png) |

Adaptive Thresholding seems to give the most accurate representation of the original image :)

### Part 2

Binary Thresholding looks like the runner up for the most accurate representation of the accurate image. However, unlike adaptive thresholding it cannot capture subtle changes in pixel values near the eye region of the sample image.


### Part 3

Adaptive Thresholding is useful where there are only slight variation of pixel values for some regions which an ordinary thresholding algorithm cannot capture.
