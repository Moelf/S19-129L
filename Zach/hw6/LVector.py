import math
import numpy as np
from scipy.constants import c

class LVector:
	def __init__(self,vector):
		self.LVector=np.array(vector)
			
		self.x0=self.LVector[0]
		self.x1=self.LVector[1]
		self.x2=self.LVector[2]
		self.x3=self.LVector[3]
		

	def __str__(self):
		return "x0 = {0} \nx1 = {1} \nx2 = {2} \nx3 = {3}".format(self.x0,self.x1,self.x2,self.x3)

	def __add__(self,other):		
		x0 = self.x0 + other.x0
		x1 = self.x1 + other.x1
		x2 = self.x2 + other.x2
		x3 = self.x3 + other.x3

		added=list([x0,x1,x2,x3])
		return LVector(added)
	
	def __sub__(self,other):
		x0 = self.x0 - other.x0
		x1 = self.x1 - other.x1
		x2 = self.x2 - other.x2
		x3 = self.x3 - other.x3

		subtracted=list([x0,x1,x2,x3])
		return LVector(subtracted)

	def __mul__(self,other):
		if type(other) == type(self):
			inner_prod = self.x0*other.x0-self.x1*other.x1-self.x2*other.x2-self.x3*other.x3
			return(inner_prod)
		elif type(other) == type(1) or type(other) == type(1.0):
			scal_prod = other*np.array([self.x0,self.x1,self.x2,self.x3])
			return(LVector(scal_prod))

	def __rmul__(self,other):
		return self.__mul__(other)

	def square(self):
		return self.__mul__(self)
	
	def set_x0(self,other):
		return LVector([other,self.x1,self.x2,self.x3])
	def set_x1(self,other):
		return LVector([self.x0,other,self.x2,self.x3])
	def set_x2(self,other):
		return LVector([self.x0,self.x1,other,self.x3])
	def set_x3(self,other):
		return LVector([self.x0,self.x1,self.x2,other])

	def get_rlength(self):
		return sum([self.x1**2,self.x2**2,self.x3**2])

	def get_rtlength(self):
		return sum([self.x1**2,self.x2**2])

	def get_r(self):
		return np.array([self.x1,self.x2,self.x3])
	def get_rt(self):
		return np.array([self.x1,self.x2,0])

	def phi(self):
		angle=math.atan2(self.x2,self.x1)
		if angle<0:
			angle+=2*math.pi
		else:
			angle=angle
		return(angle)

	def theta(self):
		angle=math.acos(self.x3/math.sqrt(self.get_rlength() ))
		return(angle)

	def eta(self):
		return -math.log(math.tan(self.theta()/2))

	def Y(self):
		if self.x0-self.x3>0:
			return .5*math.log( (self.x0+self.x3)/ (self.x0-self.x3) )
		else:
			print('Unphysical four vector, invalid')

	def boost(self,beta):
		if beta[0]<1 and beta[1]<1 and beta[2]<1:
			beta_sq = beta[0]**2+beta[1]**2+beta[2]**2
			gamma = 1/math.sqrt(1-beta_sq)
			beta_dot_position = (beta[0]*self.x1+beta[1]*self.x2+beta[2]*self.x3)
			x0_prime = gamma*(self.x0- beta_dot_position )
			x1_prime = self.x1 + (-1*gamma*self.x0 + gamma**2/(1+gamma)*beta_dot_position)*beta[0]
			x2_prime = self.x2 + (-1*gamma*self.x0 + gamma**2/(1+gamma)*beta_dot_position)*beta[1]
			x3_prime = self.x3 + (-1*gamma*self.x0 + gamma**2/(1+gamma)*beta_dot_position)*beta[2]
			return LVector([x0_prime,x1_prime,x2_prime,x3_prime])
		else:
			print('Unphysical boost, please try again')





