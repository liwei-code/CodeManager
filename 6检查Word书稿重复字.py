from docx import Document

doc = Document(r'D:/要写的Python教材/北邮《Python程序设计实用教程》/Python程序设计实用教程.docx')

contents = ''.join((p.text for p in doc.paragraphs))
words = []
for index, ch in enumerate(contents[:-2]):
    if ch==contents[index+1] or ch==contents[index+2]:
        word = contents[index:index+3]
        if word not in words:
            words.append(word)
            print(word)
