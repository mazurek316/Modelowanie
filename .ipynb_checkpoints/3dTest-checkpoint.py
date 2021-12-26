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
        self.kolor = kolor
        self.trace = self.Generacja_Planety()
    def Generacja_Planety(self):
        phi = np.linspace(0, 2 * np.pi, 15)
        theta = np.linspace(0, np.pi, 15)
        x_cords = self.odleglosc_od_slonca + self.rozmiar * np.outer(np.cos(phi), np.sin(theta))  # macierz współrzędnych x
        y_cords = self.rozmiar * np.outer(np.sin(phi), np.sin(theta))  # macierz współrzędnych y
        z_cords = 3+ self.rozmiar * np.outer(np.ones(15), np.cos(theta))
        Planeta = go.Surface(x=x_cords, y=y_cords, z=z_cords, colorscale=[[0, self.kolor], [1, self.kolor]])
        Planeta.update(showscale=False)
        return Planeta
Slonce = Planeta("Słońce",25,0,"#FFFF00").Generacja_Planety()
Ziemia = Planeta("Ziemia",25,50,"#10f2c3").Generacja_Planety()

fig = go.Figure(data = [Slonce,Ziemia],
                layout = go.Layout(
                    scene = {"xaxis": {"range": [-500,500]},
                            "yaxis": {"range": [-500,500]},
                            "zaxis": {"range": [-500,500]}}
                ))
fig.show()
fig.write_html('tmp.html', auto_open=True)