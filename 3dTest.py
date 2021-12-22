import plotly.graph_objects as go
import numpy as np
import math
import plotly.io as pio
import scipy.constants

#print(pio.renderers.default)

#fig.show()


class Planeta:
    def __init__(self,nazwa,rozmiar,odleglosc,kolor,przesuniecie_y = 0):
        self.nazwa = nazwa
        self.rozmiar = rozmiar
        self.odleglosc_od_slonca = odleglosc
        self.kolory = kolor
        self.zmianay = przesuniecie_y
        self.predkosc = (np.pi*2*50)/10
        self.srodek_x = odleglosc
        self.srodek_y = 0
    def Generacja_Planety(self):
        phi = np.linspace(0, 2 * np.pi, 15)
        theta = np.linspace(0, np.pi, 15)
        self.x_cords = self.odleglosc_od_slonca + self.rozmiar * np.outer(np.cos(phi), np.sin(theta)) # macierz współrzędnych x
        self.y_cords = self.rozmiar * np.outer(np.sin(phi), np.sin(theta)) + self.zmianay  # macierz współrzędnych y
        self.z_cords = 3+ self.rozmiar * np.outer(np.ones(15), np.cos(theta))
        Planeta = go.Surface(x=self.x_cords, y=self.y_cords, z=self.z_cords, colorscale=[[0, self.kolory], [1, self.kolory]])
        self.srodek_x = self.x_cords[0][0]
        self.srodek_y = self.y_cords[0][0]
        #print(self.y_cords[0][0])
        Planeta.update(showscale=False)
        return Planeta

    def x_dumper(self):
        return self.srodek_x
    def y_dumper(self):
        return self.srodek_y
    def Generacja_Orbity(self,offset = 1,clr = 'black',wdth = 0.5):
        xcord = []
        ycord = []
        zcord = []

        # Obliczanie koordynatow
        for i in range(0, 361):  # dla każdego stopnia
            xcord = xcord + [(round(np.cos(math.radians(i)), 5)) * self.odleglosc_od_slonca + offset]
            ycord = ycord + [(round(np.sin(math.radians(i)), 5)) * self.odleglosc_od_slonca]
            zcord = zcord + [3]
        orbita = go.Scatter3d(x=xcord, y=ycord, z=zcord, marker=dict(size=0.1), line=dict(color=clr, width=wdth))
        return orbita

    ###########################
    def sila_grawitacji(self, x1, y1, x2, y2):
        self.G = scipy.constants.gravitational_constant
        # r_wektor =
        # r_wartosc = np.power(r_wektor, 2)
        # r_wersor = que

        self.masy = {'Slonce': 1.9891 * np.power(10, 30, dtype='float64'),
                     'Merkury': 3.302 * np.power(10, 23, dtype='float64'),
                     'Wenus': 4.8685 * np.power(10, 24, dtype='float64'),
                     'Ziemia': 5.9742 * np.power(10, 24, dtype='float64'),
                     'Mars': 6.4185 * np.power(10, 23, dtype='float64'),
                     'Jowisz': 1.899 * np.power(10, 27, dtype='float64'),
                     'Saturn': 5.6846 * np.power(10, 26, dtype='float64'),
                     'Uran': 8.6832 * np.power(10, 25, dtype='float64'),
                     'Neptun': 1.02430 * np.power(10, 26, dtype='float64'),
                     'Pluton': 1.305 * np.power(10, 22, dtype='float64')}

        self.dystanse = {'Merkury': 5.79 * np.power(10, 7, dtype='float64'),
                         'Wenus': 1.082 * np.power(10, 8, dtype='float64'),
                         'Ziemia': 1.496 * np.power(10, 8, dtype='float64'),
                         'Mars': 2.279 * np.power(10, 8, dtype='float64'),
                         'Jowisz': 7.786 * np.power(10, 8, dtype='float64'),
                         'Saturn': 1.4335 * np.power(10, 10, dtype='float64'),
                         'Uran': 2.8725 * np.power(10, 10, dtype='float64'),
                         'Neptun': 4.4951 * np.power(10, 10, dtype='float64'),
                         'Pluton': 5.87 * np.power(10, 9, dtype='float64')}

        '''self.r_wektor = pozycje - pozycje2
        self.r_wartosc = abs(pozycje)
        self.r_wersor = self.r_wektor / self.r_wartosc
        self.wartosc_sily = self.G * cialo1 * cialo2 / self.r_wartosc ** 2
        self.wektor_sily = - self.wartosc_sily * self.r_wersor
        # print(self.sila_grawitacji(masy['Slonce'], self.masy['Ziemia'], self.dystanse['Ziemia']))'''
        return 0
    ##############################



def sila_grawitacji(x1, x2, y1, y2):
    G = scipy.constants.gravitational_constant
    #r_wektor =
    # r_wartosc = np.power(r_wektor, 2)
    # r_wersor = que

    masy = {'Slonce': 1.9891 * np.power(10, 30, dtype='float64'),
                 'Merkury': 3.302 * np.power(10, 23, dtype='float64'),
                 'Wenus': 4.8685 * np.power(10, 24, dtype='float64'),
                 'Ziemia': 5.9742 * np.power(10, 24, dtype='float64'),
                 'Mars': 6.4185 * np.power(10, 23, dtype='float64'),
                 'Jowisz': 1.899 * np.power(10, 27, dtype='float64'),
                 'Saturn': 5.6846 * np.power(10, 26, dtype='float64'),
                 'Uran': 8.6832 * np.power(10, 25, dtype='float64'),
                 'Neptun': 1.02430 * np.power(10, 26, dtype='float64'),
                 'Pluton': 1.305 * np.power(10, 22, dtype='float64')}

    dystanse = {'Merkury': 5.79 * np.power(10, 7, dtype='float64'),
                     'Wenus': 1.082 * np.power(10, 8, dtype='float64'),
                     'Ziemia': 1.496 * np.power(10, 8, dtype='float64'),
                     'Mars': 2.279 * np.power(10, 8, dtype='float64'),
                     'Jowisz': 7.786 * np.power(10, 8, dtype='float64'),
                     'Saturn': 1.4335 * np.power(10, 10, dtype='float64'),
                     'Uran': 2.8725 * np.power(10, 10, dtype='float64'),
                     'Neptun': 4.4951 * np.power(10, 10, dtype='float64'),
                     'Pluton': 5.87 * np.power(10, 9, dtype='float64')}

    x_wektor = x1 - x2
    y_wektor = y1 - y2

    r_wektor = x_wektor + y_wektor
    r_wartosc = abs(r_wektor)
    r_wersor = r_wektor / r_wartosc
    wartosc_sily = G * masy['Slonce'] * masy['Ziemia'] / r_wartosc ** 2
    wektor_sily = - wartosc_sily * r_wersor

    return wektor_sily


x2 = 0
y2 = 0
#for i in range(1,100):
 #   erth = Planeta("Ziemia",5,50,"#10f2c3",i,i)
  #  zmiany_pozycji.append(erth.Generacja_Planety())                       #poruszanie się
   # x1 = erth.x_dumper()
    #y1 = erth.y_dumper()
    #tmp = sila_grawitacji(x1, 0, y1, 0)
    #print(tmp)






promien_km = [200000,4878,12104,12756,6787,142796,120660,51118,48600]
promien = [((i / 12756)*2) for i in promien_km]
odleglosc_od_slonca = [0,57.9,108.2,149.6,227.9,778.6,1433.5,2872.5,4495.1]
kolory_planet = ['#ffff00','#87877d','#d23100','#10f2c3','#b20000','#ebebd2','#ebcd82','#37ffda','#2500ab']

Slonce = Planeta("Słońce",promien[0],odleglosc_od_slonca[0],kolory_planet[0]).Generacja_Planety()
Merkury = Planeta("Merkury",promien[1],odleglosc_od_slonca[1],kolory_planet[1])
Wenus = Planeta("Wenus",promien[2],odleglosc_od_slonca[2],kolory_planet[2])
Ziemia = Planeta("Ziemia",promien[3],odleglosc_od_slonca[3],kolory_planet[3])
Mars = Planeta("Mars",promien[4],odleglosc_od_slonca[4],kolory_planet[4])
Jowisz = Planeta("Jowisz",promien[5],odleglosc_od_slonca[5],kolory_planet[5])
Saturn = Planeta("Saturn",promien[6],odleglosc_od_slonca[6],kolory_planet[6])
Uran = Planeta("Uran",promien[7],odleglosc_od_slonca[7],kolory_planet[7])
Neptun = Planeta("Neptun",promien[8],odleglosc_od_slonca[8],kolory_planet[8])

Orbita_Ziemi = Ziemia.Generacja_Orbity()
Orbita_Merkury = Merkury.Generacja_Orbity()
Orbita_Wenus = Wenus.Generacja_Orbity()
zmiany_pozycji = {"Merkury":[],"Wenus":[],"Ziemia":[],"Mars":[],"Jowisz":[],"Saturn":[],"Uran":[],"Neptun":[]}


for i in range(0,50):
    time = i*2
    x_merkury = odleglosc_od_slonca[1]*np.cos(0.829545454*np.pi*time + np.pi/2)
    y_merkury = odleglosc_od_slonca[1]*np.sin(0.829545454*np.pi*time + np.pi/2)
    x_wenus = odleglosc_od_slonca[2]*np.sin(0.324444444*np.pi*time + np.pi/2)
    y_wenus = odleglosc_od_slonca[2]*np.cos(0.324444444*np.pi*time + np.pi/2)
    x_ziemi = odleglosc_od_slonca[3]*np.cos(0.2 * np.pi * time + np.pi / 2)
    y_ziemi = odleglosc_od_slonca[3]*np.sin(0.2 * np.pi * time + np.pi / 2)
    x_mars = odleglosc_od_slonca[4]*np.cos(0.106259098 * np.pi * time +np.pi/2)
    y_mars = odleglosc_od_slonca[4] * np.sin(0.106259098 * np.pi * time + np.pi/2)
    x_jowisz = odleglosc_od_slonca[5] * np.cos(0.0168490441 * np.pi * time + np.pi/2 )
    y_jowisz = odleglosc_od_slonca[5] * np.sin(0.0168490441 * np.pi * time + np.pi/2 )
    x_saturn = odleglosc_od_slonca[6] * np.cos(0.008 * np.pi * time + np.pi/2)
    y_saturn = odleglosc_od_slonca[6] * np.sin(0.008 * np.pi * time + np.pi/2)
    x_uran = odleglosc_od_slonca[7] * np.cos(0.0004 * np.pi * time + np.pi/2)
    y_uran = odleglosc_od_slonca[7] * np.sin(0.0004 * np.pi * time + np.pi/2)
    x_neptun = odleglosc_od_slonca[8] * np.cos(0.0001 * np.pi * time + np.pi/2)
    y_neptun = odleglosc_od_slonca[8] * np.sin(0.0001 * np.pi * time + np.pi/2)
    #print(x_ziemi,y_ziemi)
    merkury_tmp = Planeta("Merkury",promien[1],x_merkury,'#87877d',y_merkury)
    wenus_tmp = Planeta("Wenus",promien[2],x_wenus,'#d23100',y_wenus)
    erth_tmp = Planeta("Ziemia", promien[3],x_ziemi, "#10f2c3",y_ziemi)
    mars_tmp = Planeta("Mars",promien[4],x_mars,kolory_planet[4],y_mars)
    jowisz_tmp = Planeta("Jowisz",promien[5],x_jowisz,kolory_planet[5],y_jowisz)
    saturn_tmp = Planeta("Saturn", promien[6], x_saturn, kolory_planet[6], y_saturn)
    uran_tmp = Planeta("Uran", promien[7], x_uran, kolory_planet[7], y_uran)
    neptun_tmp = Planeta("Neptun", promien[8], x_neptun, kolory_planet[8], y_neptun)
    #print(x_wenus,y_wenus)
    zmiany_pozycji["Merkury"].append(merkury_tmp.Generacja_Planety())
    zmiany_pozycji["Wenus"].append(wenus_tmp.Generacja_Planety())
    zmiany_pozycji["Ziemia"].append(erth_tmp.Generacja_Planety())
    zmiany_pozycji["Mars"].append(mars_tmp.Generacja_Planety())
    zmiany_pozycji["Jowisz"].append(jowisz_tmp.Generacja_Planety())
    zmiany_pozycji["Saturn"].append(saturn_tmp.Generacja_Planety())
    zmiany_pozycji["Uran"].append(uran_tmp.Generacja_Planety())
    zmiany_pozycji["Neptun"].append(neptun_tmp.Generacja_Planety())

klatki = []
for i in range(0,50):
    klatki.append(go.Frame(data=[Slonce,zmiany_pozycji["Merkury"][i],
                                 zmiany_pozycji["Wenus"][i],
                                 zmiany_pozycji["Ziemia"][i],
                                 zmiany_pozycji["Mars"][i],
                                 zmiany_pozycji["Jowisz"][i],
                                 zmiany_pozycji["Saturn"][i],
                                 zmiany_pozycji["Uran"][i],
                                 zmiany_pozycji["Neptun"][i]]))


'''lay = go.Layout(title="Objektowy solar System", autosize = False, margin = dict(l=2,r=2,b=2,t=2),
                  updatemenus=[dict(
                      type='buttons',
                      buttons=[dict(label='Play',
                                    method='animate',
                                    args=[None,
                                          {"frame": {"duration": 0.5, "redraw": True}, "fromcurrent": True,
                                           "transition": {"duration": 0.2}}]),
                               {"args": [[None], {"frame": {"duration": 0, "redraw": False},
                                                  "mode": "immediate",
                                                  "transition": {"duration": 0}}],
                                "label": "Pause",
                                "method": "animate"}
                               ])])'''
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

fig = go.Figure(data = [Slonce,Merkury.Generacja_Planety(),Wenus.Generacja_Planety(),
                        Ziemia.Generacja_Planety(),Mars.Generacja_Planety(),
                        Jowisz.Generacja_Planety(),Saturn.Generacja_Planety(),Uran.Generacja_Planety(),Neptun.Generacja_Planety(),
                        Merkury.Generacja_Orbity(),Wenus.Generacja_Orbity(),Ziemia.Generacja_Orbity(),Mars.Generacja_Orbity(),Jowisz.Generacja_Orbity(),Saturn.Generacja_Orbity(),Uran.Generacja_Orbity(),Neptun.Generacja_Orbity()]
                ,layout=lay, frames=klatki)

fig.write_html('tmp.html', auto_open=False)