from celdas import celdas
from nodo_AB import nodo_AB
class hojabitacora:
	def __init__(self):
		self.nodo=None

	def agregar(self,bitacora):
		if self.nodo==None:
			self.nodo=celdas(None,bitacora,None,None,None,None,None,None,None)
			return "agregado satisfactoriamente"
		else:
			self.nodo=self.recursivo(self.nodo,bitacora).arbol

	def recursivo(self,nodo,bitacora):
# ---------------------------------1---------------------------------
		if nodo.n1==None:
			return nodo_AB(celdas(None,bitacora,None,None,None,None,None,None,None),False)
		else:
			if nodo.n1.ingreso>bitacora.ingreso:
				if nodo.p1==None:
					if nodo.n2==None:
						return nodo_AB(celdas(None,bitacora,None,nodo.n1,None,None,None,None,None),False)
					elif nodo.n3==None:
						return nodo_AB(celdas(None,bitacora,None,nodo.n1,None,nodo.n2,None,None,None),False)
					elif nodo.n4==None:
						return nodo_AB(celdas(None,bitacora,None,nodo.n1,None,nodo.n2,None,nodo.n3,None),False)
					else:
						izq =  celdas(None,bitacora,None,nodo.n1,None,None,None,None,None)
						der =  celdas(None,nodo.n3,None,nodo.n4,None,None,None,None,None)
						raiz =  celdas(izq,nodo.n2,der,None,None,None,None,None,None)
						return nodo_AB(raiz,True)
				else:
					temp = self.recursivo(nodo.p1,bitacora)
					if temp.roto==False:
						return nodo_AB(nodo,False)
					else:
						if nodo.n2==None:
							tp= celdas(temp.arbol.p1,temp.arbol.n1,temp.arbol.p2,nodo.n1,nodo.p2,None,None,None,None)
							return nodo_AB(tp,False)
						elif nodo.n3==None:
							tp= celdas(temp.arbol.p1,temp.arbol.n1,temp.arbol.p2,nodo.n1,nodo.p2,nodo.n2,nodo.p3,None,None)
							return nodo_AB(tp,False)
						elif nodo.n4==None:
							tp= celdas(temp.arbol.p1,temp.arbol.n1,temp.arbol.p2,nodo.n1,nodo.p2,nodo.n2,nodo.p3,nodo.n3,nodo.p4)
							return nodo_AB(tp,False)
						else:
							izq =  celdas(temp.arbol.p1,temp.arbol.n1,temp.arbol.p2,nodo.n1,nodo.p2,None,None,None,None)
							der =  celdas(nodo.p3      ,nodo.n3      ,nodo.p4      ,nodo.n4,nodo.p5,None,None,None,None)
							raiz = celdas(izq          ,nodo.n2      ,  der        ,  None ,  None ,None,None,None,None)
							return nodo_AB(raiz,True)
			else:
# ---------------------------------2---------------------------------
				if nodo.n2==None:
					if nodo.p2==None:
						nodo.n2=bitacora
						return nodo_AB(nodo,False)
					else:
						temp = self.recursivo(nodo.p2,bitacora)
						if temp.roto==False:
							return nodo_AB(nodo,False)
						else:
							tp = celdas(nodo.p1, nodo.n1, temp.arbol.p1, temp.arbol.n1, temp.arbol.p2,None,None,None,None)
							return nodo_AB(tp,False)
				else:
					if nodo.n2.ingreso>bitacora.ingreso:
						if nodo.p2==None:
							if nodo.n3==None:
								return nodo_AB(celdas(None,nodo.n1,None,bitacora,None,nodo.n2,None,None   ,None),False)
							elif nodo.n4==None:
								return nodo_AB(celdas(None,nodo.n1,None,bitacora,None,nodo.n2,None,nodo.n3,None),False)
							else:
								izq = celdas(None,nodo.n1,None,bitacora,None,None,None,None,None)
								der = celdas(None,nodo.n3,None,nodo.n4 ,None,None,None,None,None)
								raiz =celdas(izq ,nodo.n2,der ,  None  ,None,None,None,None,None)
								return nodo_AB(raiz,True)
						else:
							temp = self.recursivo(nodo.p2,bitacora)
							if temp.roto==False:
								return nodo_AB(nodo,False)
							else:
								if nodo.n3==None:
									tp=celdas(nodo.p1,nodo.n1,temp.p1,temp.n1,temp.p2,nodo.n2,nodo.p3,None,None)
									return nodo_AB(tp,False)
								elif nodo.n4==None:
									tp= celdas(nodo.p1,nodo.n1,temp.p1,temp.n1,temp.p2,nodo.n2,nodo.p3,nodo.n3,nodo.p4)
									return nodo_AB(tp,False)
								else:
									izq =  celdas(nodo.p1,nodo.n1,temp.p1,temp.n1,temp.p2,None,None,None,None)
									der =  celdas(nodo.p3,nodo.n3,nodo.p4,nodo.n4,nodo.p5,None,None,None,None)
									raiz = celdas(izq    ,nodo.n2,  der  ,  None ,  None ,None,None,None,None)
									return nodo_AB(raiz,True)
# ---------------------------------3---------------------------------	
					else:
						if nodo.n3==None:
							if nodo.p3==None:
								nodo.n3=bitacora
								return nodo_AB(nodo,False)
							else:
								temp = self.recursivo(nodo.p3,bitacora)
								if temp.roto==False:
									return nodo_AB(nodo,False)
								else:
									tp = celdas(nodo.p1, nodo.n1, nodo.p2, nodo.n2, temp.arbol.p1,temp.arbol.n1,temp.arbol.p2,None,None)
									return nodo_AB(tp,False)
						else:
							if nodo.n3.ingreso>bitacora.ingreso:
								if nodo.p3==None:
									if nodo.n4==None:
										return nodo_AB(celdas(None,nodo.n1,None,nodo.n2,None,bitacora,None,nodo.n3,None),False)
									else:
										izq = celdas(None,nodo.n1,None,nodo.n2,None,None,None,None,None)
										der = celdas(None,nodo.n3,None,nodo.n4 ,None,None,None,None,None)
										raiz =celdas(izq ,bitacora,der ,  None  ,None,None,None,None,None)
										return nodo_AB(raiz,True)
								else:
									temp = self.recursivo(nodo.p3,bitacora)
									if temp.roto==False:
										return nodo_AB(nodo,False)
									else:
										if nodo.n4==None:
											tp=celdas(nodo.p1,nodo.n1,nodo.p2,nodo.n2,temp.arbol.p1,temp.arbol.n1,temp.arbol.p2,nodo.n3,nodo.p4)
											return nodo_AB(tp,False)
										else:
											izq =  celdas(nodo.p1,nodo.n1,nodo.p2,nodo.n2,temp.arbol.p1,None,None,None,None)
											der =  celdas(temp.arbol.p2,nodo.n3,nodo.p4,nodo.n4,nodo.p5,None,None,None,None)
											raiz = celdas(izq    ,temp.arbol.n1,  der  ,  None ,  None ,None,None,None,None)
											return nodo_AB(raiz,True)
# ---------------------------------4---------------------------------												
							else:
								if nodo.n4==None:
									if nodo.p4==None:
										nodo.n4=bitacora
										return nodo_AB(nodo,False)
									else:
										temp = self.recursivo(nodo.p4,bitacora)
										if temp.roto==False:
											return nodo_AB(nodo_AB,False)
										else:
											tp = celdas(nodo.p1, nodo.n1, nodo.p2, nodo.n2, nodo.p3,nodo.n3,temp.arbol.p1,temp.arbol.n1,temp.arbol.p2)
											return nodo_AB(tp,False)
								else:
									if nodo.n4.ingreso>bitacora.ingreso:
										if nodo.p4==None:
											izq = celdas(None,nodo.n1 ,None,nodo.n2 ,None,None,None,None,None)
											der = celdas(None,bitacora,None,nodo.n4 ,None,None,None,None,None)
											raiz =celdas(izq ,nodo.n3 ,der ,  None  ,None,None,None,None,None)
											return nodo_AB(raiz,True)
										else:
											temp = self.recursivo(nodo.p4,bitacora)
											if temp.roto==False:
												return nodo_AB(nodo,False)
											else:
												izq=celdas(nodo.p1		,nodo.n1	  ,nodo.p2		,nodo.n2,nodo.p3,None,None,None,None)
												der=celdas(temp.arbol.p1,temp.arbol.n1,temp.arbol.p2,nodo.n4,nodo.p5,None,None,None,None)
												raiz =celdas(izq ,nodo.n3 ,der ,  None  ,None,None,None,None,None)
												return nodo_AB(raiz,True)
# ---------------------------------5---------------------------------
									else:
										temp = self.recursivo(nodo.p5,bitacora)
										if temp.roto==False:
											return nodo_AB(nodo,False)
										else:
											izq=celdas(nodo.p1,nodo.n1,nodo.p2	    ,nodo.n2	  ,nodo.p3		,None,None,None,None)
											der=celdas(nodo.p4,nodo.n4,temp.arbol.p1,temp.arbol.n1,temp.arbol.p2,None,None,None,None)
											raiz =celdas(izq ,nodo.n3 ,der ,  None  ,None,None,None,None,None)
											return nodo_AB(raiz,True)

