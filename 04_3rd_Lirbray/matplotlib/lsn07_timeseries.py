##encoding=utf8

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
from datetime import datetime, date, timedelta

def example1():
	"""date only axis, by month
	"""
	start_date, td = date(2014,1,1), timedelta(1)
	x = [start_date + i * td for i in range(365)]
	y = np.random.randn(365)

	fig, ax = plt.subplots()

	ax.plot(x, y)
	
	fig.autofmt_xdate() # automatically format x axis

	plt.xticks(rotation="vertical")
	plt.show()

# example1()

def example2():
	"""date only axis by quarter
	"""
	start_date, td = date(2014,1,1), timedelta(1)
	x = [start_date + i * td for i in range(365)]
	y = np.random.randn(365)

	fig, ax = plt.subplots()

	ax.plot(x, y)
	
	months = MonthLocator([1,4,7,10])
	monthFmt = DateFormatter("%Y-%m")
	ax.xaxis.set_major_locator(months)		# set major locator
	ax.xaxis.set_major_formatter(monthFmt)	# set major formatter

	fig.autofmt_xdate() # automatically format x axis

	plt.xticks(rotation="vertical")
	plt.show()

# example2()

def example3():
	"""Customize major tick and minor tick
	"""
	### generate data
	date1 = date(1995, 1, 1)
	date2 = date(2004, 4, 12)
	total_days = (date2 - date1).days

	dates = [date1 + i * timedelta(1) for i in range(total_days)]
	opens = np.random.randn(total_days)

	fig, ax = plt.subplots()
	ax.plot_date(dates, opens, "-")

	# format the ticks
	years = YearLocator()   # every year
	months = MonthLocator([4,7,10])  	# range(1,13) = everymonth, [4,7,10] means draw a tick at
										# 3, 6, 9 = every quarter
	yearsFmt = DateFormatter("%Y") # the text on time axis major ticker
	monthFmt = DateFormatter("%m") # the text on time axis minor ticker


	ax.xaxis.set_major_locator(years)		# set major locator
	ax.xaxis.set_major_formatter(yearsFmt)	# set major formatter
	ax.xaxis.set_minor_locator(months)		# set minor locator
	ax.xaxis.set_minor_formatter(monthFmt)	# set minor formatter
	ax.autoscale_view()

	# format the coords message box
	def price(x): return "$%1.2f"%x
	ax.fmt_xdata = DateFormatter("%Y-%m-%d")
	ax.fmt_ydata = price
# 	fig.autofmt_xdate() # automatically format x axis

	plt.ylim([-10, 10])	# set y axis limit
	
	# 只打开x的grid
	ax.grid(which="major", axis="x", color="gray", linestyle="-", linewidth=2) # set major grid
	ax.grid(which="minor", axis="x", color="black", linestyle="--", linewidth=1) # set minor grid

# 	plt.xticks(rotation="vertical") # if you only have major tick to rotate, you can use this
	plt.setp( ax.xaxis.get_majorticklabels(), rotation=90 )
	plt.setp( ax.xaxis.get_minorticklabels(), rotation=90 )
	plt.show()

example3()
