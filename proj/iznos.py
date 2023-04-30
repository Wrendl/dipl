import math
from tkinter import *
from datetime import datetime
from tkinter.ttk import Combobox
from proj.data import get_marks_models, print_models, get_a_b_L0_ML, data_to_excel, close_excel


class Iznos:
    
    def __init__(self, tab, wb):
        self.tab = tab
        self.cars = list(get_marks_models().keys())
        self.wb = wb
        self.header = ["Марка", "Модель", "Год", "Пробег", "Физ износ"]

    def updtcblist(self, model, marka):
        model['values'] = print_models(marka.get())
    
    def start(self):
        tab = self.tab

        # Текст
        Label(tab, text='Марка').grid(row=0)
        Label(tab, text='Модель').grid(row=1)
        Label(tab, text='Год').grid(row=2)
        Label(tab, text='Пробег').grid(row=3)
    
        # Выбор марки машин
        marka = Combobox(tab)
        marka['values'] = self.cars
        marka.current(0)
        marka.grid(row=0, column=1)
    
        # Выбор модель машины
        model = Combobox(tab, postcommand=lambda: self.updtcblist(model, marka))
        model.grid(row=1, column=1)
    
        # Инпут срок, пробег
        year = Entry(tab)
        year.insert(-1, "2023")
        year.grid(row=2, column=1, sticky="ew")
        probeg = Entry(tab)
        probeg.insert(-1, "0")
        probeg.grid(row=3, column=1, sticky="ew")
    
        # Итого
        itog = Label(tab, text='Физ износ: 0')
        itog.grid(row=0, column=4)
    
        # Кнопка рассчета
        Button(tab, text='Посчитать', width=10, command=lambda: self.calculate_iznos(
            marka.get(), model.get(), float(year.get()), float(probeg.get()), itog)).grid(row=5, column=1)

    def calculate_iznos(self, marka, model, year, probeg, itog):
        print("--- Физ износ ----")

        currentYear = datetime.now().year
        srok = currentYear - year
    
        # Find coeeficients
        info = get_a_b_L0_ML(marka)
        coeff_a_out = float(info["coeff_a"])
        coeff_b_out = float(info["coeff_b"])
        print(f"Коэфф a: {coeff_a_out}")
        print(f"Коэфф b: {coeff_b_out}")
    
        # Рассчет пробега если он 0
        if probeg == 0:
            Lo_out = float(info["Lo"])
            ML_out = float(info["ML"])
            print(f"Lo: {Lo_out}")
            print(f"ML: {ML_out}")
    
            probeg = Lo_out * (srok ** ML_out)
        print(f"Пробег: {probeg}")
    
        omega = (coeff_a_out * srok) + (coeff_b_out * probeg)
        print(f"Омега: {omega}")
    
        fiz_iznnos = 100 * (1 - (math.e ** (-1 * omega)))
        if fiz_iznnos > 75:
            fiz_iznnos = fiz_iznnos % 75
        print(f"Физ износ: {fiz_iznnos}")
        itog.configure(text=f"Физ износ: {fiz_iznnos}")

        arr = [marka, model, year, probeg, fiz_iznnos]
        data_to_excel(arr, self.wb, "Физ износ", self.header)
