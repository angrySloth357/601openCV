# Noise stuff
# Run: python Noise.py <ImgSource>

import cv2
import numpy as np
import sys


def add_gaussian_noise(matrix, mean, sigma):
    noise = np.copy(matrix)
    noise = cv2.randn(noise, mean,sigma);
    noise = cv2.add(noise, matrix)
    return noise


def add_salt_and_pepper_noise(mat, pa, pb):
    matrix = np.copy(mat)
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    
    '''Add black spots'''
    pa_count = int(rows*cols*pa)
    pa_rows = np.random.choice(rows, pa_count)
    pa_cols = np.random.choice(cols, pa_count)
    matrix[pa_rows, pa_cols] = 0

    '''Add white spots'''
    pb_count = int(rows*cols*pb)
    pb_rows = np.random.choice(rows, pb_count)
    pb_cols = np.random.choice(cols, pb_count)
    matrix[pb_rows, pb_cols] = 255
    return matrix
    
'''Filter out the added noise'''
def apply_noise_filters(noise_matrix, kernel):
    blur = cv2.blur(noise_matrix,kernel);
    cv2.imshow( "Box filter", blur);
    cv2.waitKey(0);
    blur = cv2.GaussianBlur(noise_matrix,kernel,1.5)
    cv2.imshow( "Gaussian filter", blur);
    cv2. waitKey(0);
    blur = cv2.medianBlur(noise_matrix,3);
    cv2.imshow( "Median filter", blur);
    cv2.waitKey(0); 
    cv2.destroyAllWindows()

#Return the mean squared error between 2 images
def calculate_mse(matrix, noise_matrix):
    return np.square(matrix - noise_matrix).mean()

def find_error(matrix, noise_type, mean=0, sigma=0, pa=0, pb=0):
    if noise_type=='gaussian':
        noisy = add_gaussian_noise(matrix, mean=mean, sigma=sigma)
        mse = calculate_mse(matrix, noisy)
        print ('| Gaussian | %d \t | %d \t | %f \t|' %(mean,sigma, mse)) 
    elif noise_type == 'sp':
        noisy = add_salt_and_pepper_noise(matrix, pa=pa, pb=pb)
        mse = calculate_mse(matrix, noisy)
        print ('| Salt & Pepper | %.2f \t | %.2f \t | %f \t|' %(pa,pb, mse))     

def eval_filter_performance(matrix, kernel, noise_type):
    if noise_type == 'gaussian':
        mean = 0
        sigma = 10
        noisy = add_gaussian_noise(matrix, mean=mean, sigma=sigma)
        blur = cv2.blur(noisy,kernel);
        mse = calculate_mse(matrix, blur)
        print ('| Box Filter | (%d, %d) \t | %f \t|' %(kernel[0],kernel[1], mse)) 
        blur = cv2.GaussianBlur(noisy,kernel,1.5)
        mse = calculate_mse(matrix, blur)
        print ('| Gaussian Filter | (%d, %d) \t | %f \t|' %(kernel[0],kernel[1], mse))
        blur = cv2.medianBlur(noisy,3);
        mse = calculate_mse(matrix, blur)
        print ('| Median Filter | (%d, %d) \t | %f \t|' %(kernel[0],kernel[1], mse))
    elif noise_type=='sp':
        pa = 0.01
        pb = 0.01
        noisy = add_salt_and_pepper_noise(matrix, pa=pa, pb=pb)
        blur = cv2.blur(noisy,kernel);
        mse = calculate_mse(matrix, blur)
        print ('| Box Filter | (%d, %d) \t | %f \t|' %(kernel[0],kernel[1], mse)) 
        blur = cv2.GaussianBlur(noisy,kernel,1.5)
        mse = calculate_mse(matrix, blur)
        print ('| Gaussian Filter | (%d, %d) \t | %f \t|' %(kernel[0],kernel[1], mse))
        blur = cv2.medianBlur(noisy,3);
        mse = calculate_mse(matrix, blur)
        print ('| Median Filter | (%d, %d) \t | %f \t|' %(kernel[0],kernel[1], mse))   

def main():
    #Check if image source is provided
    if (len(sys.argv) < 2):
        print ("Please provide an input image!!")
        return
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL) #open window
    source_img = cv2.imread(sys.argv[1], 0) # read image as grayscale
    
    '''Original Image'''
    cv2.imshow('Original Image', source_img)
    cv2.waitKey(0)

    '''Add and filter Gaussian Noise'''
    noisy_gaussian = add_gaussian_noise(source_img, mean=0, sigma=50)
    cv2.imshow("Gaussian Noise", noisy_gaussian)    
    cv2.waitKey(0)
    apply_noise_filters(noisy_gaussian, kernel=(3,3))

    '''Add and filter Salt and Pepper Noise'''
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL) #open window
    noisy_sp = add_salt_and_pepper_noise(source_img, pa=0.01, pb=0.01)
    cv2.imshow("Salt and Pepper Noise", noisy_sp)    
    cv2.waitKey(0)
    apply_noise_filters(noisy_sp, kernel=(3,3))

    '''Start Mean Square error calculations'''
    print ('| Model | Mean | Sigma | Mean Squared Error |')
    find_error(source_img, 'gaussian', mean=0, sigma=0)
    find_error(source_img, 'gaussian', mean=5, sigma=20)
    find_error(source_img, 'gaussian', mean=10, sigma=50)
    find_error(source_img, 'gaussian', mean=20, sigma=100)

    print ('\n| Model | pa | pb | Mean Squared Error |')
    find_error(source_img, 'sp', pa=0.01, pb=0.01)
    find_error(source_img, 'sp', pa=0.02, pb=0.02)
    find_error(source_img, 'sp', pa=0.03, pb=0.03)
    find_error(source_img, 'sp', pa=0.04, pb=0.04)

    '''PART 2: Find which filtering mechanism works best'''
    print('\n\nFor Gaussian noise with mean: 0, sigma: 10 =>\n')
    print ('| Filter | Kernel | Mean Squared Error |')
    eval_filter_performance(source_img, (3,3), 'gaussian')
    eval_filter_performance(source_img, (5,5), 'gaussian')
    eval_filter_performance(source_img, (7,7), 'gaussian')

    print('\n\nFor Salt & Pepper noise with pa: 0.01, pb: 0.01 =>\n')
    print ('| Filter | Kernel | Mean Squared Error |')
    eval_filter_performance(source_img, (3,3), 'sp')
    eval_filter_performance(source_img, (5,5), 'sp')
    eval_filter_performance(source_img, (7,7), 'sp')

if __name__ == "__main__":
    main()  