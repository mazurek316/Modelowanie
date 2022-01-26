
import plotly.graph_objects as go
import numpy as np
import math
import plotly.io as pio
import scipy.constants
import dane_planet


class Planeta:
    def __init__(self,nazwa,rozmiar,odleglosc,kolor, masa, przesuniecie_y = 0):
        self.nazwa = nazwa
        self.rozmiar = rozmiar
        self.odleglosc_od_slonca = odleglosc
        self.kolory = kolor
        self.zmianay = przesuniecie_y
        self.srodek_x = odleglosc
        self.srodek_y = 0
        self.masa = masa
    def Generacja_Planety(self):
        phi = np.linspace(0, 2 * np.pi, 15)
        theta = np.linspace(0, np.pi, 15)
        self.x_cords = self.odleglosc_od_slonca + self.rozmiar * np.outer(np.cos(phi), np.sin(theta)) # macierz współrzędnych x
        self.y_cords = self.rozmiar * np.outer(np.sin(phi), np.sin(theta)) + self.zmianay  # macierz współrzędnych y
        self.z_cords = 3+ self.rozmiar * np.outer(np.ones(15), np.cos(theta))
        Planeta = go.Surface(x=self.x_cords, y=self.y_cords, z=self.z_cords, colorscale=[[0, self.kolory], [1, self.kolory]])
        Planeta.update(showscale=False)
        return Planeta

    def Generacja_Orbity(self,offset = 1,clr = 'black',wdth = 0.5):
        xcord = []
        ycord = []
        zcord = []
        ped_ziemi = np.array([0, 1.78e20, 0])
        dt = 0.0001
        x_ziemi = 149
        y_ziemi = 0
        erth_tmp = Planeta("Ziemia", promien[3], x_ziemi, "#10f2c3", 5.9742 * np.power(10, 15, dtype='float64'), y_ziemi)
        # Obliczanie koordynatow
        if self.nazwa == "Ziemia":
            for i in range(0, 361):  # dla każdego stopnia
                wektor_sily_ziemi = sila_grawitacji(erth_tmp, Slonce_obliczeniowe, x_ziemi, y_ziemi, 0, 0)

                ped_ziemi = ped_ziemi + wektor_sily_ziemi * dt
                x_ziemi = x_ziemi + (ped_ziemi[0] / erth_tmp.masa) * dt
                y_ziemi = y_ziemi + (ped_ziemi[1] / erth_tmp.masa) * dt
                xcord = xcord + [x_ziemi]
                ycord = ycord + [y_ziemi]
                zcord = zcord + [3]

            orbita = go.Scatter3d(x=xcord, y=ycord, z=zcord, marker=dict(size=0.1), line=dict(color=clr, width=wdth))
            return orbita
        for i in range(0, 361):  # dla każdego stopnia
            wektor_sily_ziemi = sila_grawitacji(erth_tmp, Slonce_obliczeniowe, x_ziemi, y_ziemi, 0, 0)

            ped_ziemi = ped_ziemi + wektor_sily_ziemi * dt
            x_ziemi = x_ziemi + (ped_ziemi[0] / erth_tmp.masa) * dt
            y_ziemi = y_ziemi + (ped_ziemi[1] / erth_tmp.masa) * dt
            xcord = xcord + [(round(np.cos(math.radians(i)), 5)) * self.odleglosc_od_slonca + offset]
            ycord = ycord + [(round(np.sin(math.radians(i)), 5)) * self.odleglosc_od_slonca]
            zcord = zcord + [3]

        orbita = go.Scatter3d(x=xcord, y=ycord, z=zcord, marker=dict(size=0.1), line=dict(color=clr, width=wdth))
        return orbita

    def PlanetTrail(self,x_cords,y_cords,offset = 0,colour = 'black',wdth = 0.5,iteracje=3):
        z_cords = [3 for z in range(iteracje)]
        Trail = go.Scatter3d(x=x_cords,y=y_cords,z=z_cords,marker=dict(size=0.2),line=dict(color = colour,width = wdth))
        return Trail


def sila_grawitacji(cialo_1, cialo_2, x_1, y_1, x_2, y_2):
    G = scipy.constants.gravitational_constant

    poz_1 = np.array([x_1, y_1, 0])
    poz_2 = np.array([x_2, y_2, 0])
    wektor = poz_1 - poz_2                                          # między ciałami
    wektor_mag = np.linalg.norm(wektor)                     # absolute(x)
    wersor = wektor / wektor_mag

    sila_mag = G * cialo_1.masa * cialo_2.masa / np.power(wektor_mag, 2, dtype="float64")
    sila_wektor = -sila_mag * wersor

    return sila_wektor


promien_km = [200000, 4878, 12104, 12756, 6787, 142796, 120660, 51118, 48600, 1737]
promien = [((i / 12756)*2) for i in promien_km]
odleglosc_od_slonca = [0,57.9,108.2,149.6,227.9,778.6,1433.5,2872.5,4495.1]
kolory_planet = ['#ffff00','#87877d','#d23100','#10f2c3','#b20000','#ebebd2','#ebcd82','#37ffda','#2500ab']

Slonce = Planeta("Słońce",promien[0],odleglosc_od_slonca[0],kolory_planet[0], dane_planet.masy['Slonce'], 0).Generacja_Planety()
Slonce_obliczeniowe = Planeta("Słońce",promien[0],odleglosc_od_slonca[0],kolory_planet[0], dane_planet.masy['Slonce'], 0)
Merkury = Planeta("Merkury",promien[1],odleglosc_od_slonca[1],kolory_planet[1], dane_planet.masy['Merkury'], 0)
Wenus = Planeta("Wenus",promien[2],odleglosc_od_slonca[2],kolory_planet[2], dane_planet.masy['Wenus'], 0)
Ziemia = Planeta("Ziemia",promien[3],odleglosc_od_slonca[3],kolory_planet[3], dane_planet.masy['Ziemia'], 0)
Mars = Planeta("Mars",promien[4],odleglosc_od_slonca[4],kolory_planet[4], dane_planet.masy['Mars'], 0)
Jowisz = Planeta("Jowisz",promien[5],odleglosc_od_slonca[5],kolory_planet[5], dane_planet.masy['Jowisz'], 0)
Saturn = Planeta("Saturn",promien[6],odleglosc_od_slonca[6],kolory_planet[6], dane_planet.masy['Saturn'], 0)
Uran = Planeta("Uran",promien[7],odleglosc_od_slonca[7],kolory_planet[7], dane_planet.masy['Uran'], 0)
Neptun = Planeta("Neptun",promien[8],odleglosc_od_slonca[8],kolory_planet[8], dane_planet.masy['Neptun'], 0)

zmiany_pozycji = {"Merkury":[],"Wenus":[],"Ziemia":[],"Mars":[],"Jowisz":[],"Saturn":[],"Uran":[],"Neptun":[],'Ziemia_trail':[],"Merkury_trail":[],"Wenus_trail":[],"Mars_trail":[],"Jowisz_trail":[],"Saturn_trail":[],"Uran_trail":[],"Neptun_trail":[]}

#       #       #           #           #
Trail_cords = {"Merkury":[[],[]],"Wenus":[[],[]],"Ziemia":[[],[]],"Mars":[[],[]],"Jowisz":[[],[]],"Saturn":[[],[]],"Uran":[[],[]],"Neptun":[[],[]]}
#       #       #           #           #       sekcja fizyczna, wartości wejściowe
dt = 0.0001

# merkury
ped_merkury = dane_planet.ped['Merkury']
x_merkury = dane_planet.x_merkury
y_merkury = 0

# wenus
ped_wenus = dane_planet.ped['Wenus']
x_wenus = dane_planet.x_wenus
y_wenus = 0

# ziemia
ped_ziemi = dane_planet.ped['Ziemia']
x_ziemi = dane_planet.x_ziemi
y_ziemi = 0

# mars
ped_mars = dane_planet.ped['Mars']
x_mars = dane_planet.x_mars
y_mars = 0

# jowisz
ped_jowisz = dane_planet.ped['Jowisz']
x_jowisz = dane_planet.x_jowisz
y_jowisz = 0

# saturn
ped_saturn = dane_planet.ped['Saturn']
x_saturn = dane_planet.x_saturn
y_saturn = 0

# uran
ped_uran = dane_planet.ped['Uran']
x_uran = dane_planet.x_uran
y_uran = 0

# neptun
ped_neptun = dane_planet.ped['Neptun']
x_neptun = dane_planet.x_neptun
y_neptun = 0

x_slonca = 0
y_slonca = 0
#       #       #           #           #

#       #       #           #           #       #       #       #       sekcja fizyczna, inicjatory planet do sił między planetami
merkury_tmp = Planeta("Merkury", promien[1], x_merkury, kolory_planet[1], dane_planet.masy['Merkury'], y_merkury)
wenus_tmp = Planeta("Wenus", promien[2], x_wenus, kolory_planet[2], dane_planet.masy['Wenus'], y_wenus)
ziemia_tmp = Planeta("Ziemia", promien[3], x_ziemi, kolory_planet[3], dane_planet.masy['Ziemia'], y_ziemi)
mars_tmp = Planeta("Mars", promien[4], x_mars, kolory_planet[4], dane_planet.masy['Mars'], y_mars)
jowisz_tmp = Planeta("Jowisz", promien[5], x_jowisz, kolory_planet[5], dane_planet.masy['Jowisz'], y_jowisz)
saturn_tmp = Planeta("Saturn", promien[6], x_saturn, kolory_planet[6], dane_planet.masy['Saturn'], y_saturn)
uran_tmp = Planeta("Uran", promien[7], x_uran, kolory_planet[7], dane_planet.masy['Uran'], y_uran)
neptun_tmp = Planeta("Neptun", promien[8], x_neptun, kolory_planet[8], dane_planet.masy['Neptun'], y_neptun)
#       #       #           #           #       #       #       #       sekcja fizyczna, iteracje obliczeń sił, dodawania klatek do animacji
for i in range(0, 200):
    # merkury
    merkury_do_slonca = np.linalg.norm([x_merkury, y_merkury, 0])
    if merkury_do_slonca > 30:
        merkury_tmp = Planeta("Merkury", promien[1], x_merkury, kolory_planet[1], dane_planet.masy['Merkury'], y_merkury)
        wektor_sily_merkury = sila_grawitacji(merkury_tmp, Slonce_obliczeniowe, x_merkury, y_merkury, x_slonca, y_slonca) + sila_grawitacji(merkury_tmp, wenus_tmp, x_merkury, y_merkury, x_wenus, y_wenus)
        ped_merkury = ped_merkury + wektor_sily_merkury * dt
        x_merkury = x_merkury + (ped_merkury[0] / merkury_tmp.masa) * dt
        y_merkury = y_merkury + (ped_merkury[1] / merkury_tmp.masa) * dt
    else:
        merkury_tmp = Planeta("Merkury", 0, x_merkury, '#87877d', 0, y_merkury)

    # wenus
    wenus_do_slonca = np.linalg.norm([x_wenus, y_wenus, 0])
    if wenus_do_slonca > 30:
        wenus_tmp = Planeta("Wenus", promien[2], x_wenus, kolory_planet[2], dane_planet.masy['Wenus'], y_wenus)
        wektor_sily_wenus = sila_grawitacji(wenus_tmp, Slonce_obliczeniowe, x_wenus, y_wenus, x_slonca, y_slonca) + sila_grawitacji(wenus_tmp, merkury_tmp, x_wenus, y_wenus, x_merkury, y_merkury) + sila_grawitacji(wenus_tmp, ziemia_tmp, x_wenus, y_wenus, x_ziemi, y_ziemi)
        ped_wenus = ped_wenus + wektor_sily_wenus * dt
        x_wenus = x_wenus + (ped_wenus[0] / wenus_tmp.masa) * dt
        y_wenus = y_wenus + (ped_wenus[1] / wenus_tmp.masa) * dt
    else:
        wenus_tmp = Planeta("Wenus", 0, x_wenus, '#d23100', 0, y_wenus)

    # ziemia
    ziemia_do_slonca = np.linalg.norm([x_ziemi, y_ziemi, 0])
    if ziemia_do_slonca > 30:
        ziemia_tmp = Planeta("Ziemia", promien[3], x_ziemi, kolory_planet[3], dane_planet.masy['Ziemia'], y_ziemi)
        wektor_sily_ziemi = sila_grawitacji(ziemia_tmp, Slonce_obliczeniowe, x_ziemi, y_ziemi, x_slonca, y_slonca) + sila_grawitacji(ziemia_tmp, wenus_tmp, x_ziemi, y_ziemi, x_wenus, y_wenus) + sila_grawitacji(ziemia_tmp, mars_tmp, x_ziemi, y_ziemi, x_mars, y_mars)
        ped_ziemi = ped_ziemi + wektor_sily_ziemi * dt
        x_ziemi = x_ziemi + (ped_ziemi[0] / ziemia_tmp.masa) * dt
        y_ziemi = y_ziemi + (ped_ziemi[1] / ziemia_tmp.masa) * dt
    else:
        ziemia_tmp = Planeta("Ziemia", 0, x_ziemi, kolory_planet[3], 0, y_ziemi)

    # mars
    mars_do_slonca = np.linalg.norm([x_mars, y_mars, 0])
    if mars_do_slonca > 30:
        mars_tmp = Planeta("Mars", promien[4], x_mars, kolory_planet[4], dane_planet.masy['Mars'], y_mars)
        wektor_sily_mars = sila_grawitacji(mars_tmp, Slonce_obliczeniowe, x_mars, y_mars, x_slonca, y_slonca) + sila_grawitacji(mars_tmp, ziemia_tmp, x_mars, y_mars, x_ziemi, y_ziemi) + sila_grawitacji(mars_tmp, jowisz_tmp, x_mars, y_mars, x_jowisz, y_jowisz)
        ped_mars = ped_mars + wektor_sily_mars * dt
        x_mars = x_mars + (ped_mars[0] / mars_tmp.masa) * dt
        y_mars = y_mars + (ped_mars[1] / mars_tmp.masa) * dt
    else:
        mars_tmp = Planeta("Mars", 0, x_mars, kolory_planet[4], 0, y_mars)

    # jowisz
    jowisz_do_slonca = np.linalg.norm([x_jowisz, y_jowisz, 0])
    if jowisz_do_slonca > 30:
        jowisz_tmp = Planeta("Jowisz", promien[5], x_jowisz, kolory_planet[5], dane_planet.masy['Jowisz'], y_jowisz)
        wektor_sily_jowisz = sila_grawitacji(jowisz_tmp, Slonce_obliczeniowe, x_jowisz, y_jowisz, x_slonca, y_slonca) + sila_grawitacji(jowisz_tmp, mars_tmp, x_jowisz, y_jowisz, x_mars, y_mars) + sila_grawitacji(jowisz_tmp, saturn_tmp, x_jowisz, y_jowisz, x_saturn, y_saturn)
        ped_jowisz = ped_jowisz + wektor_sily_jowisz * dt
        x_jowisz = x_jowisz + (ped_jowisz[0] / jowisz_tmp.masa) * dt
        y_jowisz = y_jowisz + (ped_jowisz[1] / jowisz_tmp.masa) * dt
    else:
        jowisz_tmp = Planeta("Jowisz", 0, x_jowisz, kolory_planet[5], 0, y_jowisz)

    # saturn
    saturn_do_slonca = np.linalg.norm([x_saturn, y_saturn, 0])
    if saturn_do_slonca > 30:
        saturn_tmp = Planeta("Saturn", promien[6], x_saturn, kolory_planet[6], dane_planet.masy['Saturn'], y_saturn)
        wektor_sily_saturn = sila_grawitacji(saturn_tmp, Slonce_obliczeniowe, x_saturn, y_saturn, x_slonca, y_slonca) + sila_grawitacji(saturn_tmp, jowisz_tmp, x_saturn, y_saturn, x_jowisz, y_jowisz) + sila_grawitacji(saturn_tmp, uran_tmp, x_saturn, y_saturn, x_uran, y_uran)
        ped_saturn = ped_saturn + wektor_sily_saturn * dt
        x_saturn = x_saturn + (ped_saturn[0] / saturn_tmp.masa) * dt
        y_saturn = y_saturn + (ped_saturn[1] / saturn_tmp.masa) * dt
    else:
        saturn_tmp = Planeta("Saturn", 0, x_saturn, kolory_planet[6], 0, y_saturn)

    # uran
    uran_do_slonca = np.linalg.norm([x_uran, y_uran, 0])
    if uran_do_slonca > 30:
        uran_tmp = Planeta("Uran", promien[7], x_uran, kolory_planet[7], dane_planet.masy['Uran'], y_uran)
        wektor_sily_uran = sila_grawitacji(uran_tmp, Slonce_obliczeniowe, x_uran, y_uran, x_slonca, y_slonca) + sila_grawitacji(uran_tmp, saturn_tmp, x_uran, y_uran, x_saturn, y_saturn) + sila_grawitacji(uran_tmp, neptun_tmp, x_uran, y_uran, x_neptun, y_neptun)
        ped_uran = ped_uran + wektor_sily_uran * dt
        x_uran = x_uran + (ped_uran[0] / uran_tmp.masa) * dt
        y_uran = y_uran + (ped_uran[1] / uran_tmp.masa) * dt
    else:
        uran_tmp = Planeta("Uran", 0, x_uran, kolory_planet[7], 0, y_uran)

    # neptun
    neptun_do_slonca = np.linalg.norm([x_neptun, y_neptun, 0])
    if neptun_do_slonca > 30:
        neptun_tmp = Planeta("Neptun", promien[8], x_neptun, kolory_planet[8], dane_planet.masy['Neptun'], y_neptun)
        wektor_sily_neptun = sila_grawitacji(neptun_tmp, Slonce_obliczeniowe, x_neptun, y_neptun, x_slonca, y_slonca) + sila_grawitacji(neptun_tmp, uran_tmp, x_neptun, y_neptun, x_uran, y_uran)
        ped_neptun = ped_neptun + wektor_sily_neptun * dt
        x_neptun = x_neptun + (ped_neptun[0] / neptun_tmp.masa) * dt
        y_neptun = y_neptun + (ped_neptun[1] / neptun_tmp.masa) * dt
    else:
        neptun_tmp = Planeta("Neptun", 0, x_neptun, kolory_planet[8], 0, y_neptun)
#       #       #       #       #       #       #       #       #       #

    Trail_cords["Ziemia"][0].append(x_ziemi)
    Trail_cords["Ziemia"][1].append(y_ziemi)
    Trail_cords["Merkury"][0].append(x_merkury)
    Trail_cords["Merkury"][1].append(y_merkury)
    Trail_cords["Wenus"][0].append(x_wenus)
    Trail_cords["Wenus"][1].append(y_wenus)
    Trail_cords["Mars"][0].append(x_mars)
    Trail_cords["Mars"][1].append(y_mars)
    Trail_cords["Jowisz"][0].append(x_jowisz)
    Trail_cords["Jowisz"][1].append(y_jowisz)
    Trail_cords["Saturn"][0].append(x_saturn)
    Trail_cords["Saturn"][1].append(y_saturn)
    Trail_cords["Uran"][0].append(x_uran)
    Trail_cords["Uran"][1].append(y_uran)
    Trail_cords["Neptun"][0].append(x_neptun)
    Trail_cords["Neptun"][1].append(y_neptun)



    zmiany_pozycji["Merkury"].append(merkury_tmp.Generacja_Planety())
    zmiany_pozycji["Wenus"].append(wenus_tmp.Generacja_Planety())
    zmiany_pozycji["Ziemia"].append(ziemia_tmp.Generacja_Planety())
    zmiany_pozycji["Mars"].append(mars_tmp.Generacja_Planety())
    zmiany_pozycji["Jowisz"].append(jowisz_tmp.Generacja_Planety())
    zmiany_pozycji["Saturn"].append(saturn_tmp.Generacja_Planety())
    zmiany_pozycji["Uran"].append(uran_tmp.Generacja_Planety())
    zmiany_pozycji["Neptun"].append(neptun_tmp.Generacja_Planety())
    zmiany_pozycji["Ziemia_trail"].append(Ziemia.PlanetTrail(Trail_cords["Ziemia"][0],Trail_cords["Ziemia"][1],iteracje=i))
    zmiany_pozycji["Merkury_trail"].append(Merkury.PlanetTrail(Trail_cords["Merkury"][0],Trail_cords["Merkury"][1],iteracje=i))
    zmiany_pozycji["Wenus_trail"].append(Wenus.PlanetTrail(Trail_cords["Wenus"][0],Trail_cords["Wenus"][1],iteracje = i))
    zmiany_pozycji["Mars_trail"].append(Mars.PlanetTrail(Trail_cords["Mars"][0], Trail_cords["Mars"][1],iteracje=i))
    zmiany_pozycji["Jowisz_trail"].append(Jowisz.PlanetTrail(Trail_cords["Jowisz"][0], Trail_cords["Jowisz"][1],iteracje=i))
    zmiany_pozycji["Saturn_trail"].append(Saturn.PlanetTrail(Trail_cords["Saturn"][0], Trail_cords["Saturn"][1],iteracje=i))
    zmiany_pozycji["Uran_trail"].append(Uran.PlanetTrail(Trail_cords["Uran"][0], Trail_cords["Uran"][1],iteracje=i))
    zmiany_pozycji["Neptun_trail"].append(Neptun.PlanetTrail(Trail_cords["Neptun"][0], Trail_cords["Neptun"][1],iteracje=i))



klatki = []
sliders_dict = {"steps":[]}
for i in range(0, 200):
    klatki.append(go.Frame(data=[Slonce,zmiany_pozycji["Merkury"][i],
                                 zmiany_pozycji["Merkury_trail"][i],
                                 zmiany_pozycji["Wenus"][i],
                                 zmiany_pozycji["Wenus_trail"][i],
                                 zmiany_pozycji["Ziemia"][i],
                                 zmiany_pozycji['Ziemia_trail'][i],
                                 zmiany_pozycji["Mars"][i],
                                 zmiany_pozycji["Mars_trail"][i],
                                 zmiany_pozycji["Jowisz"][i],
                                 zmiany_pozycji["Jowisz_trail"][i],
                                 zmiany_pozycji["Saturn"][i],
                                 zmiany_pozycji["Saturn_trail"][i],
                                 zmiany_pozycji["Uran"][i],
                                 zmiany_pozycji["Uran_trail"][i],
                                 zmiany_pozycji["Neptun"][i],
                                 zmiany_pozycji["Neptun_trail"][i]
                                 ]))


Planety_do_Ukladu = [Slonce,
                        Merkury.Generacja_Planety(),
                        zmiany_pozycji["Merkury_trail"][0],
                        Wenus.Generacja_Planety(),
                        zmiany_pozycji["Wenus_trail"][0],
                        Ziemia.Generacja_Planety(),
                        zmiany_pozycji["Ziemia_trail"][0],
                        Mars.Generacja_Planety(),
                        zmiany_pozycji["Mars_trail"][0],
                        Jowisz.Generacja_Planety(),
                        zmiany_pozycji["Jowisz_trail"][0],
                        Saturn.Generacja_Planety(),
                        zmiany_pozycji["Saturn_trail"][0],
                        Uran.Generacja_Planety(),
                        zmiany_pozycji["Uran_trail"][0],
                        Neptun.Generacja_Planety(),
                        zmiany_pozycji["Neptun_trail"][0]]


lay = go.Layout(title = "Proto-Układ",showlegend=False,margin=dict(l=0,r=0,t=0,b=0),autosize=True,
    scene= dict(xaxis = dict(title = 'odleglosc od slonca',range = [-10000,10000],color = 'black'),
                yaxis = dict(title = 'odleglosc od slonca',range = [-10000,10000],color = 'black'),
                zaxis = dict(range = [-10000,10000],color = 'white')),
                updatemenus = [dict(
                    type = 'buttons',
                    buttons = [dict(label = 'Play',
                    method = 'animate',
                    args = [None, {"frame": {"duration": 30, "redraw": True},"fromcurrent": True, "transition": {"duration": 5}}]),
                            {"args": [[None], {"frame": {"duration": 0, "redraw": True},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"}
                    ])])

fig = go.Figure(data = Planety_do_Ukladu,layout=lay, frames=klatki)
fig["layout"]["sliders"] = [sliders_dict]
fig.write_html('tmp.html', auto_open=False)