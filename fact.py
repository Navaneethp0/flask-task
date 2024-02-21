from flask import Flask
from flask import render_template,request
app=Flask(__name__)
@app.route('/<int:num>')
def abc(num):
    if num==0:
        return '1'
    elif num>0:
        factt=1
        for i in range(1,num+1):
            factt=factt*i
        return f'{factt}'
    else:
        return "no factorial"
if __name__ == '__main__':
        app.run(debug=True)
            