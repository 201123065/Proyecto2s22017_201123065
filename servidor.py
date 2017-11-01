from flask import Flask,request,render_template,redirect,session

from Usuario import Usuario
from bitacora import bitacora
app = Flask("Hotel")
app.secret_key= 'mi_clave_secreta'
registro = Usuario()
bita = bitacora()


@app.route('/master')
def master():
	registro.agregar("super","user"," "," "," ","si")
	return redirect("/")


@app.route('/ingreso')
def ingreso():
	cad = registro.visualizarUsuarios()
	return cad


@app.route('/crear_usuario',methods=['POST'])
def crear_usuario():
	usuario = request.form['usuario']
	password = request.form['password']
	password2 = request.form['password2']
	address = request.form['address']
	phone = request.form['phone']
	age = request.form['age']
	print usuario
	print password
	if password==password2:
		ret = registro.agregar(usuario,password,address,phone,age,"no")
		print ret
		bita.cargar(ret)
		if "Agregado" in ret:
			return redirect("/")

		if usuario!=None or usuario!="":
			return redirect("/crear_cuenta")
		else:
			return render_template("user.html")
	else:
		print "ni entro el malparido"
		return render_template("user.html")


@app.route('/crear_usuario_android',methods=['POST'])
def crear_usuario_android():
	print "crear usuario"
	usu = str(request.form['usuario'])
	passwd = str(request.form['pwd'])
	p2 = str(request.form['pwd2'])
	direccion=str(request.form['direccion'])
	telefono=str(request.form['telefono'])
	edad=str(request.form['edad'])
	ret =registro.agregar(usu,passwd,direccion,telefono,edad)
	bita.cargar(ret)
	return ret


@app.route('/')
def index():
	if 'username' in session:
		print session['super']
		if "2" in session['super']:
			context={"super":True}
			return render_template("Admin_folder/admin.html")
		if "1" in session['super']:
			context={"invitado":True}
			return render_template("invitado/base.html")
		else:
			print "ni popo"
		return render_template("invitado/base.html")
	return render_template("indice.html")


@app.route('/crear_cuenta')
def crear_cuenta():
	return render_template("user.html")

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
		session.pop('super')
	return redirect('/')

@app.route('/login',methods=['POST'])
def login():
	usu = str(request.form['usuario'])
	passwd = str(request.form['password'])
	sesion=registro.login(usu,passwd)
	if sesion=="1":
		session['username']=usu
		session['super']="1"
	elif sesion=="2":
		session['username']=usu
		session['super']="2"
	return redirect("/")

@app.route('/crear_habitacion',methods=['POST'])
def crear_habitacion():
	bita.cargar(ret)
	return ret

@app.route('/reservar')
def reservar():
	
	context={
		"monto":"montiel",
		"monto2":"montiel",

	}
	return render_template("invitado/reservar.html",monto=context)



if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')