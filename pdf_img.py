import fitz

# Open the PDF file
pdf = fitz.open("Voting Booth.pdf")

# Select the page that you want to save
page_number=0
page = pdf[page_number]

# Save the page as a JPG image
pix = page.get_pixmap(alpha=False)
pix.pil_save("page_{}.jpg".format(page_number))
