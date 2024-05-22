from tkinter import *
from PIL import Image,ImageTk
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
def model():
    time=int(box.get())
    #load dataset
    df=pd.read_csv(r"C:\Users\hp\Downloads\student_info.csv")
    #df.info()
    #df.describe()
    #Data cleaning
    df2=df.fillna(df.mean())
    #split dataset
    a=df2.drop("student_marks",axis="columns")
    b=df2.drop("study_hours",axis="columns")
    #y=m*x+c
    x_train,x_test,y_train,y_test=train_test_split(a,b,test_size=0.2,random_state=51)
    #select model
    lr=LinearRegression()
    lr.fit(x_train,y_train)
    #value of m
    #print(lr.coef_)
    #value of c
    #print(lr.intercept_)
    k=lr.predict([[time]])[0][0].round(2)
    if(k>100):
        k=99.99
    msg='you will get ['+str(k)+' %] marks when you study '+str(time)+' hour per day'
    l2.config(text=msg)
    y_pred=lr.predict(x_test)
    #print(pd.DataFrame(np.c_[x_test,y_test,y_pred],columns=["study_hours","student_marks_original","student_marks_pred"]))
    #check accuracy of model
    #print(lr.score(x_test,y_test))

frame=Tk()
frame.title("cube calculator")
frame.geometry('1000x900+10+10')
pic=PhotoImage(file="C:\\Users\\hp\\Desktop\\study4.png")
lb=Label(frame,text='Student Marks Prediction',fg="blue",font=('Itallic',20,'bold'))
lb.place(x=150,y=30,width=600)
pic2=Image.open("C:\\Users\\hp\\Desktop\\study2.png")
resize_img=pic2.resize((600,250))
convrt=ImageTk.PhotoImage(resize_img)
std=Label(frame,image=convrt)
std.place(x=150,y=80,width=600)
l=Label(frame,text='Enter your Study Hours to Predict Marks',fg="green",font=('Arial',20,'bold'))
l.place(x=150,y=350,width=600)
box=Entry(frame,width=100,font=('Arial',20,'bold'))
box.place(x=250,y=400,width=300)
button=Button(frame,text='predict marks',fg='white',bg='green',font=('Arial',15,'bold'),command=model)
button.place(x=300,y=470,width=200)
l2=Label(frame,text=' ',font=('Arial',15,'bold'))
l2.place(x=70,y=530,width=700)
frame.mainloop()
