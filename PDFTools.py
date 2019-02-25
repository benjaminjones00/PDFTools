#imports
from pylovepdf.ilovepdf import ILovePdf
from tkinter import *
from tkinter.filedialog import *
import os
import sys

root = Tk()
pdf = ILovePdf('project_public_a9f9d7bdb00a5ea6e979300159080d1c_U7Q7Zdb57934cfb70703c5d774c11c0cb1bc7', verify_ssl=True)
save_location = os.getcwd()

def devmode():
        print('\n'
              '\n'
              '\n'
              '=== This feature is currently in Development === \n'
              '\n'
              '\n')

def get_pdf_file():
	Tk().withdraw()
	filename = askopenfilename()
	Tk().withdraw()
	return filename

def compresspdf():
        pdf_file = get_pdf_file()
        pdf_task = pdf.new_task('compress') #Start the pdf task
        pdf_task.add_file(pdf_file)
        pdf_task.set_output_folder(save_location) #Sets output folder
        pdf_task.execute() #Start compressing the pdf
        pdf_task.download() #Download PDF
        print('Your PDF file is saved at: ' + save_location)
        returntomenu = input('Press ENTER to return to menu')
        if returntomenu == '':
                Menu()

def Menu():
        while True:
                root.withdraw()
                print('PDF Tasks v.1\nWhat would you like to do today?: ')
                print('1: Comress PDF\n'
                      '2: Merge PDF\n'
                      '3: Unlock a password protected PDF\n'
                      '4: Password Protect your PDF\n'
                      '5: Convert an image to a PDF\n'
                      '6: Detect text inside a PDF and convert it to a txt file\n'
                      '\n'
                      'Type "exit" to exit the program'
                      '\n')
                menu_choice = input('Option: ')

                if menu_choice == '1':
                        compresspdf()
                elif menu_choice == '2':
                        devmode()
                elif menu_choice == '3':
                        devmode()
                elif menu_choice == '4':
                        devmode()
                elif menu_choice == '5':
                        devmode()
                elif menu_choice == '6':
                        devmode()
                else:
                        sys.exit()
Menu()


