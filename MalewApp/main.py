# importation de la bibliotheque
from tkinter import *
from tkinter import messagebox
import os
# importation de msql
import mysql.connector

bd = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd = "",
        database="malewapp"
)
cursor = bd.cursor()


# Creation d'une fenetre
fenetre = Tk()
fenetre.title("MalewApp")
fenetre.geometry("925x500+300+200")
fenetre.configure(bg="#fff")
fenetre.resizable(False,False)

# Coonexion a la base de donne pour teste

def connex():
        # recuperation du nom est mot de passe
        nom = user.get()
        mdp = password.get()
        requet = f"SELECT * FROM Administrateur WHERE Administrateur= '{nom}'"
        cursor.execute(requet)
        result = cursor.fetchone()
                
        if result:
                requette = f"SELECT * FROM Administrateur WHERE password= '{mdp}'"
                cursor.execute(requette)
                result = cursor.fetchone()
                if result :
                        os.system("python home.py")
                        fenetre.quit()
                else:
                        messagebox.showerror("Error","Le password incorect!")         
        else:
                messagebox.showerror("Error","Le nom saisie : '" + nom + "' N'est fais pas partie de username !")         
        

# creation fonction pour username

def on_enter(e):
        user.delete(0,"end")

def on_leave(e):
        nom = user.get()
        if nom =='':
                user.insert(0, "Username")


# Charger l'image
image_source = PhotoImage(file="Font.png")
conteneur_img = Canvas(fenetre, width=400, height=400 , background="white")
conteneur_img.create_image(400, 200, image = image_source)
conteneur_img.place(x=30, y=50)

# Creation d'un conteneur
conteneur = Frame(fenetre, width=350, height=350,bg="white")
conteneur.place(x=480,y=70)
# creation du tire login

text_titre= Label(conteneur, text="Login", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, 'bold'))
text_titre.place(x=100, y=5)


# Creation de champ user
user = Entry(conteneur, width=25,fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30,y=80)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(conteneur, width=295, height=2, bg="black").place(x=25,y=107)

# creation fonction pour password

def on_enter(e):
        password.delete(0,"end")

def on_leave(e):
        mdp = password.get()
        if mdp =='':
                password.insert(0, "Password")


# Creation de champ password
password = Entry(conteneur, width=25,fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
password.place(x=30,y=150)
password.insert(0, "Password")
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)
Frame(conteneur, width=295, height=2, bg="black").place(x=25,y=177)

# Creation du button connexion

Button(conteneur, width=42,pady=7, text="Connexion", bg="#57a1f8", fg="white", border=0, command=connex).place(x=28, y=204)



fenetre.mainloop()