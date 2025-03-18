import matplotlib.pyplot as plt

######################################################################
# rcParam control begin
######################################################################
def customizer():
	figure = {
		# 'figsize' : (5*2.5, 5*2.5),   ## figure size in inches
		'dpi'     : 100                 ## figure dots per inch
		}
	
	axes = {
		'titlesize' : 'large'           ## fontsize of the axes title
		}
	
	ticks = {
		'labelsize' : 'small'         ## fontsize of the tick labels
		}
	
	legend = {
		'fontsize' : 'small'
	}

	font = {
		# 'family' : 'Helvetica'
		'family' : 'sans-serif'

	    # 'weight' : 500,
	    # 'size'   : 18
	    }
	
	plt.rc('font', **font)        # controls default text sizes
	plt.rc('xtick', **ticks)      # fontsize of the tick labels
	plt.rc('ytick', **ticks)      # fontsize of the tick labels
	plt.rc('figure', **figure)    # fontsize of the tick labels
	plt.rc('legend', **legend)    # fontsize of the legends
	plt.rc('axes', **axes)        # fontsize of the axes title
