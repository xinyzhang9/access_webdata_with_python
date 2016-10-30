import numpy as np
import matplotlib.pyplot as plt

data = {
			"1":{
				"name":"work1",
				"minday":3,
				"maxday":5,
				"count":10
			},
			"2":{
				"name":"work2",
				"minday":4,
				"maxday":7,
				"count":15
			},
			"3":{
				"name":"work3",
				"minday":8,
				"maxday":10,
				"count":20
			},
			"4":{
				"name":"work4",
				"minday":13,
				"maxday":20,
				"count":5
			},
}

labels = [] # names
mindays = []
maxdays = []
counts = []


# divide pie into 360 parts
N = 360
theta = np.linspace(0.0,2*np.pi,N,endpoint=False)
radii_min = [] # inner radius
radii_max = [] # outer radius
width = [] # each angles occupied
legendColors = [] # legend colors

for key,value in sorted(data.items()):
	mindays.append(value['minday'])
	maxdays.append(value['maxday'])
	counts.append(value['count'])
	labels.append(value['name'])

# print labels
sumCounts = sum(counts) # total sum of counts
# print counts
timesFactor = [i*N/sumCounts for i in counts] # how many times should be copied ro fill the chart
# print timesFactor

for i in range(0,len(timesFactor)):
	for j in range(0,timesFactor[i]):
		radii_min.append(mindays[i])
		radii_max.append(maxdays[i])

width = 2 *np.pi/N # each width is 1 degree angle


ax = plt.subplot(111, projection='polar')
# bars1 for inner bars
bars1 = ax.bar(theta, radii_min, width=width, bottom=0.0, linewidth = 0) # must set linewidth = 0 to remove 360 lines
# bars2 for outer bars
bars2 = ax.bar(theta, radii_max, width=width, bottom=0.0, linewidth = 0)


# Use custom colors and opacity

# set inner bar
for r, bar in zip(radii_min, bars1):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)

# set outer bar
for r, bar in zip(radii_min, bars2):
    bar.set_facecolor(plt.cm.jet(r / 10.2)) # slmilar color to inner chart, so smart;)
    bar.set_alpha(0.5)

# set labels
for bar,ll in zip(bars2,labels):
	bar.set_label(ll)

# set legend colors
leg = ax.legend(loc='upper right', shadow=True)
for i in range(len(data)):
	leg.legendHandles[i].set_color(plt.cm.jet(mindays[i] / 10.2))

# show figure
plt.show()



