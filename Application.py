import tensorflow as tf
import pandas as pd
import keras
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from sklearn import preprocessing
import tkinter.scrolledtext as scrolledtext
from keras.utils.np_utils import normalize
from pandastable import Table

model = tf.keras.models.load_model("D:\\University\\semester 6\\Data Mining\\Project\\saved model\\saved_model_98percent.h5")
model.summary()

main_win = tkinter.Tk()
main_win.title("Network Intrusion Detection System")
main_win.geometry("1000x500")
main_win.sourceFile = ''

label1 = Label(main_win, text = 'AI based Network Intrusion Detection System')
label1.place(x = 400 , y = 20)

label2 = Label(main_win, text = 'Data Mining Project by Fraz Ahmad')
label2.place(x = 400 , y = 40)

label3 = Label(main_win, text= 'Predictions')
label3.place(x= 250, y = 60)

note = Label(main_win, text = "Note: Predictions are shown in first prediction column with original network data")
note.place(x= 350, y = 60)

attackCount = Label(main_win, text="Total Attack Counts is: ")
attackCount.place(x = 40, y = 140)

attackEntry = Entry(main_win)
attackEntry.place(x = 40, y = 160)

benignCount = Label(main_win, text = "Total Benign Count is: ")
benignCount.place(x = 40 , y = 180)

benignEntry = Entry(main_win)
benignEntry.place(x = 40, y = 200)


AttackCount80 = Label(main_win, text = "Attack Count on destination port 80")
AttackCount80.place(x = 40 , y = 220)

AttackCount80Entry = Entry(main_win)
AttackCount80Entry.place(x = 40, y = 240)

AttackCount443 = Label(main_win, text = "Attack Count on destination port 443")
AttackCount443.place(x = 40 , y = 260)

AttackCount443Entry = Entry(main_win)
AttackCount443Entry.place(x = 40, y = 280)

AttackCount53 = Label(main_win, text = "Attack Count on destination port 53")
AttackCount53.place(x = 40 , y = 300)

AttackCount53Entry = Entry(main_win)
AttackCount53Entry.place(x = 40, y = 320)

AttackCount22 = Label(main_win, text = "Attack Count on destination port 22")
AttackCount22.place(x = 40 , y = 340)

AttackCount22Entry = Entry(main_win)
AttackCount22Entry.place(x = 40, y = 360)


def chooseFile():
    main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/", title='Please select a csv file')
    print("Input File : ",main_win.sourceFile)
    data = pd.read_csv(main_win.sourceFile)

    x_data = preprocessing.normalize(data.values)
    pred = model.predict(x_data)
    TotalAttack = 0
    TotalBenign = 0
    TotalAttack80 = 0
    TotalAttack443 = 0
    TotalAttack53 = 0
    TotalAttack22 = 0

    for i,p in zip(range(len(pred)),pred):
        if p >= 0.5:
            pred[i] = 1
            TotalAttack = TotalAttack + 1
        else:
            pred[i] = 0
            TotalBenign = TotalBenign + 1

    frame = tkinter.Frame(main_win)
    frame.place(x = 250 ,y = 80,width= 700,height= 400)

    attackEntry.insert(15, str(TotalAttack))
    benignEntry.insert(15, str(TotalBenign))

    data.insert(0, "Prediction", pred , True)
    pt = Table(frame, dataframe=data)
    pt.show()

    for i in range(data.shape[0]):
        if data[' Destination Port'][i] == 80 and pred[i] == 1:
            TotalAttack80 +=1
        elif data[' Destination Port'][i] == 443 and pred[i] == 1:
            TotalAttack443 +=1
        elif data[' Destination Port'][i] == 53 and pred[i] == 1:
            TotalAttack53 +=1
        elif data[' Destination Port'][i] == 22 and pred[i] == 1:
            TotalAttack53 += 1

    AttackCount80Entry.insert(15, str(TotalAttack80))
    AttackCount443Entry.insert(15, str(TotalAttack443))
    AttackCount53Entry.insert(15, str(TotalAttack53))
    AttackCount22Entry.insert(15, str(TotalAttack22))

b_chooseFile = tkinter.Button(main_win, text = "Chose File", width = 20, height = 3, command = chooseFile)
b_chooseFile.place(x = 50,y = 60)
b_chooseFile.width = 100

main_win.mainloop()
