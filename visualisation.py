import matplotlib.pyplot as plt
import pandas as pd

# Analyse 1: Top 10 États
data1 = []
with open('resultats/analyse1-complet.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 2:
            etat = parts[0]
            temp = float(parts[1])
            data1.append({'Etat': etat, 'Temperature': temp})

df1 = pd.DataFrame(data1).head(10)
plt.figure(figsize=(12, 6))
plt.bar(df1['Etat'], df1['Temperature'], color='orange')
plt.title('Top 10 États - Température Moyenne (°F)', fontsize=16)
plt.xlabel('État')
plt.ylabel('Température (°F)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('resultats/graph1-temperatures.png', dpi=300)
plt.close()

# Analyse 3: Précipitations
data3 = []
with open('resultats/analyse3-precipitations.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 3:
            mois = parts[0].replace('Mois_', '')
            total = float(parts[1].split('=')[1].replace(',', ''))
            data3.append({'Mois': int(mois), 'Precipitations': total})

df3 = pd.DataFrame(data3).sort_values('Mois')
plt.figure(figsize=(12, 6))
plt.plot(df3['Mois'], df3['Precipitations'], marker='o', linewidth=2, color='blue')
plt.title('Précipitations Totales par Mois', fontsize=16)
plt.xlabel('Mois')
plt.ylabel('Précipitations')
plt.grid(True, alpha=0.3)
plt.xticks(range(1, 13))
plt.tight_layout()
plt.savefig('resultats/graph2-precipitations.png', dpi=300)
plt.close()

# Analyse 4: Saisons
saisons = []
temps = []
precips = []
with open('resultats/analyse4-saisons.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 4:
            saisons.append(parts[0])
            temp = float(parts[1].split('=')[1].replace(',', ''))
            precip = float(parts[2].split('=')[1].replace(',', ''))
            temps.append(temp)
            precips.append(precip)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.bar(saisons, temps, color=['brown', 'green', 'gray', 'orange'])
ax1.set_title('Température par Saison', fontsize=14)
ax1.set_ylabel('Température (°F)')
ax2.bar(saisons, precips, color=['brown', 'green', 'gray', 'orange'])
ax2.set_title('Précipitations par Saison', fontsize=14)
ax2.set_ylabel('Précipitations')
plt.tight_layout()
plt.savefig('resultats/graph3-saisons.png', dpi=300)
plt.close()

print("✅ 3 graphiques créés!")