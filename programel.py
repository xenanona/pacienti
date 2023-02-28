import customtkinter
import tkinter
import os
import pymysql

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")

fereastra = customtkinter.CTk()
fereastra.geometry("300x250")

fereastra_insert=customtkinter.CTk()
fereastra_insert.geometry("300x550")

fereastra_gasit=customtkinter.CTk()
fereastra_gasit.geometry("300x550")

fereastra_adaugat=customtkinter.CTk()
fereastra_adaugat.geometry("300x300")

text_nume = None

connection = None

def casuta():
    print("Casuta cauta pacient existent")
    
    global fereastra, text_nume
    frame = customtkinter.CTkFrame(master=fereastra)
    frame.pack(pady=20, padx=6, fill="both", expand=True)

    label=customtkinter.CTkLabel(master = frame, text=" Lista pacienti: ")
    label.pack(pady=22, padx=10)

    text_nume = customtkinter.CTkEntry(master = frame, placeholder_text="Numele: ")
    text_nume.pack(pady=12, padx=10)
    
    button = customtkinter.CTkButton(master = frame,text="Cauta", command=recivetext)
    button.pack(pady=30, padx=20)

    fereastra.mainloop()

def casuta_insert():
    print("Casuta insert")
    
    global fereastra_insert, insert_nume, insert_specie, insert_rasa, insert_sex
    global insert_cip, insert_stapan
    frame = customtkinter.CTkFrame(master=fereastra_insert)
    frame.pack(pady=20, padx=6, fill="both", expand=True)

    label=customtkinter.CTkLabel(master = frame, text=" Adauga pacient nou: ")
    label.pack(pady=22, padx=10)

    insert_nume = customtkinter.CTkEntry(master = frame, placeholder_text="Numele: ")
    insert_nume.pack(pady=12, padx=10)

    insert_specie = customtkinter.CTkEntry(master = frame, placeholder_text="Specie: ")
    insert_specie.pack(pady=12, padx=10)

    insert_rasa = customtkinter.CTkEntry(master = frame, placeholder_text="Rasa: ")
    insert_rasa.pack(pady=12, padx=10)

    insert_sex = customtkinter.CTkEntry(master = frame, placeholder_text="Sex: ")
    insert_sex.pack(pady=12, padx=10)

    insert_cip = customtkinter.CTkEntry(master = frame, placeholder_text="Cip: ")
    insert_cip.pack(pady=12, padx=10)

    insert_stapan = customtkinter.CTkEntry(master = frame, placeholder_text="Stapan: ")
    insert_stapan.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master = frame,text="Adauga", command=insert_text_get)
    button.pack(pady=30, padx=20)

    fereastra_insert.mainloop()

def casuta_pacientgasit(insert_nume, insert_specie, insert_rasa, insert_sex,insert_cip, insert_stapan):
    print("Gasit pacient existent")
    
    global fereastra_gasit
    frame = customtkinter.CTkFrame(master=fereastra_gasit)
    frame.pack(pady=20, padx=6, fill="both", expand=True)

    label=customtkinter.CTkLabel(master = frame, text=" Pacient gasit! ")
    label.pack(pady=22, padx=10)

    print("numele: ",insert_nume)
    print("specia: ",insert_specie)
    print("rasa: ", insert_rasa)
    print("cip:", insert_cip)
    print("stapan:", insert_stapan)

    label=customtkinter.CTkLabel(master = frame,text = insert_nume)
    label.pack(pady=22, padx=10)
    label=customtkinter.CTkLabel(master = frame,text = insert_specie)
    label.pack(pady=22, padx=10)
    label=customtkinter.CTkLabel(master = frame,text = insert_rasa)
    label.pack(pady=22, padx=10)
    label=customtkinter.CTkLabel(master = frame,text = insert_sex)
    label.pack(pady=22, padx=10)
    label=customtkinter.CTkLabel(master = frame,text = insert_cip)
    label.pack(pady=22, padx=10)
    label=customtkinter.CTkLabel(master = frame,text = insert_stapan)
    label.pack(pady=22, padx=10)
    fereastra_gasit.mainloop()

#sa afiseze succes dupa adaugarea unui pacient!
def casuta_pacientadaugat():
    print("Pacient nou adaugat!")
    
    global fereastra_adaugat
    frame = customtkinter.CTkFrame(master=fereastra_adaugat)
    frame.pack(pady=20, padx=6, fill="both", expand=True)

    label=customtkinter.CTkLabel(master = frame, text=" Succes ! Pacient nou adaugat! ")
    label.pack(pady=22, padx=10)
    fereastra_adaugat.mainloop()

def insert_text_get():
    global fereastra_insert, insert_nume, insert_specie, insert_rasa, insert_sex,insert_cip, insert_stapan
    input_insert_nume = insert_nume.get()
    input_insert_specie = insert_specie.get()
    input_insert_rasa = insert_rasa.get()
    input_insert_sex = insert_sex.get()
    input_insert_cip = insert_cip.get()
    input_insert_stapan = insert_stapan.get()

    print(input_insert_nume)
    print(input_insert_specie)
    print(input_insert_rasa)
    print(input_insert_sex)
    print(input_insert_cip)
    print(input_insert_stapan)

    insert_adauga_pacienti(input_insert_nume, input_insert_specie, input_insert_rasa, input_insert_sex,input_insert_cip,input_insert_stapan)
    fereastra.destroy()


def insert_adauga_pacienti(nume,specie,rasa,sex,cip,stapan):
    query_insert="INSERT INTO `tabel_pacienti` (`nume`, `specie`, `rasa`, `sex`, `cip`, `stapan`)VALUES('" + nume + "', '" + specie + "','" +rasa + "', '" +sex + "','" +cip + "','" +stapan + "')"
   
    connection= pymysql.connect(..................)
    print("query_insert: ", query_insert)
    cursor = connection.cursor()
    cursor.execute(query_insert)
    casuta_pacientadaugat() 
    connection.commit()
    connection.close()

def recivetext():
    global fereastra, text_nume
    input = text_nume.get()
    print(input)
    #conect()
    cauta_dupa_nume(input)
    fereastra.destroy()
    casuta_pacientgasit()
    #casuta_pacientadaugat()





def opendict():
    folder=r'C:\Users\Alexandra\Desktop\protectel'
    for i in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, i)):
            print(i)

#asta nu e valabil
def conect2():
    global connection
    if connection is None:
        connection= pymysql.connect(........................)
        cursor = connection.cursor()
        query="select * from tabel_pacienti"
        cursor.execute(query)
        rows=cursor.fetchall()
        for row in rows:
            print(row)
        connection.commit()
        connection.close()


def cauta_dupa_nume(nume):
    connection= pymysql.connect(.............................)
    query = "select * from tabel_pacienti where nume='" + nume + "'"
    print("query: ", query)
    cursor = connection.cursor()
    cursor.execute(query)
    rows=cursor.fetchall()
    for row in rows:
        numele=row[1]
        specie=row[2]
        rasa=row[3]
        sex=row[4]
        cip=row[5]
        stapan=row[6]
        casuta_pacientgasit(numele,specie,rasa,sex,cip,stapan)
    

    connection.commit()
    connection.close()

    




def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=6, fill="both", expand=True)

label=customtkinter.CTkLabel(master = frame, text=" Lista pacienti: ")
label.pack(pady=22, padx=10)

button = customtkinter.CTkButton(master = frame,text="Cauta pacient existent", command=casuta)
button.pack(pady=30, padx=20)

checkbox = customtkinter.CTkButton(master=frame, text="Adauga pacient nou", command=casuta_insert)
checkbox.pack(pady=30, padx=20)

button = customtkinter.CTkButton(master = frame,text="Pacient gasit! ", command=casuta_pacientgasit)
button.pack(pady=30, padx=20)


root.mainloop()