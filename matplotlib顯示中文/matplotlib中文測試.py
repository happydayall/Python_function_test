import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-regular.ttf')
mpl.rc('font' , family = 'Taipei Sans TC Beta')

x = np.linspace(-2 * np.pi , 3 * np.pi + 3 , 100)

y = np.sin(x)  + np.cos(x)

plt.title('É¸ÂêÂ¬»î')
plt.plot(x , y)
plt.show()