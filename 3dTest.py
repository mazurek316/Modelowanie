import plotly.graph_objects as go
import numpy as np
import plotly.io as pio


#print(pio.renderers.default)

#fig.show()


class Planeta:
    def __init__(self,nazwa,rozmiar,odleglosc,kolor):
        self.nazwa = nazwa
        self.rozmiar = rozmiar
        self.odleglosc_od_slonca = odleglosc
        self.kolory = kolor
        self.zmianax = 0
        self.zmianay = 0

    def zmianaPozycji(self,x = 0 ,y = 0):
        self.zmianax = x
        self.zmianay = y

    def Generacja_Planety(self):
        phi = np.linspace(0, 2 * np.pi, 15)
        theta = np.linspace(0, np.pi, 15)
        x_cords = self.odleglosc_od_slonca + self.rozmiar * np.outer(np.cos(phi), np.sin(theta)) + self.zmianax  # macierz współrzędnych x
        y_cords = self.rozmiar * np.outer(np.sin(phi), np.sin(theta)) + self.zmianay  # macierz współrzędnych y
        z_cords = 3+ self.rozmiar * np.outer(np.ones(15), np.cos(theta))
        Planeta = go.Surface(x=x_cords, y=y_cords, z=z_cords, colorscale=[[0, self.kolory], [1, self.kolory]])
        Planeta.update(showscale=False)
        np.savetxt("danex.txt", x_cords)
        return Planeta
Slonce = Planeta("Słońce",25,0,"#FFFF00").Generacja_Planety()
Ziemia = Planeta("Ziemia",25,50,"#10f2c3").Generacja_Planety()

fig = go.Figure(data = [Slonce,Ziemia])

fig.update_layout(title="Objektowy solar System", autosize = True, margin = dict(l=0,r=0,b=0,t=0))
fig.write_html('tmp.html', auto_open=False)