from flask import Flask, render_template, request, redirect, url_for
import csv
 
app = Flask(__name__)
 
# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')
 
# Ruta para manejar el formulario de reporte
@app.route('/report', methods=['POST'])
def report():
    establishment_code = request.form['code']
    status = request.form['status']
 
    # Guardar los datos en un archivo CSV
    with open('reports.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([establishment_code, status])
 
    return redirect(url_for('index'))
 
# Ruta para generar el reporte
@app.route('/generate_report')
def generate_report():
    report = []
    with open('reports.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            report.append({'code': row[0], 'status': row[1]})
 
    return render_template('report.html', report=report)
 
if __name__ == '__main__':
    app.run(debug=True)


