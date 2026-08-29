import cv2

image = cv2.imread(r"C:\PYTHON\Assignment\Modules\photo.jpg")

cv2.imwrite("output.jpg", image)
"""if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")"""
    


"""
if image is None:
    print("Image not found")
else:
    cv2.imshow("My Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""

cv2.imwrite("output.jpg", image)

