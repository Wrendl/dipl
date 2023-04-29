import math
from bs4 import BeautifulSoup
import requests
import re
from tkinter import *
from tkinter.ttk import Combobox
from proj.data import print_models, get_marks_models, get_models


class Avg_cost:

    def __init__(self, tab2):
        self.tab = tab2
        self.cars = list(get_marks_models().keys())

        self.prices = []

        # Default
        self.miles = 0
        self.volume = 0
        self.year = 2023
        self.brand = ''
        self.model = ''
        self.fuel_type = 'Бензин'
        self.kpp_type = 'Автомат'
        self.sweel_type = 'Слева'
        self.privod_type = 'Передний'

        # kolesa, mycar, aster
        self.fuel = {'бензин': [1, 9],
                     'дизель': [2, 10],
                     'гибрид': [5, 11],
                     'электричество': [6, 12]}

        self.car_transm = {'механика': [1, 14, 'MT'],
                           'автомат': [2, 13, 'AVTOMAT']}

        self.sweel = {'слева': [1, 'false', 1],
                      'справа': [2, 'true', 2]}

        self.dwheel = {'передний': [1, 15, 'front'],
                       'полный': [2, 17, 'full'],
                       'задний': [3, 16, 'back']}

    def updtcblist(self, model, marka):
        model['values'] = print_models(marka.get())

    def start(self):
        # Выбор марки машин
        Label(self.tab, text='Марка').grid(row=0)
        marka = Combobox(self.tab)
        marka['values'] = self.cars
        marka.current(0)
        marka.grid(row=0, column=1)

        # модель
        Label(self.tab, text='Модель').grid(row=1)
        model = Combobox(self.tab, postcommand=lambda: self.updtcblist(model, marka))
        model.grid(row=1, column=1)

        # Год
        Label(self.tab, text='Год').grid(row=2)
        year = Entry(self.tab)
        year.insert(-1, "2023")
        year.grid(row=2, column=1)

        # Тип двигателя
        Label(self.tab, text='Тип двигателя').grid(row=3)
        fuel = Combobox(self.tab)
        fuel['values'] = list(self.fuel.keys())
        fuel.current(0)
        fuel.grid(row=3, column=1)

        # Коробка
        Label(self.tab, text='Коробка').grid(row=4)
        kpp = Combobox(self.tab)
        kpp['values'] = list(self.car_transm.keys())
        kpp.current(0)
        kpp.grid(row=4, column=1)

        Label(self.tab, text='Руль').grid(row=5)
        sweel = Combobox(self.tab)
        sweel['values'] = list(self.sweel.keys())
        sweel.current(0)
        sweel.grid(row=5, column=1)

        Label(self.tab, text='Привод').grid(row=6)
        dwheel = Combobox(self.tab)
        dwheel['values'] = list(self.dwheel.keys())
        dwheel.current(0)
        dwheel.grid(row=6, column=1)

        Label(self.tab, text='Объём').grid(row=7)
        volume = Entry(self.tab)
        volume.insert(-1, "0")
        volume.grid(row=7, column=1)

        Label(self.tab, text='Пробег до').grid(row=8)
        miles = Entry(self.tab)
        miles.insert(-1, "0")
        miles.grid(row=8, column=1)

        # Итого
        itog = Label(self.tab, text='Ср. стоимость ТС: 0')
        itog.grid(row=9)

        # Кнопка рассчета
        Button(self.tab, text='Посчитать', width=10, command=lambda: self.calculate_avg_cost(
            float(miles.get()),
            float(volume.get()),
            float(year.get()),
            marka.get(),
            model.get(),
            fuel.get(),
            kpp.get(),
            sweel.get(),
            dwheel.get()
        )).grid(row=10, column=1)

    def calculate_avg_cost(self, miles, volume, year, marka, model, fuel, kpp, sweel, dwheel):
        self.miles = miles
        self.volume = volume
        self.year = year
        self.brand = marka
        self.model = model.split(',')[0]
        self.fuel_type = fuel
        self.kpp_type = kpp
        self.sweel_type = sweel
        self.privod_type = dwheel

        self.kolesa()
        self.mycar()
        self.aster()
        print(self.model)
        print(self.prices)

    def kolesa(self):

        try:
            host = f'https://kolesa.kz/cars/{self.brand.lower()}/{self.model.lower()}/?auto-fuel={self.fuel[self.fuel_type.lower()][0]}&auto-car-transm={self.car_transm[self.kpp_type.lower()][0]}&auto-sweel={self.sweel[self.sweel_type.lower()][0]}&car-dwheel={self.dwheel[self.privod_type.lower()][0]}&auto-run[to]={self.miles}&auto-car-volume[from]={self.volume}&auto-car-volume[to]={self.volume}&year[from]={self.year}&year[to]={self.year}'
            response = requests.get(host)
            soup = BeautifulSoup(response.text, 'html.parser')

            items_soup = soup.find_all(class_='a-card__info')

            for item in items_soup:
                item_price = re.sub("[^0-9]", "", item.find('span', class_='a-card__price').text)
                self.prices.append(int(item_price))

        except ConnectionError:
            print()

    def mycar(self):

        host = f'https://mycar.kz/cars/{self.brand.lower()}/{self.model.lower()}?yearFrom={self.year}&yearTo={self.year}&engineVolumeFrom={self.volume}&engineVolumeTo={self.volume}&gearboxes={self.car_transm[self.kpp_type.lower()][1]}&engines={self.fuel[self.fuel_type.lower()][1]}&drives={self.dwheel[self.privod_type.lower()][1]}&rightHand={self.sweel[self.sweel_type.lower()][1]}&mileage={self.miles}'
        response = requests.get(host)
        soup = BeautifulSoup(response.text, 'html.parser')

        items_soup = soup.find_all(
            class_='car-card relative w-full h-full flex flex-col rounded-2xl bg-papera border-1 border-solid border-inko-10')
        for item in items_soup:
            item_price = int(re.sub("[^0-9]", "", item.find('h6', class_='text-h6 font-bold text-inko-100').text))
            self.prices.append(item_price)

    def aster(self):

        host = f'https://aster.kz/cars/{self.brand.lower()}/{self.model.lower()}?yearFrom={self.year}&yearTo={self.year}&transmission={self.car_transm[self.kpp_type.lower()][2]}&transmissionDriveType={self.dwheel[self.privod_type.lower()][2]}&mileageTo={self.miles}&volumeFrom={self.volume}&volumeTo={self.volume}&steering={self.sweel[self.sweel_type.lower()][2]}'

        request = requests.get(host)
        soup = BeautifulSoup(request.text, 'html.parser')

        items_soup = soup.find_all(class_='car fadeIn')
        for item in items_soup:
            # print(item.find('a', class_='price fw-700 f-18 car-link').text)
            try:
                item_price = re.sub("[^0-9]", "", item.find('a', class_='px-3 pt-1 price fw-700 f-18 car-link').text)
                self.prices.append(int(item_price))
            except:
                continue
