from nodoUsuario import nodoUsuario
from hojabitacora import hojabitacora
class Usuario:
	def __init__(self):
		self.lista =None


	def agregar(self,user,passwd,direccion,telefono,edad,es_super):
		usu = nodoUsuario(user,passwd,direccion,telefono,edad,es_super,None,None,None)
		if self.lista==None:
			self.lista = usu
			return "Agregado correctamente"
		else:
			temporal = self.lista
			while temporal.der!=None:
				if temporal.usuario>usu.usuario:
					if temporal.izq==None:
						self.lista.izq=usu
						usu.der=self.lista
						self.lista=usu
					else:
						temporal.izq.der=usu
						usu.izq=temporal.izq
						usu.der=temporal
						temporal.izq=usu
					return "Agregado correctamente"
				elif temporal.usuario==usu.usuario:
					return "Este usuario ya existe"
				temporal=temporal.der
			if temporal.usuario<usu.usuario:
				usu.izq=temporal
				temporal.der=usu
			elif temporal.usuario>usu.usuario:
				if temporal.izq==None:
					self.lista.izq=usu
					usu.der=self.lista
					self.lista=usu
				else:
					temporal.izq.der=usu
					usu.izq=temporal.izq
					usu.der=temporal
					temporal.izq=usu
				return "Agregado correctamente"
			else:
				return "Este usuario ya existe"
			return "Agregado correctamente"


	def login(self,user,passwd):
		sesion = self.lista
		while sesion!=None:
			if sesion.usuario==user and sesion.passwd==passwd:
				if sesion.es_super=="si":
					return "2"
				return "1"
			sesion=sesion.der
		return "0"

	def eliminarUsuario(self,usuario):
		if self.delete(usuario)==True:
			return "eliminado satisfactoriamente"
		else:
			return "este usuario no pudo ser eliminado"

	def delete(self,usuario):
		if self.lista.usuario==usuario:
			if self.lista.der!=None:
				self.lista=self.lista.der
				self.lista.izq=None
			else:
				self.lista=None
			return True
		else:
			temporal= self.lista
			while temporal!=None:
				if temporal.user==usuario:
					if temporal.izq==None:
						if temporal.der==None:
							sesion.lista=None
						else:
							self.lista=self.lista.der
							self.lista.izq=None
					elif temporal.der==None:
						temporal.izq.der==None
					else:
						temporal.izq.der=temporal.der
						temporal.der.izq=temporal.izq
					return True
				temporal=temporal.der
			return False

	def modificar(self,usuario,passwd):
		if self.delete(usuario)==True:
			self.agregarUsuario(usuario,passwd)
			return "modificado satisfactoriamente"
		else:
			return "el usuario no se logro modificar"

	def bitacora(self,usuario,gastado,habitacion,ingreso,salida,tarjeta):
		temporal = self.lista
		while temporal.der!=None:
			if temporal.usuario==usuario:
				return self.add_bitacora(temporal,gastado,habitacion,ingreso,salida,tarjeta)
			temporal=temporal.der
		if temporal.usuario==usuario:
			return self.add_bitacora(temporal,gastado,habitacion,ingreso,salida,tarjeta)
		else:
			return "no se ha podido encontrar el usuario"

	def add_bitacora(self,usu,gastado,habitacion,ingreso,salida,tarjeta):
		if usu.bitacora==None:
			tmp=nodobitacora(gastado,habitacion,ingreso,salida,tarjeta)
			hb = hojabitacora()
			usu.bitacora=hb.agregar(tmp)
			return "agregado correctamente"
		else:
			return "esto es medio prueba"






	def visualizarUsuarios(self):
		retorno = "digraph g {\n"
		if self.lista==None:
			retorno=retorno+"lista vacia;\n}"
		else:
			temporal = self.lista
			if temporal.der==None:
				retorno =retorno + temporal.usuario+";}"
			else:
				while temporal.der!=None:
					retorno = retorno + temporal.usuario+ "->" + temporal.der.usuario+";\n"
					retorno = retorno + temporal.der.usuario+ "->" + temporal	.usuario+";\n"
					temporal= temporal.der
				retorno=retorno +"}"
		return retorno








