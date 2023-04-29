from tkinter import *
from tkinter.ttk import Notebook, Frame
from iznos import Iznos
from avg_cost import Avg_cost
from proj.remont import remont_tab


def run():
    # Tkinter settings
    window = Tk()
    window.title("Калькулятор износа машин")
    window.geometry('500x300')

    # Tabs
    tab_control = Notebook(window)
    tab1 = Frame(tab_control)
    tab2 = Frame(tab_control)
    tab3 = Frame(tab_control)
    tab_control.add(tab1, text='Физ износ')
    tab_control.add(tab2, text='Ср. стоимость ТС')
    tab_control.add(tab3, text='Стоимость ремонта')

    tab_control.pack(expand=1, fill='both')

    iznos = Iznos(tab1)
    iznos.start()

    avg_cost = Avg_cost(tab2)
    avg_cost.start()

    remont_tab(tab3)

    window.mainloop()


if __name__ == '__main__':
    run()
