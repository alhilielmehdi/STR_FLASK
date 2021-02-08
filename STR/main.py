import os
import random
import prime
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    return(render_template('index.html'))
@app.route('/',methods=['POST'])
def result():
    algo=request.form['algo']
    number=int(request.form['task'])
    open("tasks1.txt", "w").close()
    if request.method == 'POST':
        with open('tasks1.txt', 'a+') as f:
            for i in range(number):
                period=request.form['Periode'+str(i)]
                at=request.form['At'+str(i)]
                bt=request.form['Bt'+str(i)]
                dl=request.form['Deadline'+str(i)]
                nom=request.form['Nt'+str(i)]
                f.write(str(period)+" "+str(at)+" "+str(bt)+" "+str(dl)+" "+str(nom)+"\n")

    print(algo)
    if algo== "RM":
        #execfile('templates/rm/rm.py')
        os.system('python templates/rm/rm.py')
        return(render_template('rm/output.html'))
    elif algo=="DM":
        os.system('python templates/dm/rm.py')
        return (render_template('dm/output.html'))
    elif algo == "EDF":
        os.system('python templates/edf/edf.py')
        return (render_template('edf/output.html'))
    elif algo == "LLF":
        os.system('python templates/llf/llf.py')
        return (render_template('llf/output.html'))

app.run(debug=True)



