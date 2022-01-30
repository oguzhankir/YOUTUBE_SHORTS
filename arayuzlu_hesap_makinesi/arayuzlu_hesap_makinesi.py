from tkinter import *


root=Tk()
root.title('Hesap Makinesi')
root.geometry('260x300')
root.resizable(FALSE,FALSE)
root.configure(bg='black')

entry=Entry(root,width=30,borderwidth=5)
entry.grid(row=0,column=0,columnspan=4)

def tiklanan_buton(sayi):
	entry.insert(END,sayi) 


def toplama():
	global sayi1
	global islem
	islem="toplama"
	sayi1=int(entry.get())
	entry.delete(0,END)


def cikarma():
	global sayi1
	global islem
	islem="cikarma"
	sayi1=int(entry.get())
	entry.delete(0,END)

def carpma():
	global sayi1
	global islem
	islem="carpma"
	sayi1=int(entry.get())
	entry.delete(0,END)

def bolme():
	global sayi1
	global islem
	islem="bolme"
	sayi1=int(entry.get())
	entry.delete(0,END)
    
def esittir():
	sayi2=int(entry.get())
	entry.delete(0,END)
	
	if islem=="toplama":
		entry.insert(0,sayi1 + sayi2) 	
	
	if islem=="cikarma":
		entry.insert(0,sayi1 - sayi2) 
	
	if islem=="bolme":
		entry.insert(0,sayi1 / sayi2)
	
	if islem=="carpma":
		entry.insert(0,sayi1 * sayi2) 	
	

def temizle():
	entry.delete(0,END)
		

buton_1=Button(root,text='1',font="times 14 ", bg='grey', 
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=lambda: tiklanan_buton(1))

buton_2=Button(root,text='2',font="times 14", bg='grey',
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=lambda: tiklanan_buton(2))

buton_3=Button(root,text='3',font="times 14", bg='grey',
               fg='white', activebackground='yellow',
               relief=RAISED, 
               command=lambda: tiklanan_buton(3))

buton_4=Button(root,text='4',font="times 14 ", bg='grey', 
               fg='white', activebackground='yellow', 
               command=lambda: tiklanan_buton(4))

buton_5=Button(root,text='5',font="times 14", bg='grey',
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=lambda: tiklanan_buton(5))

buton_6=Button(root,text='6',font="times 14", bg='grey',
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=lambda: tiklanan_buton(6))

buton_7=Button(root,text='7',font="times 14 ", bg='grey', 
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=lambda: tiklanan_buton(7))

buton_8=Button(root,text='8',font="times 14", bg='grey',
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=lambda: tiklanan_buton(8))

buton_9=Button(root,text='9',font="times 14", bg='grey',
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=lambda: tiklanan_buton(9))

buton_0=Button(root,text='0',font="times 14", bg='grey',
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=lambda: tiklanan_buton(0))

buton_topla=Button(root,text='+',font="times 14", bg='grey',
               fg='white', activebackground='yellow',
               relief=RAISED, 
               command=toplama)

buton_cikar=Button(root,text='-',font="times 14", bg='grey',
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=cikarma)

buton_bol=Button(root,text='/',font="times 14", bg='grey',
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=bolme)

buton_carp=Button(root,text='*',font="times 14", bg='grey',
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=carpma)

buton_esittir=Button(root,text='=',font="times 14", bg='grey',
               fg='white', activebackground='yellow',
               relief=RAISED, 
               command=esittir)

#en sontanimla
buton_temizle=Button(root,text='Temizle',font="times 14", bg='grey',
               fg='white', activebackground='yellow', 
               relief=RAISED,
               command=temizle)

buton_1.grid(row=1,column=0, padx=4, pady=4, ipadx=26)
buton_2.grid(row=1,column=1,padx=4, pady=4, ipadx=26)
buton_3.grid(row=1,column=2, padx=4,pady=4, ipadx=26)
buton_4.grid(row=2,column=0, padx=4, pady=4, ipadx=26)
buton_5.grid(row=2,column=1,padx=4, pady=4, ipadx=26)
buton_6.grid(row=2,column=2, padx=4,pady=4, ipadx=26)
buton_7.grid(row=3,column=0, padx=4, pady=4, ipadx=26)
buton_8.grid(row=3,column=1,padx=4, pady=4, ipadx=26)
buton_9.grid(row=3,column=2, padx=4,pady=4, ipadx=26)
buton_0.grid(row=4,column=0, padx=4, pady=4, ipadx=26)
buton_topla.grid(row=4,column=1,padx=4, pady=4, ipadx=26)
buton_cikar.grid(row=4,column=2, padx=4,pady=4, ipadx=26)
buton_carp.grid(row=5,column=0,padx=4, pady=4, ipadx=26)
buton_bol.grid(row=5,column=1, padx=4,pady=4, ipadx=29)
buton_esittir.grid(row=5,column=2, padx=4,pady=4, ipadx=24)
buton_temizle.grid(row=6,column=0, columnspan=3)
root.mainloop()
