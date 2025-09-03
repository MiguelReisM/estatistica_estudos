import pandas as pd
import matplotlib.pyplot as plt

# Exemplo: dataset inventado de idades
idades = [18, 22, 20, 19, 23, 21, 25, 30, 18, 22, 24, 27, 21, 19]
s = pd.Series(idades)

print("Resumo estatístico:")
print(s.describe())

# Histograma
plt.hist(s, bins=6, edgecolor="black")
plt.title("Distribuição de Idades")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.savefig("images/cap1_hist.png")
plt.show()
