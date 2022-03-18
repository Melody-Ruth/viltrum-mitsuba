

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'non-zero/no samples', 'non-zero/1 samples', 'zero/no samples', 'zero/1 sample', 'non-zero/no samples (zero approx)', 'non-zero/1 sample (zero approx)', 'non-zero/2 samples (zero approx)', 'zero/no samples (zero approx)', 'zero/1 sample (zero approx)', 'zero/2 samples (zero approx)'
#labels = 'non-zero/no samples', 'non-zero/1 samples', 'zero/no samples', 'zero/2 samples', 'non-zero/no samples (zero approx)', 'non-zero/1 sample (zero approx)', 'non-zero/2 samples (zero approx)', 'zero/no samples (zero approx)', 'zero/1 sample (zero approx)', 'zero/2 samples (zero approx)'
#sizes = [3997888, 896485, 4220854, 1941575, 17196, 137021, 305988, 768624, 3000799, 5454268]
#sizes = [3772521, 841374, 4446221, 1996686, 14056, 113815, 250475, 771764, 3024005, 5509781]
#sizes = [3771868, 841696, 146, 4446874, 1996364, 4270, 14026, 113845, 250592, 771794, 3023975, 5509664]
sizes = [3958597, 871811, 1018861, 275545, 56402, 161707, 306083, 3970702, 4666817, 5458301]
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0) 
#explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', pctdistance=0.8,
        shadow=False, labeldistance=1.3, startangle=50)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#plt.text(0.5, 0.9, "Types that are barely even present (0.0%) at all: non-zero/1 sample (183), zero/1 sample (4233)")
plt.text(0.5, 0.9, "Types that are barely even present (0.0%) at all: non-zero/2 sample (114), zero/2 samples (174)")

plt.show()
