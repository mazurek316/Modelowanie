import tkinter as tk
import numpy as np
from tkinter import messagebox


# konfiguracja okna
root = tk.Tk()
root.title('Dane wejściowe')
root.geometry("1150x400")
root.resizable(False, False)


# deklaracje zmiennych
# Słońce
masa_slonce = tk.DoubleVar(root, 1.9891)
masa_slonce_pot = tk.IntVar(root, 21)

# Merkury
masa_merkury = tk.DoubleVar(root, 3.302)
masa_merkury_pot = tk.IntVar(root, 14)
dyst_merkury = tk.DoubleVar(root, 5.79)
dyst_merkury_pot = tk.IntVar(root, 10)
predkosc_merkury = tk.DoubleVar(root, 4.7847)
predkosc_merkury_pot = tk.IntVar(root, 4)

# Wenus
masa_wenus = tk.DoubleVar(root, 4.8685)
masa_wenus_pot = tk.IntVar(root, 15)
dyst_wenus = tk.DoubleVar(root, 1.082)
dyst_wenus_pot = tk.IntVar(root, 11)
predkosc_wenus = tk.DoubleVar(root, 3.4971)
predkosc_wenus_pot = tk.IntVar(root, 4)

# Ziemia
masa_ziemia = tk.DoubleVar(root, 5.9742)
masa_ziemia_pot = tk.IntVar(root, 15)
dyst_ziemia = tk.DoubleVar(root, 1.496)
dyst_ziemia_pot = tk.IntVar(root, 11)
predkosc_ziemia = tk.DoubleVar(root, 2.9806)
predkosc_ziemia_pot = tk.IntVar(root, 4)

# Mars
masa_mars = tk.DoubleVar(root, 6.4185)
masa_mars_pot = tk.IntVar(root, 14)
dyst_mars = tk.DoubleVar(root, 2.279)
dyst_mars_pot = tk.IntVar(root, 11)
predkosc_mars = tk.DoubleVar(root, 2.4124)
predkosc_mars_pot = tk.IntVar(root, 4)

# Jowisz
masa_jowisz = tk.DoubleVar(root, 1.899)
masa_jowisz_pot = tk.IntVar(root, 18)
dyst_jowisz = tk.DoubleVar(root, 7.786)
dyst_jowisz_pot = tk.IntVar(root, 11)
predkosc_jowisz = tk.DoubleVar(root, 1.2927)
predkosc_jowisz_pot = tk.IntVar(root, 4)

# Saturn
masa_saturn = tk.DoubleVar(root, 5.6846)
masa_saturn_pot = tk.IntVar(root, 17)
dyst_saturn = tk.DoubleVar(root, 1.4335)
dyst_saturn_pot = tk.IntVar(root, 12)
predkosc_saturn = tk.DoubleVar(root, 9.8485)
predkosc_saturn_pot = tk.IntVar(root, 3)

# Uran
masa_uran = tk.DoubleVar(root, 8.6832)
masa_uran_pot = tk.IntVar(root, 16)
dyst_uran = tk.DoubleVar(root, 2.8725)
dyst_uran_pot = tk.IntVar(root, 12)
predkosc_uran = tk.DoubleVar(root, 6.8132)
predkosc_uran_pot = tk.IntVar(root, 3)

# Neptun
masa_neptun = tk.DoubleVar(root, 1.0243)
masa_neptun_pot = tk.IntVar(root, 17)
dyst_neptun = tk.DoubleVar(root, 4.4951)
dyst_neptun_pot = tk.IntVar(root, 12)
predkosc_neptun = tk.DoubleVar(root, 5.4278)
predkosc_neptun_pot = tk.IntVar(root,3)

# funkcje submit i walidacyjne
def zmienione_dane():
    masy_input = {'Slonce': masa_slonce.get(),
            'Merkury': masa_merkury.get(),
            'Wenus': masa_wenus.get(),
            'Ziemia': masa_ziemia.get(),
            'Mars': masa_mars.get(),
            'Jowisz': masa_jowisz.get(),
            'Saturn': masa_saturn.get(),
            'Uran': masa_uran.get(),
            'Neptun': masa_neptun.get()}

    masy_pot_input = {'Slonce': masa_slonce_pot.get(),
                  'Merkury': masa_merkury_pot.get(),
                  'Wenus': masa_wenus_pot.get(),
                  'Ziemia': masa_ziemia_pot.get(),
                  'Mars': masa_mars_pot.get(),
                  'Jowisz': masa_jowisz_pot.get(),
                  'Saturn': masa_saturn_pot.get(),
                  'Uran': masa_uran_pot.get(),
                  'Neptun': masa_neptun_pot.get()}

    dyst_input = {'Merkury': dyst_merkury.get(),
                  'Wenus': dyst_wenus.get(),
                  'Ziemia': dyst_ziemia.get(),
                  'Mars': dyst_mars.get(),
                  'Jowisz': dyst_jowisz.get(),
                  'Saturn': dyst_saturn.get(),
                  'Uran': dyst_uran.get(),
                  'Neptun': dyst_neptun.get()}

    dyst_pot_input = {'Merkury': dyst_merkury_pot.get(),
                  'Wenus': dyst_wenus_pot.get(),
                  'Ziemia': dyst_ziemia_pot.get(),
                  'Mars': dyst_mars_pot.get(),
                  'Jowisz': dyst_jowisz_pot.get(),
                  'Saturn': dyst_saturn_pot.get(),
                  'Uran': dyst_uran_pot.get(),
                  'Neptun': dyst_neptun_pot.get()}

    pred_input = {'Merkury': predkosc_merkury.get(),
                  'Wenus': predkosc_wenus.get(),
                  'Ziemia': predkosc_ziemia.get(),
                  'Mars': predkosc_mars.get(),
                  'Jowisz': predkosc_jowisz.get(),
                  'Saturn': predkosc_saturn.get(),
                  'Uran': predkosc_uran.get(),
                  'Neptun': predkosc_neptun.get()}

    pred_pot_input = {'Merkury': predkosc_merkury_pot.get(),
                  'Wenus': predkosc_wenus_pot.get(),
                  'Ziemia': predkosc_ziemia_pot.get(),
                  'Mars': predkosc_mars_pot.get(),
                  'Jowisz': predkosc_jowisz_pot.get(),
                  'Saturn': predkosc_saturn_pot.get(),
                  'Uran': predkosc_uran_pot.get(),
                  'Neptun': predkosc_neptun_pot.get()}

    return masy_input, masy_pot_input, dyst_input, dyst_pot_input, pred_input, pred_pot_input


def domyslne_dane():
    domyslne_masy = {'Slonce': 1.9891,
                     'Merkury': 3.302,
                     'Wenus': 4.8685,
                     'Ziemia': 5.9742,
                     'Mars': 6.4185,
                     'Jowisz': 1.899,
                     'Saturn': 5.6846,
                     'Uran': 8.6832,
                     'Neptun': 1.0243}

    domyslne_masy_pot = {'Slonce': 21,
                         'Merkury': 14,
                         'Wenus': 14,
                         'Ziemia': 15,
                         'Mars': 14,
                         'Jowisz': 18,
                         'Saturn': 17,
                         'Uran': 16,
                         'Neptun': 17}

    domyslne_dyst = {'Merkury': 5.79,
                     'Wenus': 1.082,
                     'Ziemia': 1.496,
                     'Mars': 2.279,
                     'Jowisz': 7.786,
                     'Saturn': 1.4335,
                     'Uran': 2.8725,
                     'Neptun': 4.4951}

    domyslne_dyst_pot = {'Merkury': 10,
                         'Wenus': 11,
                         'Ziemia': 11,
                         'Mars': 11,
                         'Jowisz': 11,
                         'Saturn': 12,
                         'Uran': 12,
                         'Neptun': 12}

    domyslne_pred = {'Merkury': 4.7847,
                     'Wenus': 3.4971,
                     'Ziemia': 2.9806,
                     'Mars': 2.4124,
                     'Jowisz': 1.2927,
                     'Saturn': 9.8485,
                     'Uran': 6.8132,
                     'Neptun': 5.4278}

    domyslne_pred_pot = {'Merkury': 4,
                         'Wenus': 4,
                         'Ziemia': 4,
                         'Mars': 4,
                         'Jowisz': 4,
                         'Saturn': 3,
                         'Uran': 3,
                         'Neptun': 3}

    return domyslne_masy, domyslne_masy_pot, domyslne_dyst, domyslne_dyst_pot, domyslne_pred, domyslne_pred_pot


def miedzy_0_1(inp):
    try:
        input = float(inp)
        if input > 0 and input < 10:
            return True
        else:
            return False
    except ValueError:
        return False


def miedzy_0_25(inp):
    try:
        input = int(inp)
        if input > 0 and input < 25:
            return True
        else:
            return False
    except ValueError:
        return False


def setflag():
    global flag
    flag = True
    root.destroy()


def jak_wprowadzac():
    tekst = "Wprowadź wartości w notacji wykładniczej, potęgi liczby 10 muszą być liczbami między 0 a 25"
    messagebox.showinfo(title="Jak wprowadzać", message=tekst)

# komendy sprawdzające wprowadzane wartości jako zapis podawany w Entry(validatecommand)
miedzy_0_1_cmd = root.register(miedzy_0_1)
miedzy_0_25_cmd = root.register(miedzy_0_25)

# etykiety
label_MASY = tk.Label(root, text='MASY CIAŁ [kg]', font=('calibre', 20, 'bold'))
label_ODLEGLOSC = tk.Label(root, text='DYSTANS DO SŁOŃCA [m]', font=('calibre', 20, 'bold'))
label_PREDKOSCI = tk.Label(root, text='PRĘDKOŚĆ STYCZNA [m/s]', font=('calibre', 20, 'bold'))
label_0 = tk.Label(root, text='Słońce', font=('calibre', 12, 'bold'))
label_1 = tk.Label(root, text='Merkury', font=('calibre', 12, 'bold'))
label_2 = tk.Label(root, text='Wenus', font=('calibre', 12, 'bold'))
label_3 = tk.Label(root, text='Ziemia', font=('calibre', 12, 'bold'))
label_4 = tk.Label(root, text='Mars', font=('calibre', 12, 'bold'))
label_5 = tk.Label(root, text='Jowisz', font=('calibre', 12, 'bold'))
label_6 = tk.Label(root, text='Saturn', font=('calibre', 12, 'bold'))
label_7 = tk.Label(root, text='Uran', font=('calibre', 12, 'bold'))
label_8 = tk.Label(root, text='Neptun', font=('calibre', 12, 'bold'))

# wejścia masy
masa_0_entry = tk.Entry(root, textvariable=masa_slonce, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
masa_1_entry = tk.Entry(root, textvariable=masa_merkury, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
masa_2_entry = tk.Entry(root, textvariable=masa_wenus, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
masa_3_entry = tk.Entry(root, textvariable=masa_ziemia, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
masa_4_entry = tk.Entry(root, textvariable=masa_mars, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
masa_5_entry = tk.Entry(root, textvariable=masa_jowisz, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
masa_6_entry = tk.Entry(root, textvariable=masa_saturn, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
masa_7_entry = tk.Entry(root, textvariable=masa_uran, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
masa_8_entry = tk.Entry(root, textvariable=masa_neptun, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)

# wejścia potęg mas
masa_0_pot_entry = tk.Entry(root, textvariable=masa_slonce_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
masa_1_pot_entry = tk.Entry(root, textvariable=masa_merkury_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
masa_2_pot_entry = tk.Entry(root, textvariable=masa_wenus_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
masa_3_pot_entry = tk.Entry(root, textvariable=masa_ziemia_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
masa_4_pot_entry = tk.Entry(root, textvariable=masa_mars_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
masa_5_pot_entry = tk.Entry(root, textvariable=masa_jowisz_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
masa_6_pot_entry = tk.Entry(root, textvariable=masa_saturn_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
masa_7_pot_entry = tk.Entry(root, textvariable=masa_uran_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
masa_8_pot_entry = tk.Entry(root, textvariable=masa_neptun_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)

# wejścia dystansów
dyst_1_entry = tk.Entry(root, textvariable=dyst_merkury, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
dyst_2_entry = tk.Entry(root, textvariable=dyst_wenus, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
dyst_3_entry = tk.Entry(root, textvariable=dyst_ziemia, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
dyst_4_entry = tk.Entry(root, textvariable=dyst_mars, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
dyst_5_entry = tk.Entry(root, textvariable=dyst_jowisz, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
dyst_6_entry = tk.Entry(root, textvariable=dyst_saturn, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
dyst_7_entry = tk.Entry(root, textvariable=dyst_uran, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
dyst_8_entry = tk.Entry(root, textvariable=dyst_neptun, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)

# wejścia potęg dystansów
dyst_1_pot_entry = tk.Entry(root, textvariable=dyst_merkury_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
dyst_2_pot_entry = tk.Entry(root, textvariable=dyst_wenus_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
dyst_3_pot_entry = tk.Entry(root, textvariable=dyst_ziemia_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
dyst_4_pot_entry = tk.Entry(root, textvariable=dyst_mars_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
dyst_5_pot_entry = tk.Entry(root, textvariable=dyst_jowisz_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
dyst_6_pot_entry = tk.Entry(root, textvariable=dyst_saturn_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
dyst_7_pot_entry = tk.Entry(root, textvariable=dyst_uran_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
dyst_8_pot_entry = tk.Entry(root, textvariable=dyst_neptun_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
# wejścia prędkości
pred_1_entry = tk.Entry(root, textvariable=predkosc_merkury, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
pred_2_entry = tk.Entry(root, textvariable=predkosc_wenus, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
pred_3_entry = tk.Entry(root, textvariable=predkosc_ziemia, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
pred_4_entry = tk.Entry(root, textvariable=predkosc_mars, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
pred_5_entry = tk.Entry(root, textvariable=predkosc_jowisz, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
pred_6_entry = tk.Entry(root, textvariable=predkosc_saturn, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
pred_7_entry = tk.Entry(root, textvariable=predkosc_uran, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
pred_8_entry = tk.Entry(root, textvariable=predkosc_neptun, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_1_cmd, '%P'), width=6)
# wejścia potęg prędkości
pred_1_pot_entry = tk.Entry(root, textvariable=predkosc_merkury_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
pred_2_pot_entry = tk.Entry(root, textvariable=predkosc_wenus_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
pred_3_pot_entry = tk.Entry(root, textvariable=predkosc_ziemia_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
pred_4_pot_entry = tk.Entry(root, textvariable=predkosc_mars_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
pred_5_pot_entry = tk.Entry(root, textvariable=predkosc_jowisz_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
pred_6_pot_entry = tk.Entry(root, textvariable=predkosc_saturn_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
pred_7_pot_entry = tk.Entry(root, textvariable=predkosc_uran_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)
pred_8_pot_entry = tk.Entry(root, textvariable=predkosc_neptun_pot, font=('calibre', 12, 'normal'),
                        validate="key", validatecommand=(miedzy_0_25_cmd, '%P'), width=6)

# PRZYCISKI - definicje

sub_btn = tk.Button(root, text='Zatwierdź', command=setflag)
def_btn = tk.Button(root, text='Uruchom z domyślnymi', command=root.destroy)
inf_btn = tk.Button(root, text='Jak wprowadzać', command=jak_wprowadzac)


# grid, dystrybucja elementów w oknie   #   #   #   #   # GRID  #   #   #

# nagłówki
label_MASY.grid(row=0, column=1, columnspan=3)
label_ODLEGLOSC.grid(row=0, column=5, columnspan=5)
label_PREDKOSCI.grid(row=0, column=11, columnspan=5)

# obiekty
# słońce
label_0.grid(row=1, column=0)                                               # nazwa
masa_0_entry.grid(row=1, column=1)                                          # wejście masy 1.91
label_0_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))          # e
label_0_e.grid(row=1, column=2)                                             # e grid
masa_0_pot_entry.grid(row=1, column=3)                                      # wejście masy e30


# merkury
label_1.grid(row=2, column=0)
masa_1_entry.grid(row=2, column=1)
label_1_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_1_e.grid(row=2, column=2)
masa_1_pot_entry.grid(row=2, column=3)

space_1_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_11_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)  # przestrzenie do grid
space_111_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_1111_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_11111_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)       # do prędkości
space_111111_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_1_.grid(row=2, column=4)
space_11_.grid(row=2, column=5)
space_111_.grid(row=2, column=9)
space_1111_.grid(row=2, column=10)

dyst_1_entry.grid(row=2, column=6)
label_11_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_11_e.grid(row=2, column=7)
dyst_1_pot_entry.grid(row=2, column=8)

pred_1_entry.grid(row=2, column=12)
label_111_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_111_e.grid(row=2, column=13)
pred_1_pot_entry.grid(row=2, column=14)
space_11111_.grid(row=2, column=11)
space_111111_.grid(row=2, column=15)


# wenus
label_2.grid(row=3, column=0)
masa_2_entry.grid(row=3, column=1)
label_2_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_2_e.grid(row=3, column=2)
masa_2_pot_entry.grid(row=3, column=3)

space_2_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_22_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)  # przestrzenie do grid
space_222_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_2222_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_22222_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)       # do prędkości
space_222222_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_2_.grid(row=3, column=4)
space_22_.grid(row=3, column=5)
space_222_.grid(row=3, column=9)
space_2222_.grid(row=3, column=10)

dyst_2_entry.grid(row=3, column=6)
label_22_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_22_e.grid(row=3, column=7)
dyst_2_pot_entry.grid(row=3, column=8)

pred_2_entry.grid(row=3, column=12)
label_222_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_222_e.grid(row=3, column=13)
pred_2_pot_entry.grid(row=3, column=14)
space_22222_.grid(row=3, column=11)
space_222222_.grid(row=3, column=15)


# ziemia
label_3.grid(row=4, column=0)
masa_3_entry.grid(row=4, column=1)
label_3_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_3_e.grid(row=4, column=2)
masa_3_pot_entry.grid(row=4, column=3)

space_3_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_33_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)  # przestrzenie do grid
space_333_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_3333_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_33333_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)       # do prędkości
space_333333_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_3_.grid(row=4, column=4)
space_33_.grid(row=4, column=5)
space_333_.grid(row=4, column=9)
space_3333_.grid(row=4, column=10)

dyst_3_entry.grid(row=4, column=6)
label_33_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_33_e.grid(row=4, column=7)
dyst_3_pot_entry.grid(row=4, column=8)

pred_3_entry.grid(row=4, column=12)
label_333_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_333_e.grid(row=4, column=13)
pred_3_pot_entry.grid(row=4, column=14)
space_33333_.grid(row=4, column=11)
space_333333_.grid(row=4, column=15)

# mars
label_4.grid(row=5, column=0)
masa_4_entry.grid(row=5, column=1)
label_4_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_4_e.grid(row=5, column=2)
masa_4_pot_entry.grid(row=5, column=3)

space_4_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_44_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)  # przestrzenie do grid
space_444_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_4444_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_44444_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)       # do prędkości
space_444444_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_4_.grid(row=5, column=4)
space_44_.grid(row=5, column=5)
space_444_.grid(row=5, column=9)
space_4444_.grid(row=5, column=10)

dyst_4_entry.grid(row=5, column=6)
label_44_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_44_e.grid(row=5, column=7)
dyst_4_pot_entry.grid(row=5, column=8)

pred_4_entry.grid(row=5, column=12)
label_444_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_444_e.grid(row=5, column=13)
pred_4_pot_entry.grid(row=5, column=14)
space_44444_.grid(row=5, column=11)
space_444444_.grid(row=5, column=15)

# jon bon jowisz
label_5.grid(row=6, column=0)
masa_5_entry.grid(row=6, column=1)
label_5_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_5_e.grid(row=6, column=2)
masa_5_pot_entry.grid(row=6, column=3)

space_5_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_55_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)  # przestrzenie do grid
space_555_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_5555_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_55555_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)       # do prędkości
space_555555_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_5_.grid(row=6, column=4)
space_55_.grid(row=6, column=5)
space_555_.grid(row=6, column=9)
space_5555_.grid(row=6, column=10)

dyst_5_entry.grid(row=6, column=6)
label_55_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_55_e.grid(row=6, column=7)
dyst_5_pot_entry.grid(row=6, column=8)

pred_5_entry.grid(row=6, column=12)
label_555_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_555_e.grid(row=6, column=13)
pred_5_pot_entry.grid(row=6, column=14)
space_55555_.grid(row=6, column=11)
space_555555_.grid(row=6, column=15)

# saturn
label_6.grid(row=7, column=0)
masa_6_entry.grid(row=7, column=1)
label_6_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_6_e.grid(row=7, column=2)
masa_6_pot_entry.grid(row=7, column=3)

space_6_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_66_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)  # przestrzenie do grid
space_666_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_6666_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_66666_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)       # do prędkości
space_666666_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_6_.grid(row=7, column=4)
space_66_.grid(row=7, column=5)
space_666_.grid(row=7, column=9)
space_6666_.grid(row=7, column=10)

dyst_6_entry.grid(row=7, column=6)
label_66_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_66_e.grid(row=7, column=7)
dyst_6_pot_entry.grid(row=7, column=8)

pred_6_entry.grid(row=7, column=12)
label_666_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_666_e.grid(row=7, column=13)
pred_6_pot_entry.grid(row=7, column=14)
space_66666_.grid(row=7, column=11)
space_666666_.grid(row=7, column=15)

# uran
label_7.grid(row=8, column=0)
masa_7_entry.grid(row=8, column=1)
label_7_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_7_e.grid(row=8, column=2)
masa_7_pot_entry.grid(row=8, column=3)

space_7_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_77_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)  # przestrzenie do grid
space_777_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_7777_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_77777_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)       # do prędkości
space_777777_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_7_.grid(row=8, column=4)
space_77_.grid(row=8, column=5)
space_777_.grid(row=8, column=9)
space_7777_.grid(row=8, column=10)

dyst_7_entry.grid(row=8, column=6)
label_77_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_77_e.grid(row=8, column=7)
dyst_7_pot_entry.grid(row=8, column=8)

pred_7_entry.grid(row=8, column=12)
label_777_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_777_e.grid(row=8, column=13)
pred_7_pot_entry.grid(row=8, column=14)
space_77777_.grid(row=8, column=11)
space_777777_.grid(row=8, column=15)

# neptun
label_8.grid(row=9, column=0)
masa_8_entry.grid(row=9, column=1)
label_8_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_8_e.grid(row=9, column=2)
masa_8_pot_entry.grid(row=9, column=3)

space_8_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_88_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)  # przestrzenie do grid
space_888_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_8888_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_88888_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)       # do prędkości
space_888888_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5)
space_8_.grid(row=9, column=4)
space_88_.grid(row=9, column=5)
space_888_.grid(row=9, column=9)
space_8888_.grid(row=9, column=10)

dyst_8_entry.grid(row=9, column=6)
label_88_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_88_e.grid(row=9, column=7)
dyst_8_pot_entry.grid(row=9, column=8)

pred_8_entry.grid(row=9, column=12)
label_888_e = tk.Label(root, text='e', font=('calibre', 12, 'bold'))
label_888_e.grid(row=9, column=13)
pred_8_pot_entry.grid(row=9, column=14)
space_88888_.grid(row=9, column=11)
space_888888_.grid(row=9, column=15)


# BATONY
space_btn_ = tk.Label(root, text='', font=('calibre', 12, 'bold'), width=5, height=2)
space_btn_.grid(row=10, column=6)
sub_btn.grid(row=11, column=6, columnspan=3)
def_btn.grid(row=11, column=9, columnspan=2)
inf_btn.grid(row=11, column=4, columnspan=3)


messagebox.showinfo(title="Jak wprowadzać", message="Wprowadź wartości w notacji wykładniczej, potęgi liczby 10 muszą być liczbami między 0 a 25")
masa_1_entry.focus_force()
root.mainloop()

# flag zdefiniowane będzie tylko po wciśnięciu "Zatwierdź"
try:
    if flag:
        masy_input, masy_pot_input, dyst_input, dyst_pot_input, pred_input, pred_pot_input = zmienione_dane()
except NameError:
    masy_input, masy_pot_input, dyst_input, dyst_pot_input, pred_input, pred_pot_input = domyslne_dane()
