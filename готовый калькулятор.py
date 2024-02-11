from tkinter import *
from tkinter import ttk
import math
from math import *
from tkinter import messagebox
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

s=2
n=2
def clicked():
    global s
    s+=1
    res = (((8 * math.pi * 3 * 10 ** 8) / float(chit_znach.get()) ** 5) * (
            1 / (math.exp(
        (6.62607015 * 10 ** (-34) * 3 * 10 ** 8) / (float(chit_znach.get()) * 1.380649 * 10 ** (-23) * 2500)) - 1))) * 10 ** 30
    ras_zn = Label(frame1, text="")
    ras_zn.grid(row=s + 1, column=1)
    ras_zn.configure(text=res)
    volnzn = Label(frame1, text="")
    volnzn.grid(row=s + 1, column=0)
    volnzn.configure(text=chit_znach.get())

dotArr = []
def clean():
    global dotArr
    dotArr = []
def calk2():
    window_culc2=Tk()
    window_culc2.geometry("300x300")
    dlina_voln = Label(window, text="введите значение(нм)")
    dlina_voln.grid(column=0, row=1)
def grafik():
    grafik=Tk()
    grafik.geometry('600x500')
    if niz.get() == "":
        x1 = np.arange(300, 5000, 0.01)
    else:
        x1 = np.arange(float(niz.get()), float(ver.get()), 0.01)
    x2 = float(chit_znach.get())
    y1 = (((8 * np.pi * 3 * 10 ** 8) / x1 ** 5) * (1 / (np.exp(
        (6.62607015 * 10 ** (-34) * 3 * 10 ** 8) / (x1 * 1.380649 * 10 ** (-23) * 2500)) - 1))) * 10 ** 30
    y2 = (((8 * np.pi * 3 * 10 ** 8) / x2 ** 5) * (1 / (np.exp(
        (6.62607015 * 10 ** (-34) * 3 * 10 ** 8) / (x2 * 1.380649 * 10 ** (-23) * 2500)) - 1))) * 10 ** 30
    
    dotArr.append([x2, y2])

    
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    plot = figure.add_subplot(1, 1, 1)
    plot.set_xlabel('длина волны')
    plot.set_ylabel('спектральная плотность энергии')
    plot.plot(x1, y1)

    for i in range(0, len(dotArr)):
        plot.scatter(dotArr[i][0], dotArr[i][1], color="red")

    canvas = FigureCanvasTkAgg(figure, grafik)
    canvas.get_tk_widget().grid(row=3, column=5)

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        window.destroy()
def spravka():
    spravka = Tk()
    spravka.title("справка")
    spravka.geometry("150x150")
    form = Label(spravka, text="8πhc                 1         \n–––––– ––––––––––––––\n  λ\u2075     exp(hc/λkT)-1 "
                          "\n\n T - температура, К \n"
                          "k - пстоянная Больцмана \n"
                          "λ - длина волны, нм \n"
                          "h - постоянная Планка \n"
                          "c - скорость света")
    form.grid(column=0, row=0)

window = Tk()
tabs = ttk.Notebook(window,width = 1920, height = 1100)
tabs.grid(row=0,column=0)
frame1 = ttk.Frame(tabs)
frame2 = ttk.Frame(tabs)
tabs.add(frame1, text="калькулятор1")
tabs.add(frame2, text="калькулятор2")

season = ["Не учитывать", "Зима", "Лето"]
season_var = StringVar(value=season[0])
def selected(event):
    selection1 = combobox.get()
    print(selection1)
    print(combobox.get())
    print(selected)
    label_season["text"] = f"вы выбрали: {selection1}" 
label_season = ttk.Label(textvariable=season_var)
combobox = ttk.Combobox(frame2,values=season,textvariable=season_var,state="DISABLED")
combobox.grid(row=1,column=6)
combobox.bind("<<ComboboxSelected>>", selected)
#selection1 = combobox.get()

h=1


def selected2(event):
    selection = combobox1.get()
    print(selection)
    label_sost_atm["text"] = f"вы выбрали: {selected2}"
sost_atm = ["Не учитывать","Воздух абсолютно чист",
 "Исключительно высокая прозрачность",
  "Вoздух очень прозрачен",
   "Хорошая прозрачность",
   "Средняя прозрачность",
   "Воздух несколько мутен",
   "Воздух мутен",
   "Воздух очень мутен",
   "Лёгкий туман",
   "Туман",
   "густой туман"]
sost_atm_var = StringVar(value=sost_atm[0])

label_sost_atm = ttk.Label(textvariable=sost_atm_var)
combobox1 = ttk.Combobox(frame2,values=sost_atm,textvariable=sost_atm_var,state="DISABLED")
combobox1.grid(row=1,column=5)
combobox1.bind("<<ComboboxSelected>>", selected2)
window.title("калькулятор")
window.protocol("WM_DELETE_WINDOW", on_closing)
window.geometry("650x300")
main_menu = Menu()
main_menu.add_cascade(label="файл")
main_menu.add_cascade(label="кальк2",command=calk2)
main_menu.add_cascade(label="View")
window.config(menu=main_menu)

voln = Label(frame1, text="длина волны")
voln.grid(row=2, column=0)

ras = Label(frame1, text="спектральная плотность\n  энергии")
ras.grid(row=2, column=1)

dlina_voln = Label(frame1, text="введите значение(нм)")
dlina_voln.grid(column=0, row=1)

chit_znach = Entry(frame1, width=10)
chit_znach.grid(column=1, row=1)

niz = Entry(frame1, width=10)
niz.grid(column=4, row=1)

ver = Entry(frame1, width=10)
ver.grid(column=4, row=2)

graf = Button(frame1, text="график", command=grafik)
graf.grid(column=3, row=1)
clean = Button(frame1, text="очистка", command=clean)
clean.grid(column=6, row=1)

lambd = Button(frame1, text="λ", command=clicked)
lambd.grid(column=2, row=1)
spravka = Button(frame1,text="справка",command=spravka)
spravka.grid(column=5,row=2)

"жёстко высрал второе окно"
visota = Label(frame2, text="введите значение(м)")
visota.grid(column=0, row=1)
chit_znach2 = Entry(frame2, width=10)
chit_znach2.grid(column=1, row=1)
label_davlenie = Label(frame2, text="давление(кПа)")
label_davlenie.grid(row=2, column=1)
label_plotnost = Label(frame2, text="плотность(кг/м³)")
label_plotnost.grid(row=2, column=2)
label_visot = Label(frame2, text="высота(м)")
label_visot.grid(row=2, column=0)
niz2 = Entry(frame2, width=10)
niz2.grid(column=4, row=1)
ver2 = Entry(frame2, width=10)
ver2.grid(column=4, row=2)

def clicked2():
    global n
    n+=1
    if combobox1.get() == "Не учитывать" or "" :
        kef= 1
    if combobox1.get() == "Воздух абсолютно чист" :
        kef= 0.99
    if combobox1.get()=="Исключительно высокая прозрачность":
         kef= 0.97
    if combobox1.get()=="Вoздух очень прозрачен":
         kef= 0.96
    if combobox1.get()=="Хорошая прозрачность":
         kef= 0.92
    if combobox1.get()=="Средняя прозрачность":
         kef= 0.81
    if combobox1.get()=="Воздух несколько мутен":
         kef= 0.66
    if combobox1.get()=="Воздух мутен":
         kef= 0.36
    if combobox1.get()=="Воздух очень мутен":
        kef= 0.12
    if combobox1.get()=="Лёгкий туман":
        kef=0.015
    if combobox1.get()=="Туман":
        kef=np.arange(2*10**-4,8*10**-10)
    if combobox1.get()=="густой туман":
        kef=0
    if combobox.get()=="Лето":
        if float(chit_znach2.get()) in range(0,2000):
            koef =1.284
        if float(chit_znach2.get()) in range(2000,4000):
            koef =0.995
        if float(chit_znach2.get()) in range(4000,8000):
            koef =0.808
        if float(chit_znach2.get()) in range(8000,12000):
            koef =0.527
        if float(chit_znach2.get()) in range(12000,16000):
            koef =0.319
        if float(chit_znach2.get()) in range(16000,20000):
            koef =0.172
    elif combobox.get() == "Зима":
        if float(chit_znach2.get()) in range(0,2000):
            koef = 1.1288
        if float(chit_znach2.get()) in range(2000,4000):
            koef =1.025
        if float(chit_znach2.get()) in range(4000,8000):
            koef=0.827
        if float(chit_znach2.get()) in range(8000,12000):
            koef=530
        if float(chit_znach2.get()) in range(12000,16000):
            koef=0.303
        if float(chit_znach2.get()) in range(16000,20000):
            koef =0.152
    else:
        koef=1
    davlenie=1000**-1*p*((1+(L*float(chit_znach2.get()))/T)**(-g*M/(R*L)))
    tob=T+L*float(chit_znach2.get())
    plotnost=(davlenie*M/(R*tob))*koef*kef
    ras_zn_dav = Label(frame2, text="")
    ras_zn_dav.grid(row=n + 1, column=1)
    ras_zn_dav.configure(text=davlenie)
    vivod_wisot = Label(frame2, text="")
    vivod_wisot.grid(row=n + 1, column=0)
    vivod_wisot.configure(text=chit_znach2.get())
    ras_zn_p = Label(frame2, text="")
    ras_zn_p.grid(row=n + 1, column=2)
    ras_zn_p.configure(text=plotnost)
    volnzn = Label(frame2, text="aaa")
dotArr2=[]
def grafik2():

    grafik2=Tk()
    grafik2.geometry('600x500')
    if niz2.get() == "":
        x1 = np.arange(100, 10000, 100)
    else:
        x1 = np.arange(float(niz2.get()), float(ver2.get()), 10)
    x2 = float(chit_znach2.get())
    if combobox1.get() == "Не учитывать" or "" :
        kef= 1
    if combobox1.get() == "Воздух абсолютно чист" :
        kef= 0.99
    if combobox1.get()=="Исключительно высокая прозрачность":
         kef= 0.97
    if combobox1.get()=="Вoздух очень прозрачен":
         kef= 0.96
    if combobox1.get()=="Хорошая прозрачность":
         kef= 0.92
    if combobox1.get()=="Средняя прозрачность":
         kef= 0.81
    if combobox1.get()=="Воздух несколько мутен":
         kef= 0.66
    if combobox1.get()=="Воздух мутен":
         kef= 0.36
    if combobox1.get()=="Воздух очень мутен":
        kef= 0.12
    if combobox1.get()=="Лёгкий туман":
        kef=0.015
    if combobox1.get()=="Туман":
        kef=np.arange(2*10**-4,8*10**-10)
    if combobox1.get()=="густой туман":
        kef=0
    if combobox.get()=="Лето":
        if float(chit_znach2.get()) in range(0,2000):
            koef =1.284
        if float(chit_znach2.get()) in range(2000,4000):
            koef =0.995
        if float(chit_znach2.get()) in range(4000,8000):
            koef =0.808
        if float(chit_znach2.get()) in range(8000,12000):
            koef =0.527
        if float(chit_znach2.get()) in range(12000,16000):
            koef =0.319
        if float(chit_znach2.get()) in range(16000,20000):
            koef =0.172
    if combobox.get() == "Зима":
        if float(chit_znach2.get()) in range(0,2000):
            koef = 1.1288
        if float(chit_znach2.get()) in range(2000,4000):
            koef =1.025
        if float(chit_znach2.get()) in range(4000,8000):
            koef=0.827
        if float(chit_znach2.get()) in range(8000,12000):
            koef=530
        if float(chit_znach2.get()) in range(12000,16000):
            koef=0.303
        if float(chit_znach2.get()) in range(16000,20000):
            koef =0.152
    if combobox.get() == "Не учитывать":
        koef= 1
    y2 = koef*np.exp(1/cos(90))*kef*float(chit_znach2.get())*10**-3#x1 relf ,kznm
    y1 = koef*math.exp(1/cos(90))*x1*10**-3#
    dotArr2.append([x2, y2])#

    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot()
    

    figure = plt.Figure(figsize=(5, 4), dpi=105)
    plot = figure.add_subplot(1, 1, 1)
    plot.set_xlabel('Высота')
    plot.set_ylabel('Пропускание')
    plot.plot(x1, y1)

    for i in range(0, len(dotArr2)):
                    plot.scatter(dotArr2[i][0], dotArr2[i][1], color="red")

    canvas2 = FigureCanvasTkAgg(figure, grafik2)
    canvas2.get_tk_widget().place(x=10,y=10)

knopka = Button(frame2, text="подсчёт", command=clicked2)
knopka.grid(column=2, row=1)
graf2 = Button(frame2, text="график", command=grafik2)
graf2.grid(column=5, row=2)
p=101325
T=288.15
g=9.80665
L=-0.0065
R=8.31447
M=0.0289644

window.mainloop()
