# Version 0.0.1
# Usage:
# This app will use SSIM method to compare two images and score their differences
# It will read path of two images from column A and column B of an Excel workbook on the same row and it will output the results on a new Excel workbook
# Please refere to UserGuide.txt for informtaion on how to use it

# 1. Import the necessary packages
from skimage.measure import compare_ssim
import cv2
import time
import xlrd
import xlwt 
from xlwt import Workbook 
  
# Create a workbook so that we can write the output in this workbokk 
wbr = Workbook() 
  
# Add a worksheet with name 'Sheet1' where the results will be written 
sheet1 = wbr.add_sheet('Sheet 1') 
# Add headers to columns that reperesents each field
sheet1.write(0, 0, 'image1') 
sheet1.write(0, 1, 'image2') 
sheet1.write(0, 2, 'similar') 
sheet1.write(0, 3, 'Elapsed') 
# Save the workbokk
wbr.save('results.xls')  
 

# This function handles the image processing. More information is available inline
def imageProcesssor(img1,img2,counter):
    # img1 contains the path to where the left image is stored
    # Read the first image and store it in imageA    
    imageA = cv2.imread(img1)
    
    iax = ''
    iay = ''
    
    # img1 contains the path to where the right image is stored
    # Read the second image and store it in imageB
    imageB = cv2.imread(img2)

    # Check if imageA exist
    # If not, out put the result and do not continue the iterration. Otherwise, write the image path and continue
    if imageA is None:
        writeResults("Image Not Found",0,counter)
        writeResults("N/A",2,counter)
        writeResults("N/A",3,counter)
        return
    else:
        writeResults(img1,0,counter)
        # Get height and width of left image
        iax = imageA.shape[0]
        iay = imageA.shape[1]
    
    # Check if imageA exist
    # If not, out put the result and do not continue the iterration. Otherwise, write the image path and continue
    if imageB is None:
        writeResults("Image Not Found",1,counter)
        writeResults("N/A",2,counter)
        writeResults("N/A",3,counter)
        return
    else:
        writeResults(img2,1,counter)

    # Set height and width of right image to be the same as left image. This is necessary for comparison of the two image
    imageB=cv2.resize(imageB,(iay,iax))

    # Convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # Compute the Structural Similarity Index (SSIM) between the two
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    tmpRes = score - 1
    res = 0
    # Reverse the result where 0 exact same image and 1 is completely different image
    if tmpRes < 0:
        res = tmpRes * -1
    else:
        res = tmpRes

    # You can print only the score for troubleshooting
    #print("SSIM: {}".format(res))
    end = time.time()
    elapsed = end - start
    # You can print time elapsed for troubleshooting
    # print(end - start)
    writeResults(res,2,counter)
    writeResults(elapsed,3,counter)

     
# This function writes the data into spreadsheet    
def writeResults(img, col, row):
    try:
        sheet1.write(row, col, img)
    except:
        sheet1._cell_overwrite_ok=True
        sheet1.write(row, col, img)
        sheet1._cell_overwrite_ok = False
    wbr.save('results.xls')

# Read the input file
Input = ("input.xlsx")
wb = xlrd.open_workbook(Input) 
sheet = wb.sheet_by_index(0)
start = ""
# Get total number of rows in input document
count = sheet.nrows
for i in range(1,count):
    start = time.time()
    imageA=""
    imageB=""
    #print(sheet.cell_value(i, 0))
    #print(sheet.cell_value(i, 1))
    imageA = sheet.cell_value(i, 0)
    imageB = sheet.cell_value(i, 1)
    imageProcesssor(imageA,imageB,i)
    # Print how many rows have been completed
    print(i," out of ",count-1," completed")

# save the workbook at the end
wbr.save('results.xls')

print("To get latest version with updates and improvements, checkout https://github.com/mohammad-aryafar/Python")
