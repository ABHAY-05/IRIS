import PyPDF2

def read_pdf(file_pdf, speak, take_command):
	try:
		pdf=open(f'C:\\Users\\ABHAY VERMA\\Documents\\pdf\\{file_pdf}.pdf','rb')
		pdfreader=PyPDF2.PdfFileReader(pdf)
		pages = pdfreader.numPages
		speak(f'This pdf file has {pages} pages')
		speak('which page should I read.')
		page_num=int(take_command())
		page=pdfreader.getPage(page_num)
		text=page.extractText()
		speak(text)
	except Exception as e:
		print(f'{e}\n')
		speak('sorry, some error has occurred')