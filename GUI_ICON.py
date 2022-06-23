# -*- coding: utf-8 -*-

import numpy as np

from keras.models import load_model

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkintermapview as tkm
from PIL import ImageTk,Image

import coordinate as co
import info
import a_star_gravina_città as astar
import query


 
wnd_main= tk.Tk()
wnd_main.geometry("420x500")
wnd_main.title("GuidaIA")
wnd_main.configure(background="gray")

frame_title=tk.LabelFrame(wnd_main, padx=20,pady=10,background="lightgray")
frame_title.grid(row=0, column=0, padx=10,pady=30)
title=tk.Label(frame_title, text="Benvenuto in GuidaIA",pady=20,font=('arial',25,'bold'),background="lightgray",fg="green")
title.grid(row=1,column=6,sticky="N")

frame_menu=tk.LabelFrame(wnd_main, text="Seleziona cosa vuoi fare:",font=('arial',12,'bold'), padx=20,pady=10,background="lightgray")
frame_menu.grid(row=1, column=0, padx=10,pady=30)

#------------------Finestra Classificatore---------------------------------------------  
def wnd_classify():
    top=tk.Toplevel()
    top.title('Classifica Immagini')
    top.geometry("800x1200")
    top.configure(background="gray")
    
    title=tk.Label(top, text="Image Classification",pady=20,font=('arial',20,'bold'),background="gray")
    title.pack()  
    
    model=load_model("model.hdf5")

    classes={
        0:'quattroFontane',
        1:'bastione',
        2:'bibliotecaFinya',
        3:'castello',
        4:'cattedrale',
        5:'madonnaDellaStella',
        6:'museoCivico',
        7:'torreOrologio',
        8:'palazzoOrsini',
        9:'ponte',
        10:'purgatorio',
        11:'sanBasilio',
        12:'sanFrancesco',
        13:'sanMichele',
        14:'santaLucia',
        15:'santaSofia',
        16:'statuaPapa',
        }

    def open():
        file_path=filedialog.askopenfilename(initialdir="C:/Users/domyl/Desktop/imgGuiProva", title="Seleziona File", filetypes=(("jpg files","*.jpg"),("Tutti i file","*.*")))
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)

    def show_classify_button(file_path):
        classify_btn=tk.Button(top,text="Classifica Immagine", padx=10, pady=5, fg="black", bg="yellow", font=('arial',10,'bold'),command=lambda:classify(file_path,classify_btn))
        classify_btn.pack(pady=15)
        

    def classify(file_path,classify_btn):
        image=Image.open(file_path)
        image=image.resize((224,224))
        image=np.expand_dims(image, axis=0)
        image=np.array(image)
        pred=model.predict(image)
        clas=classes[np.argmax(pred)]
        label.configure(text=clas)
        classify_btn.pack_forget() 
        show_map_button(clas)
        show_info_button(clas)        
     
    btn_open=tk.Button(top,text="Apri File", padx=10, pady=5, fg="black", bg="yellow", font=('arial',10,'bold'),command=open)
    btn_open.pack(pady=8)

    #upload image
    sign_image=tk.Label(top)
    sign_image.pack()

    #predict class
    label=tk.Label(top,background="gray",font=('arial',15,'bold'))
    label.pack(pady=10)
    
    def show_map_button(clas):
        map_btn=tk.Button(top,text="Visualizza su mappa", padx=10, pady=5, fg="black", bg="yellow", font=('arial',10,'bold'),command=lambda:visualizza_map(clas,map_btn))
        map_btn.pack(pady=15)
    
    #mapview
    def visualizza_map(clas,map_btn):
        frame_map=tk.LabelFrame(top, padx=20,pady=10,background="lightgray")
        frame_map.pack()
        map_view=tkm.TkinterMapView(frame_map, width=600,height=400,corner_radius=0)
        map_view.pack(pady=8)
        lat=co.get_lat(clas)
        long=co.get_lon(clas)
        map_view.set_position(lat,long)
        map_view.set_marker(lat,long, text=clas)
        map_view.set_zoom(18)
        map_btn.pack_forget()
    
    def show_info_button(clas):
        info_btn=tk.Button(top,text="Visualizza descrizione", padx=10, pady=5, fg="black", bg="yellow", font=('arial',10,'bold'),command=lambda:visualizza_info(clas,info_btn))
        info_btn.pack(pady=15)
    
    def visualizza_info(clas,info_btn):
        testo_info=str(info.get_info(clas))
        testo=tk.Text(top,bg="lightgray")
        testo.insert(1.0, testo_info)
        testo.pack(pady=10)
        info_btn.pack_forget()
        show_closeinfo_button(testo,clas)  
    
    def show_closeinfo_button(testo,clas):
        close_btn=tk.Button(top,text="Chiudi descrizione", padx=10, pady=5, fg="black", bg="yellow", font=('arial',10,'bold'),command=lambda:chiudi_info(testo,clas,close_btn))
        close_btn.pack(pady=15)
        
    def chiudi_info(testo,clas,close_btn):
        testo.pack_forget() 
        close_btn.pack_forget()
        show_info_button(clas)
        
#------------------Finestra Navigatore---------------------------------------------       
def wnd_navigator():
    top=tk.Toplevel()
    top.title('Navigatore')
    top.geometry("800x940")
    top.configure(background="gray")
    
    title=tk.Label(top, text="Navigatore",pady=20,font=('arial',20,'bold'),background="gray")
    title.pack() 
    
    frame_start=tk.LabelFrame(top, text="Seleziona Paese di Partenza", padx=20,pady=10)  
    frame_start.pack()
    
    frame_target=tk.LabelFrame(top, text="Seleziona Paese di Arrivo", padx=20,pady=10)  
    frame_target.pack(pady=10)

    options=["Alberobello","Altamura","Andria","Bari","Barletta","Bisceglie","Bitonto","Brindisi","Canosa","Cerignola","Corato","Fasano","Foggia",
             "Gioia","Grassano","Gravina","Irsina","Lecce","Matera","Minervino","Modugno","Monopoli","Molfetta","Ostuni","Palo","Poggiorsini",
             "Polignano","Potenza","Putignano","Santeramo","Taranto","Tolve","Toritto","Trani","Tricarico"]

    def select(event):
        city_start=box_start.get()  
        city_target=box_target.get()
        if(city_target!="seleziona"):
            show_calculate_button(city_start, city_target)
    
    def show_calculate_button(city_start,city_target):    
        calculate_btn=tk.Button(top,text="Calcola Percorso", padx=10, pady=5, fg="black", bg="yellow", font=('arial',10,'bold'),command=lambda:calculate(city_start, city_target))
        calculate_btn.pack(pady=15)
    
    def calculate(city_start, city_target):
        testo_route,testo_km,lst_city=astar.calcola(city_start, city_target)
        testo1=tk.Text(top,bg="lightgray",pady=10,padx=10,font=('arial',10,'bold'),height=3)
        testo1.insert(1.0, testo_route)
        testo1.pack(pady=10)
        testo2=tk.Text(top,bg="lightgray",pady=10,padx=10,font=('arial',10,'bold'),height=1)
        testo2.insert(1.0,testo_km)
        testo2.pack(pady=7)
        show_map_button(lst_city)
    
    def show_map_button(lst_city):
        map_btn=tk.Button(top,text="Visualizza su mappa", padx=10, pady=5, fg="black", bg="yellow", font=('arial',10,'bold'),command=lambda:visualizza_map(lst_city,map_btn))
        map_btn.pack(pady=15)
    
    #mapview
    def visualizza_map(lst_city,map_btn):
        frame_map=tk.LabelFrame(top, padx=20,pady=10,background="lightgray")
        frame_map.pack()
        map_view=tkm.TkinterMapView(frame_map, width=600,height=400,corner_radius=0)
        map_view.pack(pady=8)
        lat=co.get_lat(lst_city[0])
        long=co.get_lon(lst_city[0])
        map_view.set_position(lat,long)
        lst_marker=[]
        for city in lst_city:
            lati=co.get_lat(city)
            longi=co.get_lon(city)
            marker=map_view.set_marker(lati, longi, text=city) 
            lst_marker.append(marker.position)
        map_view.set_zoom(10)
        map_view.set_path(lst_marker)
        map_btn.pack_forget()
       
        
        
    box_start=ttk.Combobox(frame_start, values=options)
    box_start.pack()
    box_start.set("seleziona")
    box_start.bind("<<ComboboxSelected>>",select)
          
    box_target=ttk.Combobox(frame_target, values=options)
    box_target.pack()
    box_target.set("seleziona")
    box_target.bind("<<ComboboxSelected>>",select)


#------------------Finestra Query---------------------------------------------       
def wnd_query():
    top=tk.Toplevel()
    top.title('Query')
    top.geometry("900x800")
    top.configure(background="gray")
    
    title=tk.Label(top, text="Query",pady=20,font=('arial',20,'bold'),background="gray")
    title.pack() 
    frame_chek=tk.LabelFrame(top, padx=20,pady=10,background="lightgray")  
    frame_chek.pack()
    
    
    def show_esegui_button(var,top):
        var=var.get()
        btn_esegui=tk.Button(frame_chek,text="Esegui", height=2,width=15,padx=5, fg="black", bg="yellow", font=('arial',10,'bold'),command=lambda:esegui_query(var,top,btn_esegui)) 
        btn_esegui.pack(pady=5)
    
    def esegui_query(var,top,btn_esegui):
        btn_esegui.pack_forget()
        query.get_answer(var,top)
        
        
    var=tk.IntVar()
    
    c1=tk.Checkbutton(frame_chek, text="Lista di tutte le attrazioni turistiche", variable=var, onvalue=1, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:show_esegui_button(var,frame_chek)) 
    c1.deselect()
    c1.pack(side='top', anchor='w', pady=5)

    c2=tk.Checkbutton(frame_chek, text="Trova attrazioni turistiche vicine al luogo in cui stai mangiando o soggiornando", variable=var, onvalue=2, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:show_esegui_button(var,top))
    c2.pack(side='top', anchor='w', pady=5)
    c2.deselect()
    
    c3=tk.Checkbutton(frame_chek, text="Trova ristoranti o b&b vicino a un'attrazione turistica", variable=var, onvalue=3, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:show_esegui_button(var,top))
    c3.pack(side='top', anchor='w', pady=5)
    c3.deselect()
    
    c4=tk.Checkbutton(frame_chek, text="Trova l'attrazione più vicina all'attrazione turistica scelta", variable=var, onvalue=4, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:show_esegui_button(var,top))
    c4.pack(side='top', anchor='w', pady=5)
    c4.deselect()
    
    c5=tk.Checkbutton(frame_chek, text="Trova la valutazione di un ristorante o b&B", variable=var, onvalue=5, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:show_esegui_button(var,top))
    c5.pack(side='top', anchor='w', pady=5)
    c5.deselect()
    
    c6=tk.Checkbutton(frame_chek, text="Trova i b&b che hanno la valutazione maggiore di un certo X (0-10)", variable=var, onvalue=6, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:show_esegui_button(var,top))
    c6.pack(side='top', anchor='w', pady=5)
    c6.deselect()
    
    c7=tk.Checkbutton(frame_chek, text="Trova i ristoranti che hanno la valutazione maggiore di un certo X (0-5)", variable=var, onvalue=7, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:show_esegui_button(var,top))
    c7.pack(side='top', anchor='w', pady=5)
    c7.deselect()
    
    c8=tk.Checkbutton(frame_chek, text="Cerca l'itinerario turistico in base alla lunghezza (completo-medio-breve)", variable=var, onvalue=8, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:show_esegui_button(var,top))
    c8.pack(side='top', anchor='w', pady=5)
    c8.deselect()
    
    c9=tk.Checkbutton(frame_chek, text="Crea l'itinerario turistico indicando il punto di partenza e di arrivo", variable=var, onvalue=9, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:show_esegui_button(var,top))
    c9.pack(side='top', anchor='w', pady=5)
    c9.deselect()
        
    
    
  

btn_classify=tk.Button(frame_menu,text="Classifica Immagine", height=2,width=15,padx=5, fg="black", bg="gray", font=('arial',10,'bold'),command=wnd_classify) 
btn_classify.grid(row=1,column=1,pady=10, sticky="W")

btn_navigator=tk.Button(frame_menu,text="Navigatore",height=2,width=15, padx=5, fg="black", bg="gray", font=('arial',10,'bold'),command=wnd_navigator)
btn_navigator.grid(row=2,column=1,pady=10,sticky="W") 

btn_query=tk.Button(frame_menu,text="Query", height=2,width=15,padx=5, fg="black", bg="gray", font=('arial',10,'bold'),command=wnd_query)
btn_query.grid(row=3,column=1,pady=10,sticky="W") 


wnd_main.mainloop()


