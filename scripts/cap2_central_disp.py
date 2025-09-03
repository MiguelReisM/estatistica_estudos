import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode

# Dados
notas = [5.5, 7.0, 8.5, 9.0, 6.0, 7.5, 8.0, 6.5, 7.0, 9.5,
         8.0, 7.0, 6.0, 8.5, 5.0, 9.0, 7.5, 8.0, 6.5, 7.0]
s = pd.Series(notas)

# Centralidade
media = s.mean()
mediana = s.median()
try:
    moda = mode(notas)
except Exception:
    # se houver empate de modas, tratamos com pandas:
    moda = s.mode().tolist()

# Dispersão
variancia = s.var(ddof=1)
desvio_padrao = s.std(ddof=1)
amplitude = s.max() - s.min()
q1 = s.quantile(0.25)
q3 = s.quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers = s[(s < limite_inferior) | (s > limite_superior)].tolist()

print("Média:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Variância:", variancia)
print("Desvio-padrão:", desvio_padrao)
print("Amplitude:", amplitude)
print("Q1:", q1, "Q3:", q3, "IQR:", iqr)
print("Limites IQR:", limite_inferior, limite_superior)
print("Outliers:", outliers)

# Boxplot
plt.boxplot(notas, vert=True, patch_artist=True)
plt.title("Boxplot das Notas")
plt.ylabel("Nota")
plt.grid(axis="y", alpha=0.4)
plt.savefig("images/cap2_boxplot.png")
plt.show()
