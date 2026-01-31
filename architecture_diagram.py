import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

ax.text(5, 11.5, 'Architecture du Système Hadoop - Analyse Météo', 
        ha='center', fontsize=18, weight='bold', color='#2c3e50')

box1 = FancyBboxPatch((1, 9.5), 3, 1.2, boxstyle="round,pad=0.1", 
                       edgecolor='#3498db', facecolor='#ecf0f1', linewidth=2)
ax.add_patch(box1)
ax.text(2.5, 10.3, 'Données Source', ha='center', fontsize=11, weight='bold')
ax.text(2.5, 9.9, 'weather.csv (16,744 lignes)', ha='center', fontsize=9)

arrow1 = FancyArrowPatch((2.5, 9.5), (2.5, 8.5), arrowstyle='->', mutation_scale=20, linewidth=2, color='#7f8c8d')
ax.add_patch(arrow1)

box2 = FancyBboxPatch((0.5, 7), 4, 1.3, boxstyle="round,pad=0.1", edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=2)
ax.add_patch(box2)
ax.text(2.5, 7.9, 'HDFS - Stockage Distribué', ha='center', fontsize=11, weight='bold')
ax.text(2.5, 7.5, '/user/hadoop/meteo/input/', ha='center', fontsize=9)

arrow2 = FancyArrowPatch((2.5, 7), (2.5, 6), arrowstyle='->', mutation_scale=20, linewidth=2, color='#7f8c8d')
ax.add_patch(arrow2)

box3a = FancyBboxPatch((0.3, 4.5), 2.8, 1.3, boxstyle="round,pad=0.08", edgecolor='#27ae60', facecolor='#d5f4e6', linewidth=2)
ax.add_patch(box3a)
ax.text(1.7, 5.5, 'MAPPER', ha='center', fontsize=10, weight='bold')
ax.text(1.7, 5.15, '• Lecture CSV', ha='center', fontsize=8)
ax.text(1.7, 4.85, '• Extraction', ha='center', fontsize=8)

box3b = FancyBboxPatch((3.6, 4.5), 2.8, 1.3, boxstyle="round,pad=0.08", edgecolor='#f39c12', facecolor='#fef5e7', linewidth=2)
ax.add_patch(box3b)
ax.text(5, 5.5, 'SHUFFLE', ha='center', fontsize=10, weight='bold')
ax.text(5, 5.15, '• Groupement', ha='center', fontsize=8)

box3c = FancyBboxPatch((6.9, 4.5), 2.8, 1.3, boxstyle="round,pad=0.08", edgecolor='#8e44ad', facecolor='#ebdef0', linewidth=2)
ax.add_patch(box3c)
ax.text(8.3, 5.5, 'REDUCER', ha='center', fontsize=10, weight='bold')
ax.text(8.3, 5.15, '• Agrégation', ha='center', fontsize=8)

arrow3a = FancyArrowPatch((3.1, 5.15), (3.6, 5.15), arrowstyle='->', mutation_scale=15, linewidth=1.5, color='#7f8c8d')
ax.add_patch(arrow3a)
arrow3b = FancyArrowPatch((6.4, 5.15), (6.9, 5.15), arrowstyle='->', mutation_scale=15, linewidth=1.5, color='#7f8c8d')
ax.add_patch(arrow3b)

box4 = FancyBboxPatch((0.3, 3), 9.4, 1.2, boxstyle="round,pad=0.08", edgecolor='#16a085', facecolor='#d1f2eb', linewidth=2)
ax.add_patch(box4)
ax.text(5, 3.85, '4 Analyses MapReduce', ha='center', fontsize=10, weight='bold')
ax.text(2.4, 3.35, '1. Temp/État', ha='center', fontsize=8)
ax.text(4.8, 3.35, '2. Min/Max', ha='center', fontsize=8)
ax.text(7.1, 3.35, '3. Précip/Mois', ha='center', fontsize=8)
ax.text(9.3, 3.35, '4. Saisons', ha='center', fontsize=8)

arrow4 = FancyArrowPatch((5, 3), (5, 2.2), arrowstyle='->', mutation_scale=20, linewidth=2, color='#7f8c8d')
ax.add_patch(arrow4)

box5 = FancyBboxPatch((0.5, 0.8), 4, 1.3, boxstyle="round,pad=0.1", edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=2)
ax.add_patch(box5)
ax.text(2.5, 1.7, 'Résultats HDFS', ha='center', fontsize=11, weight='bold')
ax.text(2.5, 1.3, '/output/analyse*/', ha='center', fontsize=9)

arrow5 = FancyArrowPatch((4.5, 1.4), (5.5, 1.4), arrowstyle='->', mutation_scale=20, linewidth=2, color='#7f8c8d')
ax.add_patch(arrow5)

box6 = FancyBboxPatch((5.5, 0.8), 4, 1.3, boxstyle="round,pad=0.1", edgecolor='#9b59b6', facecolor='#f4ecf7', linewidth=2)
ax.add_patch(box6)
ax.text(7.5, 1.7, 'Visualisation', ha='center', fontsize=11, weight='bold')
ax.text(7.5, 1.3, 'Python + Matplotlib', ha='center', fontsize=9)

box_infra = FancyBboxPatch((0.3, 0.05), 9.4, 0.5, boxstyle="round,pad=0.05", edgecolor='#34495e', facecolor='#ecf0f1', linewidth=1.5)
ax.add_patch(box_infra)
ax.text(5, 0.3, 'Infrastructure: Docker | Hadoop 2.9.2 | YARN | Java 1.8', ha='center', fontsize=8, style='italic')

plt.tight_layout()
plt.savefig('architecture_systeme.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✅ Image créée: architecture_systeme.png")