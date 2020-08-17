import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
import os
from datetime import datetime , timedelta
path = 'E:\\My Projects\\2019 Works\\Python\\Sublime\\Matplotlib'
os.chdir(path)


# Plotting Dates
dates = [datetime(2019,5,1),
		 datetime(2019,5,2),
		 datetime(2019,5,3),
		 datetime(2019,5,4),
		 datetime(2019,5,5),
		 datetime(2019,5,6),
		 datetime(2019,5,7),
		 datetime(2019,5,8)]
y = [100 , 200 , 134 , 10 , 350 , 51 , 155 , 1500]

# Such a nasty plot!!
plt.plot_date(dates , y , linestyle = '--')
plt.show(False)
plt.pause(3)

# Now, we can fix it
# plt.gcf is for get current figure, and there are a few methods to change our pyplot!
plt.plot_date(dates , y , linestyle = '--')
plt.gcf().autofmt_xdate()
plt.show(False)
plt.pause(3)

# Now, we can have our own formats by matplotlib dates
from matplotlib import dates as mldates
plt.plot_date(dates , y , linestyle = '--')
formatter = mldates.DateFormatter('%b , %d , %Y')
# gca is the convention for get current axis
plt.gca().xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate()
plt.show(False)
plt.pause(3)
