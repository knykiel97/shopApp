from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
import tkinter as tk
from PIL import Image, ImageTk

class Koszyk(Frame):
    def __init__(self):
        super().__init__()
        self.shoppinglist = []
        self.adding = True
        self.initUI()

    def initUI(self):
        def press():
            sc.delete("1.0", tk.END)
            sc.insert(tk.END, getList(self))

        def addpress():
            self.adding=not self.adding
            if self.adding==True:
                ar['text'] = "Click to \r remove"
                press()
            else:
                ar['text']="Click to \r add"
                press()

        def shop(s):
            if(self.adding==True):
                self.shoppinglist.append(s)
            else:
                if s in self.shoppinglist:
                    self.shoppinglist.remove(s)

        self.master.title("sklyp")


        # Trasa button dla PageRoute master.switch_frame(PageRoute)    .pack()
        trasa = tk.Button(self, text="Route", bg="red", fg="white", font='Calibri 17 bold', width=13,
                       height=3, command=lambda: None)
        trasa.grid(row=2, column=6)

        ar = tk.Button(self, text="Remove \r Item", bg="green", fg="white", font='Calibri 17 bold', width=13,
                       height=3, command=lambda: [addpress()])
        ar.grid(row=3, column=6)

        exit = tk.Button(self, text="Exit", fg="white", bg="blue", font='Calibri 17 bold',
                         command=self.master.destroy, width=13, height=3)
        exit.grid(row=4, column=6)

        woda = tk.Button(self, command=lambda:[shop("Woda"),press()])
        image = Image.open('woda.jpg')
        image = image.resize((100,100))
        myimage = ImageTk.PhotoImage(image)
        woda.config(image=myimage, width=100, height=100, bg="green")
        woda.image = myimage
        woda.grid(row=2, column=1)

        napgaz = tk.Button(self, command=lambda:[shop("Napoje gazowane"),press()])
        myimage = Image.open('napgaz.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        napgaz.config(image=image, width=100, height=100, bg="green")
        napgaz.image = image
        napgaz.grid(row=2, column=2)

        napowo = tk.Button(self, command=lambda: [shop("Napoje owocowe"),press()])
        myimage = Image.open('napowo.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        napowo.config(image=image, width=100, height=100, bg="green")
        napowo.image = image
        napowo.grid(row=2, column=3)

        alko = tk.Button(self, command=lambda:[shop("Alkohole mocne"),press()])
        myimage = Image.open('alko.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        alko.config(image=image, width=100, height=100, bg="green")
        alko.image = image
        alko.grid(row=2, column=4)

        piwa = tk.Button(self, command=lambda: [shop("Piwa"), press()])
        myimage = Image.open('piwa.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        piwa.config(image=image, width=100, height=100, bg="green")
        piwa.image = image
        piwa.grid(row=2, column=5)

        sery = tk.Button(self, command=lambda: [shop("Sery "), press()])
        myimage = Image.open('sery.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        sery.config(image=image, width=100, height=100, bg="green")
        sery.image = image
        sery.grid(row=3, column=1)

        jogurty = tk.Button(self, command=lambda: [shop("Jogurty"), press()])
        myimage = Image.open('jogurty.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        jogurty.config(image=image, width=100, height=100, bg="green")
        jogurty.image = image
        jogurty.grid(row=3, column=2)

        smietany = tk.Button(self, command=lambda: [shop("Śmietany"), press()])
        myimage = Image.open('smietany.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        smietany.config(image=image, width=100, height=100, bg="green")
        smietany.image = image
        smietany.grid(row=3, column=3)

        mleka = tk.Button(self, command=lambda: [shop("Mleka"), press()])
        myimage = Image.open('mleka.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        mleka.config(image=image, width=100, height=100, bg="green")
        mleka.image = image
        mleka.grid(row=3, column=4)

        jajka = tk.Button(self, command=lambda: [shop("Jajka"), press()])
        myimage = Image.open('jajka.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        jajka.config(image=image, width=100, height=100, bg="green")
        jajka.image = image
        jajka.grid(row=3, column=5)

        mieso = tk.Button(self, command=lambda: [shop("Mięso"), press()])
        myimage = Image.open('miesa.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        mieso.config(image=image, width=100, height=100, bg="green")
        mieso.image = image
        mieso.grid(row=4, column=1)

        przyprawy = tk.Button(self, command=lambda: [shop("przyprawy"), press()])
        myimage = Image.open('przyprawy.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        przyprawy.config(image=image, width=100, height=100, bg="green")
        przyprawy.image = image
        przyprawy.grid(row=4, column=2)

        artcuk = tk.Button(self, command=lambda:[shop("Artykuły cukiernicze"),press()])
        myimage = Image.open('artcuk.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artcuk.config(image=image, width=100, height=100, bg="green")
        artcuk.image = image
        artcuk.grid(row=4, column=3)

        ryze = tk.Button(self, command=lambda:[shop("Ryże"),press()])
        myimage = Image.open('ryze.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        ryze.config(image=image, width=100, height=100, bg="green")
        ryze.image = image
        ryze.grid(row=4, column=4)

        kasze = tk.Button(self, command=lambda: [shop("Kasze"),press()])
        myimage = Image.open('kasze.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        kasze.config(image=image, width=100, height=100, bg="green")
        kasze.image = image
        kasze.grid(row=4, column=5)

        ciastka = tk.Button(self, command=lambda:[shop("Ciastka"),press()])
        myimage = Image.open('ciastka.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        ciastka.config(image=image, width=100, height=100, bg="green")
        ciastka.image = image
        ciastka.grid(row=5, column=1)

        czipery = tk.Button(self, command=lambda: [shop("Chipsy"), press()])
        myimage = Image.open('czipsy.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        czipery.config(image=image, width=100, height=100, bg="green")
        czipery.image = image
        czipery.grid(row=5, column=2)

        makarony = tk.Button(self, command=lambda: [shop("Makarony"), press()])
        myimage = Image.open('makarony.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        makarony.config(image=image, width=100, height=100, bg="green")
        makarony.image = image
        makarony.grid(row=5, column=3)

        konserwy = tk.Button(self, command=lambda: [shop("Konserwy"), press()])
        myimage = Image.open('konserwy.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        konserwy.config(image=image, width=100, height=100, bg="green")
        konserwy.image = image
        konserwy.grid(row=5, column=4)

        platki = tk.Button(self, command=lambda: [shop("Płatki śniadaniowe"), press()])
        myimage = Image.open('platki.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        platki.config(image=image, width=100, height=100, bg="green")
        platki.image = image
        platki.grid(row=5, column=5)

        owoce = tk.Button(self, command=lambda: [shop("Owoce"), press()])
        myimage = Image.open('owoce.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        owoce.config(image=image, width=100, height=100, bg="green")
        owoce.image = image
        owoce.grid(row=6, column=1)

        warzywa = tk.Button(self, command=lambda: [shop("Warzywa"), press()])
        myimage = Image.open('warzywa.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        warzywa.config(image=image, width=100, height=100, bg="green")
        warzywa.image = image
        warzywa.grid(row=6, column=2)

        pieczywo = tk.Button(self, command=lambda: [shop("Pieczywo"), press()])
        myimage = Image.open('pieczywo.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        pieczywo.config(image=image, width=100, height=100, bg="green")
        pieczywo.image = image
        pieczywo.grid(row=6, column=3)

        ubrania = tk.Button(self, command=lambda: [shop("Ubrania"), press()])
        myimage = Image.open('ubrania.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        ubrania.config(image=image, width=100, height=100, bg="green")
        ubrania.image = image
        ubrania.grid(row=6, column=4)

        rtv = tk.Button(self, command=lambda: [shop("RTV"),press()])
        myimage = Image.open('rtv.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        rtv.config(image=image, width=100, height=100, bg="green")
        rtv.image = image
        rtv.grid(row=6, column=5)

        agd = tk.Button(self, command=lambda:[shop("AGD"),press()])
        myimage = Image.open('agd.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        agd.config(image=image, width=100, height=100, bg="green")
        agd.image = image
        agd.grid(row=7, column=1)

        artnapr = tk.Button(self, command=lambda: [shop("Narzędzia"), press()])
        myimage = Image.open('narzedzia.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artnapr.config(image=image, width=100, height=100, bg="green")
        artnapr.image = image
        artnapr.grid(row=7, column=2)

        artrosl = tk.Button(self, command=lambda: [shop("Art. Do uprawy roślin"), press()])
        myimage = Image.open('artros.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artrosl.config(image=image, width=100, height=100, bg="green")
        artrosl.image = image
        artrosl.grid(row=7, column=3)

        srczyst = tk.Button(self, command=lambda: [shop("Środki czystości"), press()])
        myimage = Image.open('srczys.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        srczyst.config(image=image, width=100, height=100, bg="green")
        srczyst.image = image
        srczyst.grid(row=7, column=4)

        kosmetyki = tk.Button(self, command=lambda: [shop("Kosmetyki"), press()])
        myimage = Image.open('kosmetyki.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        kosmetyki.config(image=image, width=100, height=100, bg="green")
        kosmetyki.image = image
        kosmetyki.grid(row=7, column=5)

        artszk = tk.Button(self, command=lambda: [shop("Art. Szkolne"), press()])
        myimage = Image.open('artszk.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artszk.config(image=image, width=100, height=100, bg="green")
        artszk.image = image
        artszk.grid(row=8, column=1)

        zabawki = tk.Button(self, command=lambda: [shop("Zabawki"), press()])
        myimage = Image.open('zabawki.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        zabawki.config(image=image, width=100, height=100, bg="green")
        zabawki.image = image
        zabawki.grid(row=8, column=2)

        artzoo = tk.Button(self, command=lambda: [shop("Art. Zoologiczne"), press()])
        myimage = Image.open('artzoo.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artzoo.config(image=image, width=100, height=100, bg="green")
        artzoo.image = image
        artzoo.grid(row=8, column=3)

        artkuch = tk.Button(self, command=lambda: [shop("Art. Kuchenne"), press()])
        myimage = Image.open('artkuch.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artkuch.config(image=image, width=100, height=100, bg="green")
        artkuch.image = image
        artkuch.grid(row=8, column=4)

        promocje = tk.Button(self, command=lambda: [shop("Promocje"), press()])
        myimage = Image.open('promocje.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        promocje.config(image=image, width=100, height=100, bg="green")
        promocje.image = image
        promocje.grid(row=8, column=5)

        sc = tk.Text(self, height=26, width=20)
        sc.insert(tk.END, getList(self))
        sc.grid(row=5, column=6, rowspan=4)

        self.pack()

def getList(self):
    items='Koszyk: \n'
    for item in self.shoppinglist:
        items+= item + "\n"
    return items

def main():
    root = Tk()
    app = Koszyk()
    root.configure(background="green")
    root.mainloop()

if __name__ == '__main__':
    main()
