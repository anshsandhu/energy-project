import numpy as np


# function to convert solar energy and temperature to energy output
class SolarEnergy(self,V_oc,I_sc, temperature, solar_radiation,V_MPP,noct):

 # V_oc, I_sc Provided the the manufacturer; Temperature and radiation are available from data

	q = 1.602e-19  # Charge on an electron
	k = 1.3806e-23 # Boltzman Constant


def __init__(self,V_oc,I_sc,temperature,solar_radiation,noct):
	self.__I_o = I_sc/[np.exp(V_oc/(k*temperature/q)) - 1]
	self.__cell_temperature = temperature + (noct - 20)*solar/0.8 # in Watts
	

def __back_current(self):
	self.__I_o*(exp(q*) )	

def __I_o(self,V_oc,I_sc):
	V_t = k*temperature/q
	I_o = I_sc/[np.exp(V_oc/V_t) - 1]
	return 


def I_no_resistance(self, I_sc):
	I = I_sc - I_o()



def SolarEnergy(V_oc,I_sc, temperature, solar_radiation,V_MPP,noct):

 # V_oc, I_sc Provided the the manufacturer; Temperature and radiation are available from data

	q = 1.602e-19  # Charge on an electron
	k = 1.3806e-23 # Boltzman Constant

	cell_temperature = temperature + (noct - 20)*solar/800 # in Watts

	I_o = I_sc/[np.exp(V_oc/(k*cell_temperature/q)) - 1]
		
	V_t = k*cell_temperature/q

	I_o = I_sc/[np.exp(V_oc/V_t) - 1]

	I_back_current = I_o * [np.exp(q*V_MPP/k*cell_temperature) - 1]

	I_no_resistance = I_sc - I_back_current

	
