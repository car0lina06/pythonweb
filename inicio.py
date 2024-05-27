from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/area')
def area():
    return render_template("areatri.html")

@app.route('/grados')
def grados():
    return render_template("grados.html")

@app.route('/calificaciones')
def cali():
    return render_template("Calificaciones.html")

@app.route('/tablas')
def tab():
    return render_template("tablasmulti.html")

@app.route('/viaje')
def viaje():
    return render_template("viaje.html")


@app.route('/areaT', methods=['POST'])
def area_triangulo():
    if request.method == 'POST':
        ar =0
        b = int(request.form['base'])
        a = int(request.form['altura'])
        ar= b*a/2

    return render_template('areatri.html', res=ar)

@app.route('/gradosC', methods=['POST'])
def gradosconv():
    if request.method == 'POST':
        c = 0
        f= int(request.form['gradosF'])  
        c= 5/9*(f-32)

    return render_template('areatri.html', res=c)

@app.route('/cali', methods=['POST'])
def cf():
    if request.method == 'POST':
        c= int(request.form['calif']) 

        if c== 10:
            t="Exelente"

        elif c==9 :
            t= "Notable"

        elif c==8 :
            t= "Notable"
        
        elif c==7 :
            t= "Regular"
        elif c==6 :
            t= "suficiente"
        elif c==5 :
            t= "Reprobado"
        else: 
            t="Califificacion ingresada no valida"

    

    return render_template('Calificaciones.html',nota=c, res=t)



@app.route('/tablasm', methods=['GET', 'POST'])
def gtb():
    if request.method == 'POST':
        n = int(request.form['num'])
        tabla = []
        for i in range(1, 11):
            res = n * i
            tabla.append(res)

        return render_template('tablasmulti.html', tabla=tabla)

@app.route('/viaje', methods=[ 'POST'])
def vie():
    if request.method == 'POST':
        alumnos = int(request.form['ca'])
        cpa=0
        if alumnos >50 and alumnos<99:
            cpa=70
        elif alumnos >30 and alumnos<49:
            cpa=95
        elif alumnos<30:
            cpa=3500/alumnos
        
        ct= cpa*alumnos


        return render_template('viaje.html', res=cpa, res1=ct)
   




if __name__ == "__main__":
    app.run(debug=True)