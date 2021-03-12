import PyPDF2 


def merge_pdfs(_pdfs):

    merge_file = PyPDF2.PdfFileMerger()

    for _pdf in _pdfs:

        merge_file.append(PyPDF2.PdfFileReader(_pdf, 'rb'))

    merge_file.write("New_Merged_File.pdf")


if __name__ == '__main__':

    _pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf']

    merge_pdfs(_pdfs)
