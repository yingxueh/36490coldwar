# creates .txt from pdf files
# pip3 install Pillow
# pip3 install pytesseract
# pip3 install pdf2image
# source /Users/suzannenie/.virtualenvs/venv/bin/activate


# Import libraries
from PIL import Image, ImageEnhance
import pytesseract
import sys
from pdf2image import convert_from_path
import os
  
def generate_text(infile, outfile):
    PDF_file = infile
    
    # Store all the pages of the PDF in a variable
    pages = convert_from_path(PDF_file, 500)
    
    image_counter = 1
    
    for page in pages:
    
        filename = "page_"+str(image_counter)+".jpg"
        # Save the image of the page in system
        page.save(filename, 'JPEG')

        img = Image.open(filename)
        gray = img.convert('L')
        bw = gray.point(lambda x: 0 if x<170 else 255, '1')
  
        # showing resultant image
        bw.show()

        # img_contr_obj=ImageEnhance.Contrast(img)
        # # increase contrast
        # e_img=img_contr_obj.enhance(5)
        bw.save(filename)
    
        # Increment the counter to update filename
        image_counter = image_counter + 1
 
    '''
    Part #2 - Recognizing text from the images using OCR
    '''

    filelimit = image_counter-1
    f = open(outfile, "a")
    
    # Iterate from 1 to total number of pages
    for i in range(2, filelimit + 1):
    
        filename = "page_"+str(i)+".jpg"
            
        # Recognize the text as string in image using pytesserct
        text = str(((pytesseract.image_to_string(Image.open(filename)))))
  
        text = text.replace('-\n', '')    
    
        f.write(text)
    
    f.close()

if __name__ == "__main__":
    i = 30
    while (i < 31):
        infile = "{}.pdf".format(i)
        outfile = "{}.txt".format(i)
        print(infile)
        generate_text(infile, outfile)
        print("done")
        i += 1