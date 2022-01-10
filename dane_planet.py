import numpy as np
from scipy.constants import pi

masy = {'Slonce': 1.9891 * np.power(10, 21, dtype='float64'),
        'Merkury': 3.302 * np.power(10, 14, dtype='float64'),
        'Wenus': 4.8685 * np.power(10, 15, dtype='float64'),
        'Ziemia': 5.9742 * np.power(10, 15, dtype='float64'),
        'Mars': 6.4185 * np.power(10, 14, dtype='float64'),
        'Jowisz': 1.899 * np.power(10, 18, dtype='float64'),
        'Saturn': 5.6846 * np.power(10, 17, dtype='float64'),
        'Uran': 8.6832 * np.power(10, 16, dtype='float64'),
        'Neptun': 1.02430 * np.power(10, 17, dtype='float64')}

dystanse = {'Merkury': 5.79 * np.power(10, 10, dtype='float64'),
            'Wenus': 1.082 * np.power(10, 11, dtype='float64'),
            'Ziemia': 1.496 * np.power(10, 11, dtype='float64'),
            'Mars': 2.279 * np.power(10, 11, dtype='float64'),
            'Jowisz': 7.786 * np.power(10, 11, dtype='float64'),
            'Saturn': 1.4335 * np.power(10, 13, dtype='float64'),
            'Uran': 2.8725 * np.power(10, 13, dtype='float64'),
            'Neptun': 4.4951 * np.power(10, 13, dtype='float64')}

dni_na_sekundy = 24 * 60 * 60
okresy_obr = {'Merkury': 88 * dni_na_sekundy,
              'Wenus': 225 * dni_na_sekundy,
              'Ziemia': 365 * dni_na_sekundy,
              'Mars': 687 * dni_na_sekundy,
              'Jowisz': 4380 * dni_na_sekundy,
              'Saturn': 10585 * dni_na_sekundy,
              'Uran': 30660 * dni_na_sekundy,
              'Neptun': 60225 * dni_na_sekundy}

predkosci = {'Merkury': 2 * pi * dystanse['Merkury'] / okresy_obr['Merkury'],
              'Wenus': 2 * pi * dystanse['Wenus'] / okresy_obr['Wenus'],
              'Ziemia': 2 * pi * dystanse['Ziemia'] / okresy_obr['Ziemia'],
              'Mars': 2 * pi * dystanse['Mars'] / okresy_obr['Mars'],
              'Jowisz': 2 * pi * dystanse['Jowisz'] / okresy_obr['Jowisz'],
              'Saturn': 2 * pi * dystanse['Saturn'] / okresy_obr['Saturn'],
              'Uran': 2 * pi * dystanse['Uran'] / okresy_obr['Uran'],
              'Neptun': 2 * pi * dystanse['Neptun'] / okresy_obr['Neptun']}

ped = {'Merkury': np.array([0, predkosci['Merkury'] * masy['Merkury'], 0]),
              'Wenus': np.array([0, predkosci['Wenus'] * masy['Wenus'], 0]),
              'Ziemia': np.array([0, predkosci['Ziemia'] * masy['Ziemia'], 0]),
              'Mars': np.array([0, predkosci['Mars'] * masy['Mars'], 0]),
              'Jowisz': np.array([0, predkosci['Jowisz'] * masy['Jowisz'], 0]),
              'Saturn': np.array([0, predkosci['Saturn'] * masy['Saturn'], 0]),
              'Uran': np.array([0, predkosci['Saturn'] * masy['Saturn'], 0]),
              'Neptun': np.array([0, predkosci['Neptun'] * masy['Neptun'], 0])}

#       #       #           #           #
#       #       #           #           #
"""
dt = 0.0001

# merkury
ped_merkury = dane_planet.ped['Merkury']
x_merkury = 57.9
y_merkury = 0

# wenus
ped_wenus = dane_planet.ped['Wenus']
x_wenus = 108.2
y_wenus = 0

# ziemia
ped_ziemi = dane_planet.ped['Ziemia']
x_ziemi = 149.6
y_ziemi = 0

# mars
ped_mars = dane_planet.ped['Mars']
x_mars = 227.9
y_mars = 0

# jowisz
ped_jowisz = dane_planet.ped['Jowisz']
x_jowisz = 778.6
y_jowisz = 0

# saturn
ped_saturn = dane_planet.ped['Saturn']
x_saturn = 1433.5
y_saturn = 0

# uran
ped_uran = dane_planet.ped['Uran']
x_uran = 2872.5
y_uran = 0

# neptun
ped_neptun = dane_planet.ped['Neptun']
x_neptun = 4495.1
y_neptun = 0

#       #       #           #           #
for i in range(0, 200):
    time = i * 2

    # merkury
    merkury_tmp = Planeta("Merkury", promien[1], x_merkury, '#87877d', 3.302 * np.power(10, 14, dtype='float64'), y_merkury)
    wektor_sily_merkury = sila_grawitacji(merkury_tmp, Slonce_obliczeniowe, x_merkury, y_merkury, 0, 0)
    ped_merkury = ped_merkury + wektor_sily_merkury * dt
    x_merkury = x_merkury + (ped_merkury[0] / merkury_tmp.masa) * dt
    y_merkury = y_merkury + (ped_merkury[1] / merkury_tmp.masa) * dt

    # wenus
    wenus_tmp = Planeta("Wenus", promien[2], x_wenus, '#d23100', 4.8685 * np.power(10, 15, dtype='float64'), y_wenus)
    wektor_sily_wenus = sila_grawitacji(wenus_tmp, Slonce_obliczeniowe, x_wenus, y_wenus, 0, 0)
    ped_wenus = ped_wenus + wektor_sily_wenus * dt
    x_wenus = x_wenus + (ped_wenus[0] / wenus_tmp.masa) * dt
    y_wenus = y_wenus + (ped_wenus[1] / wenus_tmp.masa) * dt

    # ziemia
    ziemia_tmp = Planeta("Ziemia", promien[3], x_ziemi, kolory_planet[3], 5.9742 * np.power(10, 15, dtype='float64'), y_ziemi)
    wektor_sily_ziemi = sila_grawitacji(ziemia_tmp, Slonce_obliczeniowe, x_ziemi, y_ziemi, 0, 0)
    ped_ziemi = ped_ziemi + wektor_sily_ziemi * dt
    x_ziemi = x_ziemi + (ped_ziemi[0] / ziemia_tmp.masa) * dt
    y_ziemi = y_ziemi + (ped_ziemi[1] / ziemia_tmp.masa) * dt

    # mars
    mars_tmp = Planeta("Mars", promien[4], x_mars, kolory_planet[4], 6.4185 * np.power(10, 14, dtype='float64'), y_mars)
    wektor_sily_mars = sila_grawitacji(mars_tmp, Slonce_obliczeniowe, x_mars, y_mars, 0, 0)
    ped_mars = ped_mars + wektor_sily_mars * dt
    x_mars = x_mars + (ped_mars[0] / mars_tmp.masa) * dt
    y_mars = y_mars + (ped_mars[1] / mars_tmp.masa) * dt

    # jowisz
    jowisz_tmp = Planeta("Jowisz", promien[5], x_jowisz, kolory_planet[5], 1.899 * np.power(10, 18, dtype='float64'), y_jowisz)
    wektor_sily_jowisz = sila_grawitacji(jowisz_tmp, Slonce_obliczeniowe, x_jowisz, y_jowisz, 0, 0)
    ped_jowisz = ped_jowisz + wektor_sily_jowisz * dt
    x_jowisz = x_jowisz + (ped_jowisz[0] / jowisz_tmp.masa) * dt
    y_jowisz = y_jowisz + (ped_jowisz[1] / jowisz_tmp.masa) * dt

    # saturn
    saturn_tmp = Planeta("Saturn", promien[6], x_saturn, kolory_planet[6], 5.6846 * np.power(10, 17, dtype='float64'), y_saturn)
    wektor_sily_saturn = sila_grawitacji(saturn_tmp, Slonce_obliczeniowe, x_saturn, y_saturn, 0, 0)
    ped_saturn = ped_saturn + wektor_sily_saturn * dt
    x_saturn = x_saturn + (ped_saturn[0] / saturn_tmp.masa) * dt
    y_saturn = y_saturn + (ped_saturn[1] / saturn_tmp.masa) * dt

    # uran
    uran_tmp = Planeta("Uran", promien[7], x_uran, kolory_planet[7], 8.6832 * np.power(10, 16, dtype='float64'), y_uran)
    wektor_sily_uran = sila_grawitacji(uran_tmp, Slonce_obliczeniowe, x_uran, y_uran, 0, 0)
    ped_uran = ped_uran + wektor_sily_uran * dt
    x_uran = x_uran + (ped_uran[0] / uran_tmp.masa) * dt
    y_uran = y_uran + (ped_uran[1] / uran_tmp.masa) * dt

    # neptun
    neptun_tmp = Planeta("Neptun", promien[8], x_neptun, kolory_planet[8], 1.02430 * np.power(10, 17, dtype='float64'), y_neptun)
    wektor_sily_neptun = sila_grawitacji(neptun_tmp, Slonce_obliczeniowe, x_neptun, y_neptun, 0, 0)
    ped_neptun = ped_neptun + wektor_sily_neptun * dt
    x_neptun = x_neptun + (ped_neptun[0] / neptun_tmp.masa) * dt
    y_neptun = y_neptun + (ped_neptun[1] / neptun_tmp.masa) * dt
"""