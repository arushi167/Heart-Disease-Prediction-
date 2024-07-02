from django.shortcuts import render
import pickle
import pandas as pd
import json




# Create your views here.
def index(request):
    return render(request,'index.html')


def predict(request):
    age=request.GET['age']
    sex=request.GET['sex']
    if sex=='0':
        sex=0
    elif sex=='1':
        sex=1
    cpt=request.GET['cp']
    if cpt=='0':
        cpt=0
    elif cpt=='1':
        cpt=1
    elif cpt=='2':
        cpt=2
    elif cpt=='3':
        cpt=3
    tps=request.GET['trestbps']
    chol=request.GET['chol']
    fbs=request.GET['fbs']
    if fbs=='0':
        fbs=0
    elif fbs=='1':
        fbs=1
    restecg=request.GET['restecg']
    if restecg=='0':
        restecg=0
    elif restecg=='1':
        restecg==1
    elif restecg=='2':
        restecg=2
    thalach=request.GET['thalach']
    exang=request.GET['exang']
    if exang=='0':
        exang=0
    elif exang=='1':
        exang=1
    oldpeak=request.GET['oldpeak']
    slope=request.GET['oldpeak']
    if oldpeak=='0':
        oldpeak=0
    elif oldpeak=='1':
        oldpeak=1
    elif oldpeak=='2':
        oldpeak=2
    ca=request.GET['ca']
    if ca=='0':
        ca =0
    elif ca=='1':
        ca=1
    elif ca=='2':
        ca=2
    elif ca=='3':
        ca==3
    thal=request.GET['thal']
    if thal=='0':
        thal=0
    elif thal=='1':
        thal=1
    elif thal=='2':
        thal=2
    age_cat=request.GET['age_category']
    if age_cat=='0':
        age_cat=0
    elif age_cat=='1':
        age_cat=1
    elif age_cat=='2':
        age_cat=2
    model_choice=request.GET['model_choice']

    user_input=[[age,sex,cpt,tps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,age_cat]]
    
    if model_choice == 'rfmodel':
        RFmodel=pickle.load(open('heart.pkl','rb'))
        pred = RFmodel.predict(user_input)
    elif model_choice == 'knnmodel':
        KNmodel =pickle.load(open('knheart.pkl','rb'))
        pred = KNmodel.predict(user_input)
    elif model_choice == 'svcmodel':
        SVCmodel = pickle.load(open('svheart.pkl','rb'))
        pred = SVCmodel.predict(user_input)
    

    pred=pred[0]
    return render(request,'result.html',{'result':pred,'model_choice':model_choice})

def preview(request):
    df = pd.read_csv("heart.csv")
    df = df[:10]
    json_records = df.reset_index().to_json(orient ='records')
    arr = []
    arr = json.loads(json_records)
    context = {'df': arr}
    return  render(request,'preview.html',context)
