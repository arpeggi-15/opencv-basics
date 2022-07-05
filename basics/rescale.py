import cv2 as cv

# img = cv.imread('Photos/cat_large2.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    #For images, videos and live videos

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #Only for Live video
    capture.set(3,width)
    capture.set(4,height)


#Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)