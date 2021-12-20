import plotly.graph_objects as go
import numpy as np
import math
import plotly.io as pio


#print(pio.renderers.default)

#fig.show()


class Planeta:
    phi = np.linspace(0, 2 * np.pi, 15)
    theta = np.linspace(0, np.pi, 15)
    def __init__(self,nazwa,rozmiar,odleglosc,kolor,xcords,ycords,przesuniecie_x = 0,przesuniecie_y = 0):
        self.nazwa = nazwa
        self.rozmiar = rozmiar
        self.odleglosc_od_slonca = odleglosc
        self.kolory = kolor
        self.zmianax = przesuniecie_x
        self.zmianay = przesuniecie_y
        #self.x_cords = self.odleglosc_od_slonca + self.rozmiar * np.outer(np.cos(self.phi), np.sin(self.theta)) + self.zmianax
        #self.y_cords = self.rozmiar * np.outer(np.sin(self.phi), np.sin(self.theta)) + self.zmianay
        self.x_cords = xcords
        self.y_cords = ycords
        self.z_cords = 3 + self.rozmiar * np.outer(np.ones(15), np.cos(self.theta))
    def zmianaPozycji(self,x = 0 ,y = 0):
        self.zmianax = x
        self.zmianay = y

    def Generacja_Planety(self):

        Planeta = go.Surface(x=self.x_cords, y=self.y_cords, z=self.z_cords, colorscale=[[0, self.kolory], [1, self.kolory]])
        Planeta.update(showscale=False)
        return Planeta
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


Slonce = Planeta("Słońce",25,0,"#FFFF00").Generacja_Planety()
Ziemia = Planeta("Ziemia",5,50,"#10f2c3")
Orbita_Ziemi = Ziemia.Generacja_Orbity()
zmiany_pozycji = []
for i in range(1,100):
    zmiany_pozycji.append(Planeta("Ziemia",5,50,"#10f2c3",i,i).Generacja_Planety())
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

fig = go.Figure(data = [Slonce,Ziemia.Generacja_Planety(),Orbita_Ziemi],layout=lay,frames=klatki)


fig.write_html('tmp.html', auto_open=False)