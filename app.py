#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask


app = Flask(__name__)



from flask import render_template, request 

@app.route("/", methods == ["GET", "POST"])
def index():
    if request.method =="POST":
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")
        purchases = float(purchases)
        suppcard = float(suppcard)
        print(purchases,suppcard)
        model1 = joblib.load('CCU_DT')
        pred1 = model1.predict([[purchases, suppcard]])
        s1 = "The score of credit card upgrade base on decision tree is " + str(pred1)
        model2 = joblib.load('CCU_Reg')
        pred2 = model2.predict([[purchases, suppcard]])
        s2 = "The score of credit card upgrade base on regression is " + str(pred2)
        model3 = joblib.load('CCU_NN')
        pred3 = model.predict([[purchases, suppcard]])
        s3 = "The score of credit card upgrade base on neural network is " + str(pred3)
        model4 = joblib.load('CCU_RF')
        pred4 = model.predict([[purchases, suppcard]])
        s4 = "The score of credit card upgrade base on random forest is " + str(pred4)
        model5 = joblib.load('CCU_GB')
        pred5 = model.predict([[purchases, suppcard]])
        s5 = "The score of credit card upgrade base on gradient boosting is " + str(pred5)
        
        return(render_template("index.html", result1=s1, result2="1", result3="1", result4="1", result5="2"))
    else: 
        return (render_template("index.html", result="2", result2="2", result3="2", result4="2", result5="2"))



if __name__=="__main__":
    app.run()

