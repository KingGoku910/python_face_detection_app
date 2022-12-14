import cv2, glob

gimp = glob.glob("*.jpg")
fclass = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

for gimgelement in gimp:
    img = cv2.imread(gimgelement)
    gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = fclass.detectMultiScale(gimp, scaleFactor=1.25, minNeighbors=5)

    for x,y,w,h in faces:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)


    #iw=int(img.shape[1]/3)
    #ih=int(img.shape[0]/3)
    #rimg = cv2.resize(img, (iw, ih))
    cv2.imshow("Gray", img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


 