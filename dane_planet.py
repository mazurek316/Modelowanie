import numpy as np
from scipy.constants import pi
import interfejs


masy = {'Slonce': interfejs.masy_input['Slonce'] * np.power(10, interfejs.masy_pot_input['Slonce'], dtype='float64'),
        'Merkury': interfejs.masy_input['Merkury'] * np.power(10, interfejs.masy_pot_input['Merkury'], dtype='float64'),
        'Wenus': interfejs.masy_input['Wenus'] * np.power(10, interfejs.masy_pot_input['Wenus'], dtype='float64'),
        'Ziemia': interfejs.masy_input['Ziemia'] * np.power(10, interfejs.masy_pot_input['Ziemia'], dtype='float64'),
        'Mars': interfejs.masy_input['Mars'] * np.power(10, interfejs.masy_pot_input['Mars'], dtype='float64'),
        'Jowisz': interfejs.masy_input['Jowisz'] * np.power(10, interfejs.masy_pot_input['Jowisz'], dtype='float64'),
        'Saturn': interfejs.masy_input['Saturn'] * np.power(10, interfejs.masy_pot_input['Saturn'], dtype='float64'),
        'Uran': interfejs.masy_input['Uran'] * np.power(10, interfejs.masy_pot_input['Uran'], dtype='float64'),
        'Neptun': interfejs.masy_input['Neptun'] * np.power(10, interfejs.masy_pot_input['Neptun'], dtype='float64')}

dystanse = {'Merkury': interfejs.dyst_input['Merkury'] * np.power(10, interfejs.dyst_pot_input['Merkury'], dtype='float64'),
            'Wenus': interfejs.dyst_input['Wenus'] * np.power(10, interfejs.dyst_pot_input['Merkury'], dtype='float64'),
            'Ziemia': interfejs.dyst_input['Ziemia'] * np.power(10, interfejs.dyst_pot_input['Merkury'], dtype='float64'),
            'Mars': interfejs.dyst_input['Mars'] * np.power(10, interfejs.dyst_pot_input['Mars'], dtype='float64'),
            'Jowisz': interfejs.dyst_input['Jowisz'] * np.power(10, interfejs.dyst_pot_input['Jowisz'], dtype='float64'),
            'Saturn': interfejs.dyst_input['Saturn'] * np.power(10, interfejs.dyst_pot_input['Saturn'], dtype='float64'),
            'Uran': interfejs.dyst_input['Uran'] * np.power(10, interfejs.dyst_pot_input['Uran'], dtype='float64'),
            'Neptun': interfejs.dyst_input['Neptun'] * np.power(10, interfejs.dyst_pot_input['Neptun'], dtype='float64')}

dni_na_sekundy = 24 * 60 * 60
okresy_obr = {'Merkury': 88 * dni_na_sekundy,
              'Wenus': 225 * dni_na_sekundy,
              'Ziemia': 365 * dni_na_sekundy,
              'Mars': 687 * dni_na_sekundy,
              'Jowisz': 4380 * dni_na_sekundy,
              'Saturn': 10585 * dni_na_sekundy,
              'Uran': 30660 * dni_na_sekundy,
              'Neptun': 60225 * dni_na_sekundy}

prawdziwe_predkosci = {'Merkury': 2 * pi * dystanse['Merkury'] / okresy_obr['Merkury'],
              'Wenus': 2 * pi * dystanse['Wenus'] / okresy_obr['Wenus'],
              'Ziemia': 2 * pi * dystanse['Ziemia'] / okresy_obr['Ziemia'],
              'Mars': 2 * pi * dystanse['Mars'] / okresy_obr['Mars'],
              'Jowisz': 2 * pi * dystanse['Jowisz'] / okresy_obr['Jowisz'],
              'Saturn': 2 * pi * dystanse['Saturn'] / okresy_obr['Saturn'],
              'Uran': 2 * pi * dystanse['Uran'] / okresy_obr['Uran'],
              'Neptun': 2 * pi * dystanse['Neptun'] / okresy_obr['Neptun']}

predkosci = {'Merkury': interfejs.pred_input['Merkury'] * np.power(10, interfejs.pred_pot_input['Merkury'], dtype='float64'),
              'Wenus': interfejs.pred_input['Wenus'] * np.power(10, interfejs.pred_pot_input['Wenus'], dtype='float64'),
              'Ziemia': interfejs.pred_input['Ziemia'] * np.power(10, interfejs.pred_pot_input['Ziemia'], dtype='float64'),
              'Mars': interfejs.pred_input['Mars'] * np.power(10, interfejs.pred_pot_input['Mars'], dtype='float64'),
              'Jowisz': interfejs.pred_input['Jowisz'] * np.power(10, interfejs.pred_pot_input['Jowisz'], dtype='float64'),
              'Saturn': interfejs.pred_input['Saturn'] * np.power(10, interfejs.pred_pot_input['Saturn'], dtype='float64'),
              'Uran': interfejs.pred_input['Uran'] * np.power(10, interfejs.pred_pot_input['Uran'], dtype='float64'),
              'Neptun': interfejs.pred_input['Neptun'] * np.power(10, interfejs.pred_pot_input['Neptun'], dtype='float64')}

ped = {'Merkury': np.array([0, predkosci['Merkury'] * masy['Merkury'], 0]),
              'Wenus': np.array([0, predkosci['Wenus'] * masy['Wenus'], 0]),
              'Ziemia': np.array([0, predkosci['Ziemia'] * masy['Ziemia'], 0]),
              'Mars': np.array([0, predkosci['Mars'] * masy['Mars'], 0]),
              'Jowisz': np.array([0, predkosci['Jowisz'] * masy['Jowisz'], 0]),
              'Saturn': np.array([0, predkosci['Saturn'] * masy['Saturn'], 0]),
              'Uran': np.array([0, predkosci['Saturn'] * masy['Saturn'], 0]),
              'Neptun': np.array([0, predkosci['Neptun'] * masy['Neptun'], 0])}


#       #       #           #           #       Koordynaty do animacji
# merkury
x_merkury = interfejs.dyst_input['Merkury'] * np.power(10, (interfejs.dyst_pot_input['Merkury'] - 9), dtype='float64')

# wenus
x_wenus = interfejs.dyst_input['Wenus'] * np.power(10, (interfejs.dyst_pot_input['Wenus'] - 9), dtype='float64')

# ziemia
x_ziemi = interfejs.dyst_input['Ziemia'] * np.power(10, (interfejs.dyst_pot_input['Ziemia'] - 9), dtype='float64')

# mars
x_mars = interfejs.dyst_input['Mars'] * np.power(10, (interfejs.dyst_pot_input['Mars'] - 9), dtype='float64')

# jowisz
x_jowisz = interfejs.dyst_input['Jowisz'] * np.power(10, (interfejs.dyst_pot_input['Jowisz'] - 9), dtype='float64')

# saturn
x_saturn = interfejs.dyst_input['Saturn'] * np.power(10, (interfejs.dyst_pot_input['Saturn'] - 9), dtype='float64')

# uran
x_uran = interfejs.dyst_input['Uran'] * np.power(10, (interfejs.dyst_pot_input['Uran'] - 9), dtype='float64')

# neptun
x_neptun = interfejs.dyst_input['Neptun'] * np.power(10, (interfejs.dyst_pot_input['Neptun'] - 9), dtype='float64')
