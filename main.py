import math
import numpy as np
import time
from plotly.basedatatypes import BaseLayoutType
import plotly.graph_objects as go
import numpy as np

def sfery(rozmiar,kolory,odleglosc = 0,przesuniecie = 0): #rozmiar to                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              promien, odleglosc to odlegosc od srodka ukladu czyli srodka slonca
    #Ustawiam by każda sfera złożona była ze 100 punktów
    theta = np.linspace(0,2*np.pi,100)
    phi = np.linspace(0,np.pi,100)

    #Ustawianie współrzędnych punktów z których tworzona jest sfera
    x0 = -(przesuniecie+10) + odleglosc + rozmiar*np.outer(np.cos(theta),np.sin(phi))
    y0 = przesuniecie + rozmiar*np.outer(np.sin(theta),np.sin(phi))
    z0 = rozmiar*np.outer(np.ones(100),np.cos(phi))

    #Tworzenie linii ruchu
    tor = go.Surface(x=x0, y=y0, z=z0, colorscale=[[0,kolory],[1,kolory]])
    tor.update(showscale=False)
    return tor
def orbity(odleglosc,offset=2,clr='black',wdth=5):
    xcord = []
    ycord = []
    zcord = []

    #Obliczanie koordynatow
    for i in range(0,361): # dla każdego stopnia
        xcord = xcord + [(round(np.cos(math.radians(i)),5))*odleglosc + offset]
        ycord = ycord + [(round(np.sin(math.radians(i)),5))*odleglosc]
        zcord = zcord + [0]
    tor = go.Scatter3d(x = xcord,y = ycord, z= zcord,marker=dict(size=0.1),line=dict(color=clr,width=wdth))
    return tor
promien_km = [200000,4878,12104,12756]
promien = [((i / 12756)*2) for i in promien_km]
odleglosc_od_slonca = [0,57.9,108.2,149.6,227.9]
    #tworzenie sfer:
trace0 = sfery(promien[0],'#ffff00',odleglosc_od_slonca[0]) #Słońce
trace1 = sfery(promien[1],'#87877d',odleglosc_od_slonca[1]) #Merkury
trace2 = sfery(promien[2],'#d23100',odleglosc_od_slonca[2]) #Venus
trace3 = sfery(promien[3],'#325bff',odleglosc_od_slonca[3]) #Ziemia
trace1f2 = sfery(promien[1],'#87877d',odleglosc_od_slonca[1],10)  
trace2f2 = sfery(promien[2],'#d23100',odleglosc_od_slonca[2],10)    
trace3f2 = sfery(promien[3],'#325bff',odleglosc_od_slonca[3],10)    
    
    #tworzenie orbit:
trace11 = orbity(odleglosc_od_slonca[1]-2) # Merkury
trace12 = orbity(odleglosc_od_slonca[2]-2) #Venus
trace13 = orbity(odleglosc_od_slonca[3]-2) #Ziemia

layout = go.Layout(title = "Proto-Układ",showlegend=False,margin=dict(l=0,r=0,t=0,b=0),
    scene= dict(xaxis = dict(title = 'odleglosc od slonca',range = [-300,300],color = 'black'),
                yaxis = dict(title = 'odleglosc od slonca',range = [-300,300],color = 'black'),
                zaxis = dict(range = [-300,300],color = 'white')),
                updatemenus = [dict(
                    type = 'buttons',
                    buttons = [dict(label = 'Play',
                    method = 'animate',
                    args = [None]),
                            {"args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"}
                    ])])
                

fig = go.Figure(data = [trace0,trace1,trace11,trace2,trace12,trace3,trace13],
                layout = layout,
                frames=[go.Frame(data = [trace0,trace1,trace2,sfery(promien[3],'#325bff',odleglosc_od_slonca[3],k),trace11,trace12,trace13,
                ])
                        for k in range(0,150,1)])
#fig.add_traces([trace11,trace12,trace13])
#fig.update_traces(patch = dict(y = y+5),selector = dict(trace1,trace2,trace3))
fig.show()
