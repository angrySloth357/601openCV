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

Each cvMat consists of planes of pixel values for Red, Green and Blue input channels. cvMat[0] consits of all the pixels corresponding to Red channel, cvMat[1] for Green channel and cvMat[2] for Blue channel.

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



