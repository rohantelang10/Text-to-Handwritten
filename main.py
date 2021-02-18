import pywhatkit
print('Convert the text into handwritten\n')
txt = input('Enter the text(paragraph) - \n')
pywhatkit.text_to_handwriting(txt, rgb=[0,0,255])