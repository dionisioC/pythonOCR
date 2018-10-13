import cv2
import tempfile
import pytesseract
from pdf2image import convert_from_path
from os import listdir
from os.path import isfile, join

folder = 'samples/'

onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]

for file in onlyfiles:
    full_file = folder + file
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(full_file, fmt='jpeg', output_folder=path)
        for image in images_from_path:
            cv_image = cv2.imread(image.filename)
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            text = pytesseract.image_to_string(gray)
            print(text)
