import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# PMF do dado
dados = [1,2,3,4,5,6,6,6,3,2,1,4,6,5,3,2,2,6,1,4]
s = pd.Series(dados)
pmf = s.value_counts(normalize=True).sort_index()
print("PMF:\n", pmf)

pmf.plot(kind="bar")
plt.title("PMF - Dado")
plt.xlabel("Número no dado")
plt.ylabel("Probabilidade")
plt.savefig("images/pmf_dado.png")
plt.show()

# CDF do dado
cdf_dado = pmf.cumsum()
print("CDF:\n", cdf_dado)

cdf_dado.plot(drawstyle="steps-post", marker="o")
plt.title("CDF - Dado (discreto)")
plt.xlabel("Número no dado")
plt.ylabel("Probabilidade acumulada")
plt.savefig("images/cdf_dado.png")
plt.show()

# PDF da normal
x = np.linspace(140, 200, 500)
pdf = norm.pdf(x, loc=170, scale=10)

plt.plot(x, pdf)
plt.title("PDF - Altura (Normal(170,10))")
plt.xlabel("Altura (cm)")
plt.ylabel("Densidade")
plt.savefig("images/pdf_normal.png")
plt.show()

# CDF da normal
cdf = norm.cdf(x, loc=170, scale=10)

plt.plot(x, cdf)
plt.title("CDF - Altura (Normal(170,10))")
plt.xlabel("Altura (cm)")
plt.ylabel("Probabilidade acumulada")
plt.savefig("images/cdf_normal.png")
plt.show()
