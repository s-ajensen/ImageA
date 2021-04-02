import os
import re
import cv2
import sys

# Generates .avi of all .png files in 'src'
def video_writer(src):
    images = [img for img in os.listdir(src) if img.endswith(".png")]
    
    if images != []:
        frame = cv2.imread(os.path.join(src, images[0]))
        height, width, layers = frame.shape

        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        video = cv2.VideoWriter("%s.avi" % src, fourcc, 7, (width,height))

        for image in images:
            video.write(cv2.imread(os.path.join(src, image)))

        cv2.destroyAllWindows()
        video.release()

# generates movies for images in each subdir of 'src' if it matches the optional regex 'fil'
def image_a(src, fil=''):
    # holds paths for directors containing image sequences
    sequence_dirs = []

    # gather list of directories to generate movies from
    for (root, dirs, files) in os.walk(src):
        for d in dirs:
            if re.search(fil, d):
                sequence_dirs.append("%s/%s" % (root, d))

    # iterate through dirs and make movies
    for d in sequence_dirs:
        video_writer(d)

def main():
    
    try:
        path = sys.argv[1]
        image_a(path)
    except IndexError:
        print("Please provide path to root directory as argument.")

if __name__ == "__main__":
    main()