from flask import Flask,render_template,request,redirect,url_for
import re
app=Flask(__name__)

# App server
@app.route('/') 
def index_function():
    return render_template("index.html")

@app.route('/Result',methods=['POST'])
def Result_function():
    Expression = request.form['in_1']
    String = request.form['in_2']
    count=0
    res=[]
    for it in re.finditer(r"{}".format(Expression),String):
        st=""
        count=count+1
        st=st+"Match :{} = \'{}\' , span=({} , {})".format(count,it.group(),it.start(),it.end())
        res.append(st)
    return render_template("Result.html",ans="Match Found." , E=Expression ,s=String,c=count,spans=res)
    return render_template("Result.html",count=-1)






#response
if __name__=='__main__':
    app.run(debug=True)