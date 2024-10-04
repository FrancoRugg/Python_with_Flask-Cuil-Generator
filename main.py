from flask import Flask,redirect,session,render_template,request,send_from_directory,jsonify, send_file;
import os;
from Business.calculator import cuilCalculator
from Model.dataModel import Users;

app = Flask(__name__,template_folder="templates",static_folder="static"); #Nombre de la App y Ubicación de los archivos .HTML
#Key de variable de sesion
app.secret_key = "1234";

Users;
@app.route("/index", methods=['GET', 'POST'])
def index():
    # return "<h1>Welcome</h1>";
    if request.method == "POST":
        if request.form["username"] == "franco_ruggiero" and request.form["password"] == "1":
            session["logged"] = True;
            session["name"] = request.form["username"];
            return redirect("/home")
        return render_template("login.html",error="Credenciales Erroneas")
    return render_template("login.html");
@app.route("/home", methods = ['GET', 'POST'])
def Home():
    if request.method == "POST":
        try:
            print(request.form.get('dni'))
            print(request.form['dni'])
            print(request.form.get('genre'))
            if request.form["dni"] and request.form["genre"]:
            # if request.form["dni"] != None and request.form["genre"] == "M" or request.form["dni"] != None and request.form["genre"] == "F":
                #----------------------
                print(request.form.get("dni"))
                print(request.form.get("genre"))
                session["dni"] = request.form["dni"];
                session["genre"] = request.form["genre"];
                conn = cuilCalculator(request.form["dni"],request.form["genre"])
                conn.validateDNI();
                cuil = conn.calculate();
                print(cuil)
                
                render_template("home.html",setCuil=f"CUIL: {cuil}")
                #----------------------
                # print(jsonify({'cuil': f'CUIL: {cuil}'}));
                # return jsonify({'cuil': f'CUIL: {cuil}'})
                # return redirect("/home")
            return render_template("home.html",error="Error! Complete todos los campos.") #ESTE]
            # return jsonify({'Error' : "Error! Complete todos los campos."})
        except Exception as e:
            render_template("home.html",error=f"{e.args[0]}") #ESTE
            # print({'error' : f"{e.args[0]}"});
            # print(jsonify({'error' : f"{e.args[0]}"}));
            # jsonify({'error' : f"{e.args[0]}"})
    return render_template("home.html");
@app.route("/setCuil", methods=['POST'])#Preguntar como acceder directamente a las funciones
def setCuil():
    pass;
@app.route("/saveCuil", methods=['POST'])
def saveCuil():
    data = request.json
    cuil = data.get('cuil')

    if not cuil:
        return jsonify({'error': 'No CUIL provided'}), 400

    filename = f'cuil_{cuil}.txt'
    filepath = os.path.join('files', filename)

    # Crear carpeta si no existe
    if not os.path.exists('files'):
        os.makedirs('files')

    with open(filepath, 'w') as f:
        f.write(f'CUIL: {cuil}\n')

    return jsonify({'filename': filename})

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    filepath = os.path.join('files', filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route("/style.css")
def style():
    return send_from_directory(os.path.join(os.path.join(app.root_path,'static'),'css'),'style.css')
@app.route("/favicon.ico")
def icon():
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon.ico',mimetype='image/vnd.microsoft.icon')
@app.route("/exit")
def exit():
    # return "Hasta la próxima!"
    try:
        if session["logged"] == True:
            text = session["name"];
            return f"Hasta la próxima {text}!"
    except KeyError:
        return "No se encuentra logueado"
            

@app.route("/")
def gotoIndex():
    return redirect("/index"); #Si no especifica nada, va al index

app.run(debug = True,host='localhost',port=5000); #Del 65535 hasta el 1023 están reservados.

# debug = True, El servidor se recarga con cada cambio





