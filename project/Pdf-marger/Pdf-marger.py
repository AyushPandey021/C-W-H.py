from pypdf import PdfWriter

merger = PdfWriter()
pdfs = []
n = int(input("how many pdfs do you want too marge?\n"))
for i in range(0, n):
    print("Enter the name of first pdf:")
    name = input(f"Enter the name of {i+1} pdf :")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()
