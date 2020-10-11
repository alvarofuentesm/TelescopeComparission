import numpy as np 
import datetime

def to_pulgadas(mm):
	return(0.039370*mm)

def to_milimeter(pulgada):
	return(0.039370/pulgada)
 
class Telescope:
	
	def __init__(self, diameter, focal_length, type, name = ""):
		self.D = diameter
		self.DF = focal_length # distancia focal
		self.F = focal_length/diameter # razon focal
		self.type = type # tipo
		self.name = name

	def info(self):
		print("{name} {D}{DF} {type}".format(name = self.name, D=self.D, DF=self.DF, type = self.type))

	#Luminosidad del telescopio respecto del ojo humano medio, Ø pupila  ± 5,5 mm	
	def lum_respecto_ojo(self, out = False): 
		lum = np.round( (self.D/2)**2/(5.5/2)**2 , 2) 
		if (out):
			print("Iluminacion respecto al ojo humano: {lum} veces".format(lum=lum) )
		return lum

	def resolucion(self, out = False): # mientras mas pequeño mejor
		res = np.round(115.908 / self.D, 2)
		if (out):
			print("Resolucion: {res} arcosegundos (''arc)".format(res=res))
		return res		

	# Los OCULARES le permiten cambiar el aumento aparente de la imagen, formada por la lente o el espejo.
	def aumento_ocular(self, mm_ocular, barlow = 1, out = False):
		aum = self.DF/mm_ocular
		if (barlow != 1):
			aum = aum*barlow
		if (out):
			if (barlow != 1):
				print("Aumento proporcionado con ocular {mm_ocular}[mm] + barlow x{barlow} es {aum}x"
					.format(mm_ocular = mm_ocular, barlow=barlow, aum = aum) )
			else:
				print("Aumento proporcionado con ocular {mm_ocular}[mm] es {aum}x"
					.format(mm_ocular = mm_ocular, aum = aum) )
		return aum

	'''
	Cualquier telescopio se puede organizar para aumentar la imagen a casi cualquier tamaño,
	pero claro cuantos más aumentos... la imagen se verá más oscura, y por eso hay un límite, 
	de aumentos para cada telescopio ( En principio sea: ± 2,362 x Ø mm ) 
	'''
	def aumento_maximo(self, out = False):
		max = np.round(2.362*self.D,1)
		if (out):
			print("Aumento máximo práctico {max}x".format(max = max) )
		return max

	def get_F(self, out):
		if (out):
			print("F{F}".format(F = np.round(self.F,1) ))
		return np.round(self.F,1)

	def get_all(self, ocular_list, barlow_list = []): # example, ocular_list:  [20, 12.5]  barlow_list [1.5, 2] 
		self.info()
		self.lum_respecto_ojo(out=1)
		self.resolucion(out=1)
		self.aumento_maximo(out=1)
		self.get_F(out=1)

		for ocular in ocular_list: 
				self.aumento_ocular(ocular, out=1)

		if len(barlow_list) == 0:
			return
			
		for barlow in barlow_list:
			for ocular in ocular_list: 
				self.aumento_ocular(ocular, barlow, out=1)		

'''
EXAMPLES
'''
if __name__ == "__main__":
   
	## Refractor 60700
	t1 = Telescope(60, 700, "Refractor", "Old Telescope") #diameter, focal_length, type, name
	t1.get_all(ocular_list = [20, 12.5], barlow_list = [1.5, 3])
	print()

	## Reflector 76350 SOLARIX 76/350
	t2 = Telescope(76, 350, "Reflector", "SOLARIX 76/350")
	t2.get_all(ocular_list = [20, 4], barlow_list = [2])
	print()

	#Celestron FirstScope
	t3 = Telescope(76, 300, "Reflector", "Celestron FirstScope")
	t3.get_all(ocular_list = [20, 2.4])
	print()

	#Orion SpaceProbe 76AZ II
	t4 = Telescope(76, 700, "Reflector", "Orion SpaceProbe 76AZ II")
	t4.get_all(ocular_list = [25, 10])
	print()

	#Telescopio Orion Observer 80ST EQ
	t5 = Telescope(80, 400, "Reflector", "Orion Observer 80ST EQ")
	t5.get_all(ocular_list = [25, 10])

	print()
	#Celestron AstroMaster 114EQ
	t6 = Telescope(114, 1000, "Reflector", "Celestron AstroMaster 114EQ")
	t6.get_all(ocular_list = [20, 10])
