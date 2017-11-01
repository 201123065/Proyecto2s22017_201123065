from nodobitacora import nodobitacora
import time
class bitacora:
	def __init__(self):
		self.mi_bitacora=None

	def cargar(self,transaccion):
		proceso=str(time.strftime("%d/%m/%Y"))+str(time.strftime("%H:%M:%S"))
		nuevo=nodobitacora(transaccion,proceso,None)
		if self.mi_bitacora==None:
			self.mi_bitacora=nuevo
		else:
			nuevo.siguiente=self.mi_bitacora
			self.mi_bitacora=nuevo

	def historial(self):
		temporal=self.bitacora
		if temporal.siguiente!=None:
			retorno=""	
			while temporal!=None:
				retorno=retorno+temporal.transaccion+":"+temporal.fecha+","
				temporal=temporal.siguiente
			return "{" + retorno +"};"
		elif temporal!=None:
			return "{"+temporal.transaccion+":"+temporal.fecha +"}"
		else:
			return "{}"

	def graficar_historia(self):
		temporal=self.bitacora
		if temporal.siguiente!=None:
			retorno="digraph g{"	
			while temporal!=None:
				retorno=retorno+temporal.transaccion+"->"+temporal.fecha+";"
				temporal=temporal.siguiente
			return retorno +"}"
		elif temporal!=None:
			return "digraph g {"+temporal.transaccion+"->"+temporal.fecha +";}"
		else:
			return "digraph g{}"

