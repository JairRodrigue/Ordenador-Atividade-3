import matplotlib.pyplot as plt
import numpy as np

# Dados
categorias = ["AWS - Python (BS)", "AWS - JavaScript (BS)", "AWS - Python (MS)", "AWS - JavaScript (MS)",
              "Codespace - Python (BS)", "Codespace - JavaScript (BS)", "Codespace - Python (MS)", "Codespace - JavaScript (MS)",
              "Replit - Python (BS)", "Replit - JavaScript (BS)", "Replit - Python (MS)", "Replit - JavaScript (MS)"]

medias_tempo = [16196.63, 1585.73, 51.31, 18.52, 10718.67, 402.11, 33.04, 15.05, 17974.28, 426.63, 52.7, 18.22]
medianas_tempo = [16126.8, 1586.47, 51.75, 18.3, 10710.58, 343.28, 30.93, 14.18, 18108.57, 421.9, 49.64, 18.92]

medias_memoria = [12612, 6505.74, 13004, 6238, 15604.8, 5565.49, 16691.2, 6218.68, 17331.2, 5409.91, 17664, 6108.08]
medianas_memoria = [12612, 6405.03, 13004, 6238, 16384, 5378.52, 16640, 6218.67, 17408, 5352.37, 17664, 6065.43]

indices = np.arange(len(categorias))
largura = 0.35

# Criando o gráfico
fig, ax1 = plt.subplots(figsize=(15, 8))

# Gráfico de tempo
ax1.plot(indices, medias_tempo, label='Média - Tempo (ms)', marker='o', linestyle='-', color='blue')
ax1.plot(indices, medianas_tempo, label='Mediana - Tempo (ms)', marker='s', linestyle='--', color='cyan')
ax1.set_ylabel('Tempo (ms)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xticks(indices)
ax1.set_xticklabels(categorias, rotation=45, ha='right')
ax1.set_title('Média e Mediana de Tempo e Memória em Diferentes Plataformas')

# Criando um segundo eixo para a memória
ax2 = ax1.twinx()
ax2.plot(indices, medias_memoria, label='Média - Memória (KB)', marker='o', linestyle='-', color='green')
ax2.plot(indices, medianas_memoria, label='Mediana - Memória (KB)', marker='s', linestyle='--', color='lime')
ax2.set_ylabel('Memória (KB)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Adicionando as legendas
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), bbox_transform=ax1.transAxes)

plt.tight_layout()
plt.show()
