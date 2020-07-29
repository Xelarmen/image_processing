import cv2
img = cv2.imread('1.png',0)
esit = cv2.equalizeHist(img)
res = np.hstack((img,esit))
cv2.imwrite('res.png',res)

cv2.imshow("equalizeHist", res)
cv2.waitKey(0)

