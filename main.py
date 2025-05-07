from standings import FinalResult
from f1_data import graficar_standings_combinados, handleInput
import matplotlib.pyplot as plt

handleInput(FinalResult)
graficar_standings_combinados()
plt.show()
