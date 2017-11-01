from nodoHabitacion import nodoHabitacion
class Habitacion:
	def __init__(self):
		self.cuarto=None
	def agregar(self,habitacion,piso):
		habitacion = nodoHabitacion(habitacion,piso,None,None)
		if self.cuarto==None:
			self.cuarto=habitacion
			self.cuarto.der=self.cuarto
			self.cuarto.izq=self.cuarto
			return True
		else:
			temporal = self.cuarto.der
			while temporal!=self.cuarto:
				if temporal.habitacion==habitacion:
					if temporal.piso==piso:
						return False
					elif temporal.piso<piso:
						temporal.izq.der=habitacion
						temporal.izq=habitacion
						


				elif temporal.habitacion>habitacion:
				else:
					return False
				temporal=temporal.der