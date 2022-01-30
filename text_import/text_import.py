from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("dosya import")
root.geometry("400x400")

yazi = StringVar()
yazi = Text(root, width=20, height=10, font="times 20 bold")
yazi.pack()

def dosyaImport():
    importDosya=filedialog.askopenfilename(
                initialdir="desktop/YOUTUBE/SHORTS/\
                    text_import",
                title="Bir dosya seçin",
                filetypes=(
                    ("text files",".txt"),("all files","*.*")
                )
    )

    with open(importDosya, "r") as file:
        dosya = file.read()
        yazi.insert(INSERT, dosya)
        yazi.config(state=DISABLED)
        print(dosya)

    file.close()


importButon = Button(root, text="Dosya import",
                command=dosyaImport).pack()

root.mainloop()