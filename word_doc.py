from docx import Document

document = Document()

name = input('What is your name? : ')
last_name = input('What is your las name? : ')

document.add_paragraph('Hello ' + name + ' ' + last_name)

document.save('cv.docx')
print('Thanks! Check the document please ')
