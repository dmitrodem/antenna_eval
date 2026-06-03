import matplotlib.pyplot as plt

# Data
arrays = ['1x1', '2x2', '4x4', '8x8']
gain = [5.5, 10.5, 14.9, 18.5]  # in dBi

# Create bar plot
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(arrays, gain, color='#1f77b4', edgecolor='black', width=0.5)

# Add values on top of bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f} dBi',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

# Labels and title
ax.set_xlabel('Размер решетки', fontsize=12, labelpad=10)
ax.set_ylabel('Коэффициент усиления ($dBi$)', fontsize=12, labelpad=10)
#ax.set_title('Total Realized Antenna Array Gain vs. Dimension at 10 GHz\n(Including Wilkinson Feed & Element Losses on RO4350B)', fontsize=14, pad=15, fontweight='bold')
ax.set_ylim(0, 22)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout and save
plt.tight_layout()
plt.savefig('../img/antenna_array_gain.png', dpi=300)
print("Plot successfully saved as antenna_array_gain.png")
