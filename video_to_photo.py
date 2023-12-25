import cv2

vid = cv2.VideoCapture("10.mp4")
count = 0

while True:
    success, image = vid.read()
    if not success:
        break
    
    filename = f"C:\\Users\\Yoga\\Downloads\\PROJECTS\\text_detect\\images\\frame_{count}.jpg"
    cv2.imwrite(filename, image)
    
    count += 1

vid.release()  

print(f"{count} frames saved as images.")
