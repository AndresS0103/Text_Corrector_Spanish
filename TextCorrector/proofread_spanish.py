#You need Python and this library on the next line:
#pip install language-tool-python

#For run this script you need to stay in the directory where you copy the file
#go to the command line and write: python proofread_spanish.py 
#and that's it enter your text and click enter!

import language_tool_python

def proofread_spanish(text):
    tool = language_tool_python.LanguageTool('es')
    matches = tool.check(text)
    correction = language_tool_python.utils.correct(text, matches)
    print("Original: {}".format(text))
    print("Correción: {}".format(correction))

text = input("Ingrese el texto a corregir: ")
proofread_spanish(text)