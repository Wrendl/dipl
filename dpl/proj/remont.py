import math
from tkinter import *
from tkinter.ttk import Combobox
from proj.data import coeff_a, coeff_b, Lo, ML, get_marks_models, print_models, get_a_b_L0_ML

cars = list(get_marks_models().keys())


def updtcblist(model, marka):
    model['values'] = print_models(marka.get())


def calculate(tab3):
    pass


def remont_tab(tab3):
    Label(tab3, text='Марка').grid(row=1, column=0)
    Label(tab3, text='Модель').grid(row=2, column=0)
    Label(tab3, text='Год').grid(row=3, column=0)
    Label(tab3, text='Часть').grid(row=4, column=0)
    Label(tab3, text='Деталь').grid(row=5, column=0)
    Label(tab3, text='Площадь').grid(row=6, column=0)
    Label(tab3, text='Вид работы').grid(row=7, column=0)
    Label(tab3, text='Время').grid(row=8, column=0)
    Label(tab3, text='Норм часы').grid(row=9, column=0)

    marka = Combobox(tab3)
    marka['values'] = cars
    marka.current(0)
    marka.grid(row=1, column=1)

    # Выбор модель машины
    model = Combobox(tab3)
    model = Combobox(tab3, postcommand=lambda: updtcblist(model, marka))
    model.grid(row=2, column=1)

    year = Entry(tab3)
    year.insert(-1, "0")
    year.grid(row=3, column=1)

    detail_v2 = Combobox(tab3)
    detail_v2['values'] = ['Передняя часть', 'Средняя часть', 'Задняя часть']
    detail_v2.current(0)
    detail_v2.grid(row=4, column=1)

    detail_v3 = Combobox(tab3)
    detail_v3['values'] = ['Поперечина передка (рамки радиатора) нижняя', 'Брызговик облицовки радиатора съемный',
                           'Брызговик облицовки радиатора несъемный', 'Крыло съемное', 'Крыло не съемное',
                           'Брызговик переднего крыла без лонжерона (в т.ч. в сборе с верхними усилителями)',
                           'Лонжерон передний без брызговика крыла', 'Щит передка (в т.ч. в сборе с надставкой)',
                           'Надставка щита передка', 'Короб воздухопритока', 'Панель рамы ветрового окна',
                           'Нижняя часть панели рамы ветрового окна']
    detail_v3.current(0)
    detail_v3.grid(row=5, column=1)

    plowad = Entry(tab3)
    plowad.insert(-1, "0")
    plowad.grid(row=6, column=1)

    vid = Combobox(tab3)
    vid['values'] = ['Молярные', 'Снятие/Установка', 'Разборка/Сборка', 'Замена']
    vid.current(0)
    vid.grid(row=7, column=1)

    vremya = Entry(tab3)
    vremya.insert(-1, "0")
    vremya.grid(row=8, column=1)

    norm_chas = Entry(tab3)
    norm_chas.insert(-1, "0")
    norm_chas.grid(row=9, column=1)

    Button(tab3, text='Посчитать', width=15, command=lambda: calculate(tab3)).grid(row=10, column=1)
