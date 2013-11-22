import cv2
import numpy as np

def searchForPawn(img):
    #global img
    #img2 = cv2.imread(r"C:\Users\rexina\Dropbox\AGH\MiTP\cz.jpg")
    img2 = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    img2 = cv2.medianBlur(img2,5)
    #cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img2,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=43,param2=28,minRadius=0,maxRadius=0)

    if circles == None:
        print "NO_PAWN"
        return 0;
    print circles
    circles = np.uint16(np.around(circles))
    i = circles[0][0]


    d = int(i[2]/1.41)
    x = i[0]
    y = i[1]
    cv2.rectangle(img, (x-d,y-d),(x+d,y+d),(0,255,0))
    sum = [0.0, 0.0, 0.0]
    divi = 0
    for row in img2[x-d:x+d,y-d:y+d]:
        for px in row:
            sum += px
            divi += 1
        
    #if divi != 0: sum = [i/divi for i in sum]
    try:
        sum /= divi
    except TypeError:
        print "|!!!| ",sum,divi
        
    suma = sum[0] + sum[1] + sum[2];
    print "KOLOR: ",suma

    if suma > 300:
        print "WHITE PAWN"
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    else:
        print "BLACK PAWN"
        cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),2)
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    


    #cv2.imshow('detected circles',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

drawing = False
points = []
def mouseEvent(event, x, y, flags, param):
    global ix, iy, drawing,img,points
    if event == cv2.EVENT_LBUTTONDOWN:
        print x,y
        points.append([x,y])
        cv2.circle(img,(x,y),10,(0,0,255),-1)
        

img = cv2.imread(r"C:\Users\rexina\Dropbox\AGH\MiTP\asm.jpg")
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouseEvent)

rows,cols,ch = img.shape
pts1 = np.float32([[70,152],[392,159],[68,461],[381,469]])
pts2 = np.float32([[0,0],[600,0],[0,600],[600,600]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(600,600))


#points = [[66, 12], [176, 17], [288, 20], [401, 25], [512, 27], [626, 29], [735, 30], [844, 31], [948, 31], [62, 121], [180, 131], [288, 130], [402, 130], [510, 136], [623, 139], [731, 145], [837, 142], [948, 143], [62, 236], [174, 237], [290, 243], [399, 242], [507, 245], [617, 246], [720, 248], [843, 247], [940, 255], [60, 348], [169, 347], [283, 353], [397, 352], [504, 355], [610, 355], [723, 358], [833, 358], [941, 364], [68, 446], [169, 446], [284, 457], [395, 456], [502, 458], [615, 458], [723, 464], [834, 467], [943, 465], [58, 552], [166, 553], [281, 555], [390, 558], [500, 558], [603, 563], [725, 565], [828, 570], [937, 569], [60, 663], [165, 663], [275, 667], [386, 666], [499, 667], [606, 671], [722, 669], [829, 677], [937, 676], [52, 773], [160, 773], [275, 773], [391, 773], [494, 779], [606, 774], [715, 781], [831, 783], [931, 786], [50, 874], [162, 883], [274, 885], [386, 883], [492, 884], [605, 886], [721, 884], [825, 891], [927, 894]]
points = []
for i in range(1,602,75):
    for j in range(1,602,75):
        points.append([j,i]);
print points

print len(points)


dic = {}
for i in range(0,9):
    for j in range(0,9):
        dic[i,j] = points[9*i+j]

print dic[0,0],dic[1,1]

for i in range(0,8):
    for j in range(0,8):
        x1 = dic[i,j][0]
        y1 = dic[i,j][1]
        x2 = dic[i+1,j+1][0]
        y2 = dic[i+1,j+1][1]
        #cv2.imshow('image',img[y1:y2,x1:x2])
        searchForPawn(dst[y1:y2,x1:x2])
        #cv2.waitKey(0)

for i in points:
    cv2.circle (dst,tuple(i),3,(0,0,255),-1)

while True:
    cv2.imshow('image',dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break;
    
print points;
cv2.destroyAllWindows()

