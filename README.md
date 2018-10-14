# pythonOCR
Sample using OCR in python with PDFs

## Samples
Samples are from:  
https://idrh.ku.edu/sites/idrh.ku.edu/files/files/tutorials/pdf/Text-searchable.pdf
https://idrh.ku.edu/sites/idrh.ku.edu/files/files/tutorials/pdf/Non-text-searchable.pdf

## How to use

1. Clone the repo.
2. Go inside the folder.  
``cd pythonOCR``
3. Create a virtual environment (tested with python 3.6).  
``python3.6 -m venv venv``
4. Activate the virtual env.  
``source venv/bin/activate``
5. Install the requirements.  
``pip install -r requirements.txt``
6. Install tesseract-ocr. Go to the [official repo](https://github.com/tesseract-ocr/tesseract) and follow the instructions for your OS.
7. Put the pdfs in the samples folder.
8. Run it!  
``python Main.py``