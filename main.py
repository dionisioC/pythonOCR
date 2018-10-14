import tempfile
from os.path import isfile, join
from os import listdir
import cv2
import pytesseract
from pdf2image import convert_from_path

FOLDER = 'samples/'

ONLY_FILES = [f for f in listdir(FOLDER) if isfile(join(FOLDER, f))]

for current_file in ONLY_FILES:
    full_file = FOLDER + current_file
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(full_file, fmt='jpeg', output_folder=path)
        for image in images_from_path:
            cv_image = cv2.imread(image.filename)
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            text = pytesseract.image_to_string(gray)
            print(text)
