
import plotly.graph_objects as go
import numpy as np
import math
import plotly.io as pio
import scipy.constants

#print(pio.renderers.default)

#fig.show()


class Planeta:
    def __init__(self,nazwa,rozmiar,odleglosc,kolor, masa, przesuniecie_y):
        self.nazwa = nazwa
        self.rozmiar = rozmiar
        self.odleglosc_od_slonca = odleglosc
        self.kolory = kolor
        self.zmianay = przesuniecie_y
        self.predkosc = (np.pi*2*50)/10             # to chyba zbędne
        self.srodek_x = odleglosc
        self.srodek_y = 0
        self.masa = masa
    def Generacja_Planety(self):
        phi = np.linspace(0, 2 * np.pi, 15)
        theta = np.linspace(0, np.pi, 15)
        self.x_cords = self.odleglosc_od_slonca + self.rozmiar * np.outer(np.cos(phi), np.sin(theta)) # macierz współrzędnych x
        self.y_cords = self.rozmiar * np.outer(np.sin(phi), np.sin(theta)) + self.zmianay  # macierz współrzędnych y
        self.z_cords = 3+ self.rozmiar * np.outer(np.ones(15), np.cos(theta))
        Planeta = go.Surface(x=self.x_cords, y=self.y_cords, z=self.z_cords, colorscale=[[0, self.kolory], [1, self.kolory]],hovertext=f'nazwa = {str(self.nazwa)},<br> rozmiar = {str(self.rozmiar)} <br> odleglosc od slonca = {str(self.odleglosc_od_slonca)}')
        Planeta.update(showscale=False)
        return Planeta

    def x_dumper(self):
        return self.srodek_x
    def y_dumper(self):
        return self.zmianay
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
    #print(poz_1)
    return sila_wektor


promien_km = [200000,4878,12104,12756,6787,142796,120660,51118,48600]
promien = [((i / 12756)*2) for i in promien_km]
odleglosc_od_slonca = [0,57.9,108.2,149.6,227.9,778.6,1433.5,2872.5,4495.1]
kolory_planet = ['#ffff00','#87877d','#d23100','#10f2c3','#b20000','#ebebd2','#ebcd82','#37ffda','#2500ab']

Slonce = Planeta("Słońce",promien[0],odleglosc_od_slonca[0],kolory_planet[0], 1.9891 * np.power(10, 21, dtype='float64'), 0).Generacja_Planety()
Slonce_obliczeniowe = Planeta("Słońce",promien[0],odleglosc_od_slonca[0],kolory_planet[0], 1.9891 * np.power(10, 21, dtype='float64'), 0)
Merkury = Planeta("Merkury",promien[1],odleglosc_od_slonca[1],kolory_planet[1], 3.302 * np.power(10, 14, dtype='float64'), 0)
Wenus = Planeta("Wenus",promien[2],odleglosc_od_slonca[2],kolory_planet[2], 4.8685 * np.power(10, 15, dtype='float64'), 0)
Ziemia = Planeta("Ziemia",promien[3],odleglosc_od_slonca[3],kolory_planet[3], 5.9742 * np.power(10, 15, dtype='float64'), 0)
Mars = Planeta("Mars",promien[4],odleglosc_od_slonca[4],kolory_planet[4], 6.4185 * np.power(10, 14, dtype='float64'), 0)
Jowisz = Planeta("Jowisz",promien[5],odleglosc_od_slonca[5],kolory_planet[5], 1.899 * np.power(10, 18, dtype='float64'), 0)
Saturn = Planeta("Saturn",promien[6],odleglosc_od_slonca[6],kolory_planet[6], 5.6846 * np.power(10, 17, dtype='float64'), 0)
Uran = Planeta("Uran",promien[7],odleglosc_od_slonca[7],kolory_planet[7], 8.6832 * np.power(10, 16, dtype='float64'), 0)
Neptun = Planeta("Neptun",promien[8],odleglosc_od_slonca[8],kolory_planet[8], 1.02430 * np.power(10, 17, dtype='float64'), 0)


zmiany_pozycji = {"Merkury":[],"Wenus":[],"Ziemia":[],"Mars":[],"Jowisz":[],"Saturn":[],"Uran":[],"Neptun":[],'Ziemia_trail':[],"Merkury_trail":[],"Wenus_trail":[]}

#       #       #           #           #

ped_ziemi = np.array([0, 1.78e20, 0])

x_ziemi = 149.6
y_ziemi = 0
dt = 0.0001
Trail_cords = {"Merkury":[[],[]],"Wenus":[[],[]],"Ziemia":[[],[]]}
#       #       #           #           #
erth_tmp = Planeta("Ziemia", promien[3], x_ziemi, "#10f2c3", 5.9742 * np.power(10, 15, dtype='float64'), y_ziemi)
for i in range(0, 200):
    time = i * 0.02

    wektor_sily_ziemi = sila_grawitacji(erth_tmp, Slonce_obliczeniowe, x_ziemi, y_ziemi, 0, 0)

    ped_ziemi = ped_ziemi + wektor_sily_ziemi * dt

    x_merkury = odleglosc_od_slonca[1]*np.cos(0.829545454*np.pi * time + np.pi / 2)
    y_merkury = odleglosc_od_slonca[1]*np.sin(0.829545454*np.pi * time + np.pi / 2)
    x_wenus = odleglosc_od_slonca[2]*np.sin(0.324444444*np.pi * time + np.pi / 2)
    y_wenus = odleglosc_od_slonca[2]*np.cos(0.324444444*np.pi * time + np.pi / 2)
    #print('kordy', x_ziemi, y_ziemi)
    #x_ziemi = odleglosc_od_slonca[3] * np.cos(0.2 * np.pi * time + np.pi / 2)
    #y_ziemi = odleglosc_od_slonca[3] * np.sin(0.2 * np.pi * time + np.pi / 2)

    #print(erth_tmp.odleglosc_od_slonca, y_ziemi)
    x_ziemi = x_ziemi + (ped_ziemi[0] / erth_tmp.masa) * dt
    y_ziemi = y_ziemi + (ped_ziemi[1] / erth_tmp.masa) * dt
    Trail_cords["Ziemia"][0].append(x_ziemi)
    Trail_cords["Ziemia"][1].append(y_ziemi)
    Trail_cords["Merkury"][0].append(x_merkury)
    Trail_cords["Merkury"][1].append(y_merkury)
    Trail_cords["Wenus"][0].append(x_wenus)
    Trail_cords["Wenus"][1].append(y_wenus)


    x_mars = odleglosc_od_slonca[4]*np.cos(0.106259098 * np.pi * time + np.pi / 2)
    y_mars = odleglosc_od_slonca[4] * np.sin(0.106259098 * np.pi * time + np.pi / 2)
    x_jowisz = odleglosc_od_slonca[5] * np.cos(0.0168490441 * np.pi * time + np.pi / 2)
    y_jowisz = odleglosc_od_slonca[5] * np.sin(0.0168490441 * np.pi * time + np.pi / 2)
    x_saturn = odleglosc_od_slonca[6] * np.cos(0.008 * np.pi * time + np.pi / 2)
    y_saturn = odleglosc_od_slonca[6] * np.sin(0.008 * np.pi * time + np.pi / 2)
    x_uran = odleglosc_od_slonca[7] * np.cos(0.0004 * np.pi * time + np.pi / 2)
    y_uran = odleglosc_od_slonca[7] * np.sin(0.0004 * np.pi * time + np.pi / 2)
    x_neptun = odleglosc_od_slonca[8] * np.cos(0.0001 * np.pi * time + np.pi / 2)
    y_neptun = odleglosc_od_slonca[8] * np.sin(0.0001 * np.pi * time + np.pi / 2)

    merkury_tmp = Planeta("Merkury",promien[1],x_merkury,'#87877d', 3.302 * np.power(10, 14, dtype='float64'), y_merkury)
    wenus_tmp = Planeta("Wenus",promien[2],x_wenus,'#d23100', 4.8685 * np.power(10, 15, dtype='float64'), y_wenus)
    ziemia_tmp = Planeta("Ziemia",promien[3],x_ziemi,kolory_planet[3],5.9742 * np.power(10, 15, dtype='float64'), y_ziemi)
    mars_tmp = Planeta("Mars",promien[4],x_mars,kolory_planet[4], 6.4185 * np.power(10, 14, dtype='float64'), y_mars)
    jowisz_tmp = Planeta("Jowisz",promien[5],x_jowisz,kolory_planet[5], 1.899 * np.power(10, 18, dtype='float64'), y_jowisz)
    saturn_tmp = Planeta("Saturn", promien[6], x_saturn, kolory_planet[6], 5.6846 * np.power(10, 17, dtype='float64'), y_saturn)
    uran_tmp = Planeta("Uran", promien[7], x_uran, kolory_planet[7], 8.6832 * np.power(10, 16, dtype='float64'), y_uran)
    neptun_tmp = Planeta("Neptun", promien[8], x_neptun, kolory_planet[8], 1.02430 * np.power(10, 17, dtype='float64'), y_neptun)
    #print(x_wenus,y_wenus)
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
#Trail1 = go.Scatter3d(x=[149.6,130],y=)
klatki = []
Ziemia.Generacja_Orbity()
for i in range(0, 200):
    klatki.append(go.Frame(data=[Slonce,zmiany_pozycji["Merkury"][i],
                                 zmiany_pozycji["Wenus"][i],
                                 zmiany_pozycji["Ziemia"][i],
                                 zmiany_pozycji["Merkury_trail"][i],
                                 zmiany_pozycji["Wenus_trail"][i],
                                 zmiany_pozycji['Ziemia_trail'][i]
                                 #zmiany_pozycji["Mars"][i],
                                 #zmiany_pozycji["Jowisz"][i],
                                 #zmiany_pozycji["Saturn"][i],
                                 #zmiany_pozycji["Uran"][i],
                                 #zmiany_pozycji["Neptun"][i]
                                 ]))
print(zmiany_pozycji["Ziemia_trail"])



Planety_do_Układu = [Slonce,
                        Merkury.Generacja_Planety(),
                        Wenus.Generacja_Planety(),
                        Ziemia.Generacja_Planety(),
                        Mars.Generacja_Planety(),
                        Jowisz.Generacja_Planety(),
                        Saturn.Generacja_Planety(),
                        Uran.Generacja_Planety(),Neptun.Generacja_Planety()]


Orbity_Planet = [#Merkury.Generacja_Orbity()
                #,Wenus.Generacja_Orbity(),
                 #Ziemia.Generacja_Orbity(),
                 Mars.Generacja_Orbity(),
                 Jowisz.Generacja_Orbity(),
                 Saturn.Generacja_Orbity(),
                 Uran.Generacja_Orbity(),Neptun.Generacja_Orbity()]


lay = go.Layout(title = "Proto-Układ",showlegend=False,margin=dict(l=2,r=2,t=2,b=2),autosize=False,width=1920,height=1080,
    scene= dict(xaxis = dict(title = 'odleglosc od slonca',range = [-7000,7000],color = 'black'),
                yaxis = dict(title = 'odleglosc od slonca',range = [-7000,7000],color = 'black'),
                zaxis = dict(range = [-7000,7000],color = 'white')),
                updatemenus = [dict(
                    type = 'buttons',
                    buttons = [dict(label = 'Play',
                    method = 'animate',
                    args = [None, {"frame": {"duration": 1, "redraw": True},"fromcurrent": True, "transition": {"duration": 0.2}}]),
                            {"args": [[None], {"frame": {"duration": 0, "redraw": True},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"}
                    ])])

fig = go.Figure(data = Planety_do_Układu+Orbity_Planet,layout=lay, frames=klatki)

#fig.write_html('tmp.html', auto_open=False)
fig.show()