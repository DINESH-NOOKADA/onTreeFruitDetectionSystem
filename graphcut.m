clc 
clear all
close all
warning off
RGB=imread("./originalImage/originalImage1.jpg")
[BW,maskedImage] = segmentImage2(RGB)
imshow(BW)