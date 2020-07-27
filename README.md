Objective
=========
Objective of this tool is to automate the image comparison which is currently being done by collegues.
My first goal was to research and select a language which had existing libraries/modules that handled the complexity of comparing two images perceptually, not with binary data of the images. Looking at existing resources, the closest solution was SSIM(Structral Similarity Index) for comparing images. Hence, this tool is written based on the SSIM method. 
Second goal was to select a language which is easy to install by end user and does not require a big amount of effort by user to prepare their mahcine to run the code.

Image Compare
=============
A command line tool that compares two images and score them based on SSIM. It will read the path to two images from an Excel workbook and it will compare every two image from each row of workbook until it reaches the end and there are not more rows.


Installation
------------
This tool is developed and tested with Python 3.8.5. I recommend using this version as some modules may not work with other versions of Python
Install following libraries:
1. pip install scikit-image
2. pip install opencv-python
3. pip install xlrd
4. pip install xlwt

Usage
-----
You will need an input file 'input.xlsx' where the tool reads paths to images from this file
Run 'Python app-0.0.1.py' in your powershell or CMD

Input example
-------------
|image1|image2|
|---|---|
|aa.png|ba.png|
|ab.png|bb.png|
|ad.png|bd.png|

Output example
--------------
|image1|image2|similar|elapesd|
|---|---|---|---|
|aa.png|ba.png|0|0.006|
|ab.png|bb.png|0.23|0.843|
|ad.png|bd.png|0|1.43|
