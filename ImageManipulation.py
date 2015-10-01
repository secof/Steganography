#!/usr/bin/env python
import os
import binascii
from PIL import Image

def asciiToBinary(textData):
	#binaryData = bin(int(binascii.hexlify(textData), 16))
	binaryData = ''.join(format(letter,'b').zfill(8) for letter in bytearray(textData))
	return binaryData

def binaryToAscii(binaryData):
	tempData = int(binaryData, 2)
	stringData = binascii.unhexlify('%x' % tempData)
	return stringData

def decimalToBinary(decimal):
	binaryValue = bin(decimal)[2:].zfill(8)
	return binaryValue

def fileToBinary(file):
	binaryDataList = []
	binaryBitsList = []
	binaryDataString = ""

	#Open the file and conver the data to bytes
	with open(file, "rb") as f:
		bytes = bytearray(f.read())

	#For each byte, convert it to binary and concatenate it to a string variable.
	for bits in bytes:
		binaryDataString += bin(bits)[2:].zfill(8)

	for char in binaryDataString:
		binaryDataList.append(char)
	
	#print binaryDataList

	#Get the length of the data string in order to know when to stop iterating later.
	binaryDataSize = len(binaryDataString)

	return binaryDataSize, binaryDataList

def binaryToFile:
	#tux1.bmp is the new file name
	with open("tux1.bmp", "w") as w:
		w.write(bytes)

def compareFileSize(coverFile, dataFile):
	coverFileSize = os.path.getsize(coverFile)
	print "Cover File Size (Bytes): %d"  %coverFileSize
	dataFileSize = os.path.getsize(dataFile)
	print "Data File Size (Bytes): %d" %dataFileSize
	#Code method to compare the file sizes - 8 to 1 ratio?

def hideData():
	binaryDataSize, binaryDataList = fileToBinary("butterfly.bmp")
	#Create an image object with the user selected image.
	imageObj = Image.open("butterfly.bmp")
	imageObjNew = imageObj.copy()
	#Get the dimensions of the image to create a new canvas with the same dimensions
	canvasWidth, canvasHeight = imageObjNew.size
	#print "Canvas width: %d" %canvasWidth + " canvas height: %d" %canvasHeight
	#Convert the type of image to an RGB image.
	rgba_img = imageObjNew.convert('RGBA')

	#r, g, b, a = rgba_img.getpixel((x,y))

	binaryConvertCounter = 0
	redList = []
	blueList = []
	greenList = []
	alphaList = []

	for xWidth in range(canvasWidth):
		for yHeight in range(canvasHeight):
			r, g, b, a = rgba_img.getpixel((xWidth,yHeight))
			
			print r, g, b, a

			#Constant checker to see if the binary counter is smaller than the total size of the binary data
			if binaryConvertCounter <= binaryDataSize:
				redBinary = decimalToBinary(r)
				redList = list(redBinary)
				#Hard code the array position to be 7 since the size of the decimal value will always be 8
				If not you can use (redList.length-1)
				redList[7] = binaryDataList[binaryConvertCounter]
				binaryConvertCounter += 1
			else:
				return

			if binaryConvertCounter <= binaryDataSize:
				greenBinary = decimalToBinary(g)
				greenList = list(greenBinary)
				greenList[7] = binaryDataList[binaryConvertCounter]
				binaryConvertCounter += 1
			else:
				return

			if binaryConvertCounter <= binaryDataSize:
				blueBinary = decimalToBinary(b)
				blueList = list(blueBinary)
				blueList[7] = binaryDataList[binaryConvertCounter]
				binaryConvertCounter += 1
			else:
				return

			if binaryConvertCounter <= binaryDataSize:
				alphaBinary = decimalToBinary(a)
				alphaList = list(alphaBinary)
				alphaList[7] = binaryDataList[binaryConvertCounter]
				binaryConvertCounter += 1
			else:
				return

			print r, g, b, a



if __name__ == "__main__":
	hideData()


	
	