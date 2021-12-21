import plotly.graph_objects as go
import numpy as np
import math
import plotly.io as pio
import scipy.constants

#print(pio.renderers.default)

#fig.show()


class Planeta:
    def __init__(self,nazwa,rozmiar,odleglosc,kolor,przesuniecie_x = 0,przesuniecie_y = 0):
        self.nazwa = nazwa
        self.rozmiar = rozmiar
        self.odleglosc_od_slonca = odleglosc
        self.kolory = kolor
        self.zmianax = przesuniecie_x
        self.zmianay = przesuniecie_y

    def Generacja_Planety(self):
        phi = np.linspace(0, 2 * np.pi, 15)
        theta = np.linspace(0, np.pi, 15)
        self.x_cords = self.odleglosc_od_slonca + self.rozmiar * np.outer(np.cos(phi), np.sin(theta)) + self.zmianax  # macierz współrzędnych x
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
    def Generacja_Orbity(self,offset = 2,clr = 'black',wdth = 2):
        xcord = []
        ycord = []
        zcord = []

        # Obliczanie koordynatow
        for i in range(0, 361):  # dla każdego stopnia
            xcord = xcord + [(round(np.cos(math.radians(i)), 5)) * self.odleglosc_od_slonca + offset]
            ycord = ycord + [(round(np.sin(math.radians(i)), 5)) * self.odleglosc_od_slonca]
            zcord = zcord + [0]
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

Slonce = Planeta("Słońce",25,0,"#FFFF00").Generacja_Planety()
Ziemia = Planeta("Ziemia",5,50,"#10f2c3")
Orbita_Ziemi = Ziemia.Generacja_Orbity()
zmiany_pozycji = []

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
for i in range(1,100):
    erth = Planeta("Ziemia",5,50,"#10f2c3",i,i)
    zmiany_pozycji.append(erth.Generacja_Planety())                       #poruszanie się
    x1 = erth.x_dumper()
    y1 = erth.y_dumper()
    tmp = sila_grawitacji(x1, 0, y1, 0)
    print(tmp)

klatki = []
for i in range(0,50):
    klatki.append(go.Frame(data=[Slonce,zmiany_pozycji[i]]))
zmiany_pozycji.append(Slonce)

lay = go.Layout(title="Objektowy solar System", autosize = True, margin = dict(l=2,r=2,b=2,t=2),
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
                               ])])

fig = go.Figure(data = [Slonce,Ziemia.Generacja_Planety(),Orbita_Ziemi],layout=lay, frames=klatki)


fig.write_html('tmp.html', auto_open=False)