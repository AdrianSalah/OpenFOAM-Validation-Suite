import matplotlib.pylab as plt
import numpy as np

##########################################################################
# To run the script:
# 1) adapt case_name and the name of your sample function (assumed to be singleGraph, etc.
# 2) fill the formula to converte the experimental U_RMSx/y/z into turbulent kinetic energy k
# Note: a² is written as a**2 in Python, script has to be run in directory where your case folders are (run by "python3 loadAndPlotData.py")



# specify case names and sample locations
case_name = ['kEpsilon', 'kOmega', 'RNG']	# adapt case names 
sample_locations = ['X1', 'X3', 'X5']		# adapt names of your singleGraph functions


# load experimental data and extract uMean and uRMS at sample locations
exp_U = np.loadtxt('experimentData/kasagiExpUMean.txt', delimiter=" ")
exp_RMS = np.loadtxt('experimentData/kasagiExpURMS.txt', delimiter=" ")
iX1 = np.where(exp_U[:,0]==1.0)[0]
iX3 = np.where(exp_U[:,0]==3.0)[0]
iX5 = np.where(exp_U[:,0]==5.0)[0]
z_exp = np.column_stack((exp_U[iX1,1],exp_U[iX3,1],exp_U[iX5,1]))
U_exp = np.column_stack((exp_U[iX1,3],exp_U[iX3,3],exp_U[iX5,3]))
U_RMSx = np.column_stack((exp_RMS[iX1,3],exp_RMS[iX3,3],exp_RMS[iX5,3]))
U_RMSy = np.column_stack((exp_RMS[iX1,4],exp_RMS[iX3,4],exp_RMS[iX5,4]))
U_RMSz = np.column_stack((exp_RMS[iX1,5],exp_RMS[iX3,5],exp_RMS[iX5,5]))


##########################################################################
# compute k from U_RMSx/y/z here, U_RMS of different directions is stored in individual arrays

k_exp = (1/2)(U_RMSx**2+ U_RMSy**2+ U_RMSz**2)

##########################################################################

base_string = '/postProcessing/singleGraph'
all_names = case_name + ['experiment']

# load simulation data and create plots for different locations
n = 0
for sample in sample_locations:
	for case in case_name:
		path_k = case + base_string + sample + '/300/' + 'line_kMean.xy'
		path_U = case + base_string + sample + '/300/' + 'line_UMean.xy'
		data_U = np.loadtxt(path_U, delimiter="\t")
		data_k = np.loadtxt(path_k, delimiter="\t")
		z = data_U[:,0]
		U_x = data_U[:,1]
		k = data_k[:,1]

		plt.figure('U_Mean at '+sample)
		plt.plot(z,U_x)
		plt.ylabel('U_x (m/s)')
		plt.xlabel('z (m)')

		plt.figure('k_Mean at '+sample)
		plt.plot(z,k)
		plt.ylabel('k (m^2/s^2)')
		plt.xlabel('z (m)')

	# add legend to figures
	plt.figure('U_Mean at '+sample)
	plt.plot(z_exp[:,n],U_exp[:,n],'k')
	plt.legend(all_names)
	plt.figure('k_Mean at '+sample)
	plt.plot(z_exp[:,n],k_exp[:,n],'k')
	plt.legend(all_names)
	n += 1


plt.show()



