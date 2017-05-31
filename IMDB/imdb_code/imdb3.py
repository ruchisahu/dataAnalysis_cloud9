
#Mini Project Popular Animals

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

import numpy as np

fig=plt.figure()

animals = ('Dog', 'Cat', 'Tiger', 'Dolphin', 'Wolf','Penguin','Horse','Elephant')

y_pos = np.arange(len(animals))

percentage = [13, 8, 7, 5, 5,4,4,3]



#plot a bar graph(use bar or barh anything is fine,barh is use for horizontal graph)

plt.barh(y_pos,percentage, align='center',color='green')

#add text in the y axis

plt.yticks(y_pos,animals)

#add text in the x axis

plt.xlabel('Voting Percentage')

#Adds a title

plt.title('Top Ten Best Animals')

#show plot and save figure

plt.show()
fig.savefig('animals.png')
