# Python
1. Go to https://www.python.org/downloads/release/python-385/ and download the Windows x86-64 executable installer
2. Run the installer and follow the on screen wizard
3. Make sure python is added to your environment variable
4. Run the following commands in a powershell or CMD
	a. pip install scikit-image
	b. pip install opencv-python
	c. pip install xlrd
	d. pip install xlwt
5. Download the code from https://
6. Copy app.py to where your input Excel file is located
7. Rename your input file to be input.xlsx
	a. Column A and Column B must contain path to the images which need to be compared
8. Start a powershell or CMD sesssion and change you working directory to where the script and input.xlsx is located. For example, if your files are in C:\Temp\Test\, you will need to change to this directory by running "cd C:\Temp\Test\"
9. Once you are in C:\Temp\Test\, execute python .\app.py
10. This will execute the application and the result will be generated in a new workbook with the name 'result.xls.
	a. If you need to run the app again, you need to ensure results.xls is closed. 
