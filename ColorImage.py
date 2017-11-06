# Display all Colorspaces for an input image
# Run: python ColorImage.py <ImgSource>
import cv2
import numpy as np
import sys

def main():
	#Check if image source is provided
	if (len(sys.argv) < 2):
		print ("Please provide an input image!!")
		return
	cv2.namedWindow('Image', cv2.WINDOW_NORMAL) #open window
	source_img = cv2.imread(sys.argv[1]) # read image --> Default is BGR
	
	'''Original Image'''
	cv2.imshow('Original Image', source_img)
	cv2.waitKey(0)

	'''RBG'''
	cv2.imshow('Blue', source_img[:,:,0])
	cv2.imwrite('Blue.png', source_img[:,:,0])
	print ('Blue(20,25): ', source_img[20,25,0]);
	print ('Blue min: ', np.min(np.min(source_img[:,:,0])))
	print ('Blue max: ', np.max(np.max(source_img[:,:,0])))
	cv2.waitKey(0)

	cv2.imshow('Green', source_img[:,:,1])
	cv2.imwrite('Green.png', source_img[:,:,1])
	print ('Green(20,25): ', source_img[20,25,1]);
	print ('Green min: ', np.min(np.min(source_img[:,:,1])))
	print ('Green max: ', np.max(np.max(source_img[:,:,1])))
	cv2.waitKey(0)
	
	cv2.imshow('Red', source_img[:,:,2])
	cv2.imwrite('Red.png', source_img[:,:,2])
	print ('Red(20,25): ', source_img[20,25,2]);
	print ('Red min: ', np.min(np.min(source_img[:,:,2])))
	print ('Red max: ', np.max(np.max(source_img[:,:,2])))
	cv2.waitKey(0)

	'''YCrCb'''
	y_img = cv2.cvtColor(source_img, cv2.COLOR_BGR2YCrCb)
	cv2.imshow('Y', y_img[:,:,0])
	cv2.imwrite('Y.png', y_img[:,:,0])
	print ('Y(20,25): ', y_img[20,25,0]);
	print ('Y min: ', np.min(np.min(y_img[:,:,0])))
	print ('Y max: ', np.max(np.max(y_img[:,:,0])))
	cv2.waitKey(0)

	cv2.imshow('Cb', y_img[:,:,1])
	cv2.imwrite('Cb.png', y_img[:,:,1])
	print ('Cb(20,25): ', y_img[20,25,1]);
	print ('Cb min: ', np.min(np.min(y_img[:,:,1])))
	print ('Cb max: ', np.max(np.max(y_img[:,:,1])))
	cv2.waitKey(0)

	cv2.imshow('Cr', y_img[:,:,2])
	cv2.imwrite('Cr.png', y_img[:,:,2])
	print ('Cr(20,25): ', y_img[20,25,2]);
	print ('Cr min: ', np.min(np.min(y_img[:,:,2])))
	print ('Cr max: ', np.max(np.max(y_img[:,:,2])))
	cv2.waitKey(0)

	'''HSV'''
	h_img = cv2.cvtColor(source_img, cv2.COLOR_BGR2HSV)
	
	cv2.imshow('Hue', h_img[:,:,0])
	cv2.imshow('Hue', h_img[:,:,0])
	cv2.imwrite('Hue.png', h_img[:,:,0])
	print ('Hue(20,25): ', h_img[20,25,0]);
	print ('Hue min: ', np.min(np.min(h_img[:,:,0])))
	print ('Hue max: ', np.max(np.max(h_img[:,:,0])))
	cv2.waitKey(0)

	cv2.imshow('Saturation', h_img[:,:,1])
	cv2.imshow('Saturation', h_img[:,:,1])
	cv2.imwrite('Saturation.png', h_img[:,:,1])
	print ('Saturation(20,25): ', h_img[20,25,1]);
	print ('Saturation min: ', np.min(np.min(h_img[:,:,1])))
	print ('Saturation max: ', np.max(np.max(h_img[:,:,1])))
	cv2.waitKey(0)

	cv2.imshow('Value', h_img[:,:,2])
	cv2.imshow('Value', h_img[:,:,2])
	cv2.imwrite('Value.png', h_img[:,:,2])
	print ('Value(20,25): ', h_img[20,25,2]);
	print ('Value min: ', np.min(np.min(h_img[:,:,2])))
	print ('Value max: ', np.max(np.max(h_img[:,:,2])))
	cv2.waitKey(0)


	cv2.destroyAllWindows()

if __name__ == "__main__":
    main()	
