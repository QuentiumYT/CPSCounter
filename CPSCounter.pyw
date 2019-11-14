import os, sys, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 3
__filename__ = "CPSCounter"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)
__picpath__ = __savepath__ + "/{}.png".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:
            urllib.request.urlretrieve("https://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
            urllib.request.urlretrieve("https://quentium.fr/+++PythonDL/{}.png".format(__filename__), __picpath__)
        except:pass

if connection == True:
    try:script_version = int(urllib.request.urlopen("https://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("https://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("https://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

import time

clics = 0
flag = 0
depart = 0
chrono_active = False

def reset():
    global chrono_active, clics, depart, flag
    chrono_active = False
    clics = 0
    flag = 0
    depart = 0
    clics_add.set("Clics : " + str(clics))
    button1.configure(state="active")
    message1.configure(text="Chronomètre automatique, cliquez pour commencer.")
    message2.configure(text="Ici apparaitrons vos CPS...")
    message3.configure(text="Stade : Cliquez pour commencer !")

def lancer_chrono():
    global depart, flag
    flag = 1
    depart = time.time()
    top_horloge()

def top_horloge():
    global depart, flag
    y = time.time() - depart
    secondes = time.localtime(y)[5]
    secondes = secondes + 1
    sec_get = nb_sec.get()
    sec = int(sec_get)
    if flag:
        if secondes <= 1:
            message1.configure(text="%i Seconde" %secondes)
        elif secondes == int(sec):
            message1.configure(text="%i Seconde" %secondes)
            button1.configure(state="disabled")
            def stoper_chrono():
                global flag
                flag=0
            stoper_chrono()
            time.sleep(0.3)
            message1.configure(text="Vous avez fait " + str(clics) + " clics en " + str(sec) + " secondes !")
            cps_env = clics / sec
            cps = round(cps_env, 2)
            if cps <= 1:
                message2.configure(text="Vous avez fait moins de 1 CPS !")
                message3.configure(text="Stade : Mauvais cliqueur")
            if cps >= 2.5:
                message2.configure(text="Vous avez fait " + str(cps) + " CPS !")
                message3.configure(text="Stade : Débutant du clic")
            if cps >= 5:
                message2.configure(text="Vous avez fait " + str(cps) + " CPS !")
                message3.configure(text="Stade : Cliqueur du dimanche")
            if cps >= 7.5:
                message2.configure(text="Vous avez fait " + str(cps) + " CPS !")
                message3.configure(text="Stade : Cliqueur moyen")
            if cps >= 10:
                message2.configure(text="Vous avez fait " + str(cps) + " CPS !")
                message3.configure(text="Stade : Bon cliqueur")
            if cps >= 12.5:
                message2.configure(text="Vous avez fait " + str(cps) + " CPS !")
                message3.configure(text="Stade : Cliqueur expérimenté")
            if cps >= 15:
                message2.configure(text="Vous avez fait " + str(cps) + " CPS !")
                message3.configure(text="Stade : Initié des clics")
            if cps >= 20:
                message2.configure(text="Vous avez fait " + str(cps) + " CPS !")
                message3.configure(text="Stade : Monstre du clic")
            if cps >= 25:
                message2.configure(text="Vous avez fait " + str(cps) + " CPS !")
                message3.configure(text="Stade : Dieu du CPS")
            if cps >= 30:
                message2.configure(text="Vous avez fait " + str(cps) + " CPS !")
                message3.configure(text="Stade : Cliquer c'est mal ☺")
            else:
                message2.configure(text="Vous avez fait " + str(cps) + " CPS !")
        else:
            message1.configure(text="%i Secondes" %secondes)
    clicker.after(1000, top_horloge)

def addclick():
    global clics, chrono_active
    try:
        sec_get = nb_sec.get()
        sec = int(sec_get)
        if sec > 1:
            if chrono_active == False:
                chrono_active = True
                lancer_chrono()
            if chrono_active == True:
                clics = int(clics) + 1
                def f_add_clic():
                    global clics
                    clics_add.set("Clics : " + str(clics))
                f_add_clic()
        else:
            showwarning("Erreur", "Le nombre de secondes est trop petit !")
    except:
        showwarning("Erreur", "Le nombre de secondes est incorrect ou est mal écrit !")

clicker = Tk()
clicker.configure(bg="white")
clicker.state("zoomed")
if os.path.exists(__iconpath__):
    clicker.iconbitmap(__iconpath__)
clicker.title(__filename__)

Label(clicker, text="CPS Counter", font="impact 50", fg="red", bg="white").pack()

nb_sec = StringVar()
nb_sec.set("5")
Label(clicker, text="Nombre de secondes : ", font="impact 20", bg="white").pack()
Entry(clicker, textvariable=nb_sec, width=4, font="impact 20").pack()

def character_limit(nb_sec):
    if len(nb_sec.get()) > 0:
        nb_sec.set(nb_sec.get()[:2])

nb_sec.trace("w", lambda *args: character_limit(nb_sec))

if os.path.exists(__picpath__):
    if clicker.winfo_screenheight() >= 1080:
        button1 = Button(clicker, relief=GROOVE, height=450, width=800, bg="white", command=addclick)
    else:
        button1 = Button(clicker, relief=GROOVE, height=195, width=800, bg="white", command=addclick)
    b_img = PhotoImage(file=__picpath__)
    button1.config(image=b_img)
    button1.image=b_img
    button1.pack(side=TOP, pady=10)
else:
    button1 = Button(clicker, relief=GROOVE, height=30, width=120, bg="gray", command=addclick)
    button1.pack(side=TOP, pady=10)

message1 = Label(clicker, text="Chronomètre automatique, cliquez pour commencer.", font="impact 20", bg="white")
message1.pack()

clics_add = StringVar()
clics_add.set("Clics : " + str(clics))
Label(clicker, textvariable=clics_add, width=9, font="impact 25", bg="white", fg="red").pack(side=TOP, pady=10)

message2 = Label(clicker, text="Ici apparaitrons vos CPS...", font="impact 20", bg="white")
message2.pack(pady=5)
message3 = Label(clicker, text="Stade : Cliquez pour commencer !", font="impact 20", bg="white")
message3.pack(pady=10)

button2 = Button(clicker, text="Recommencer ?", height=1, width=20, relief=GROOVE, bg="red", command=reset, font="impact 20")
button2.pack(pady=20)

clicker.mainloop()
