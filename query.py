# -*- coding: utf-8 -*-

from pyswip import Prolog
from pyswip import Functor

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

prolog=Prolog()
prolog.consult("prologQuery.pl")

prolog2=Prolog()
prolog2.consult("bfsProlog.pl")

def show_result(answer,top):
    testo_answer=str(answer)
    testo=tk.Text(top,bg="lightgreen",height=5, width=80,font=('arial',11,'bold'))
    testo.insert(1.0, testo_answer)
    testo.pack(pady=10)
    

def get_answer(number,top):
    options_rist_beb=["ziaRosa","radici","sottofondo","santAgostino","1881","mammaMia","alVecchioCrapo","trediciVolte","fondoCrudo","saporiDiCasa","tibbasta","alCastello","daLapo",
             "labò","fontanaLaStella","sulPonte","laCattedraleSuites","laCivita","setteCamere","sanMicheleDelleGrotte","stanzeDiFinya","melograno","calderoni24","ducaOrsini","santaSofia","colleDelRe",
             "villaRadiosa","ilBorgo","daiMimmi","rebelSuite","grantò","albaSuite","ilPiccoloPrincipe","stanzeOrsini","sottoLarco"]
    options_attr=["ponte","cattedrale","quattroFontane","purgatorio","bibliotecaFinya","museoCivico","sanMichele","santaLucia","santaSofia","castello","torreOrologio","madonnaDellaStella","bastione","sanFrancesco","sanBasilio","palazzoOrsini","statuaPapa"]
    
    if number==1:
        lst_answer=''
        for val in prolog.query("monument(X)"):
            lst_answer=lst_answer+str(val["X"])+' - '
        show_result(lst_answer,top)
    
    elif number==2:
        frame=tk.LabelFrame(top, text="Seleziona luogo:", padx=20,pady=10,background="lightgray",font=('arial',10,'bold'))  
        frame.pack(pady=5)
        def select(event):
            lst_answer2=''
            luogo=box_luoghi.get()  
            if(luogo!="seleziona"):
                Y=luogo
                for val in prolog.query("neighbor(X,"+Y+")"):
                    lst_answer2=lst_answer2+str(val["X"])+' - '
            show_result(lst_answer2,top)
        
        box_luoghi=ttk.Combobox(frame, values=options_rist_beb)
        box_luoghi.pack(pady=5)
        box_luoghi.set("seleziona")
        box_luoghi.bind("<<ComboboxSelected>>",select)
    
    elif number==3:
        frame=tk.LabelFrame(top, text="Seleziona cosa stai cercando:", padx=20,pady=10,background="lightgray",font=('arial',10,'bold'))  
        frame.pack(pady=5)
        options=["ristoranti","b&b"]
        def select(event):
            scelta=box_scelta.get()
            frame_2=tk.LabelFrame(frame, text="Seleziona attrazione:", padx=20,pady=10,background="lightgray",font=('arial',10,'bold'))  
            frame_2.pack(pady=5)
            
            def select2(event):
                answer=''
                luogo=box_attr.get()
                if scelta=="ristoranti":
                    for val in prolog.query("searchR("+luogo+",X)"):
                        answer=answer+str(val["X"])+' - '
                    show_result(answer,top)
                elif scelta=="b&b":
                    for val in prolog.query("searchB("+luogo+",X)"):
                        answer=answer+str(val["X"])+' - '
                    show_result(answer,top)
                    
            box_attr=ttk.Combobox(frame_2, values=options_attr)
            box_attr.pack(pady=5)
            box_attr.set("seleziona")
            box_attr.bind("<<ComboboxSelected>>",select2)
                
            
        box_scelta=ttk.Combobox(frame, values=options)
        box_scelta.pack(pady=5)
        box_scelta.set("seleziona")
        box_scelta.bind("<<ComboboxSelected>>",select)
        
        
    elif number==4:
        frame=tk.LabelFrame(top, text="Seleziona l'attrazione turistica:", padx=20,pady=10,background="lightgray",font=('arial',10,'bold'))  
        frame.pack(pady=5)
        def select(event):
            answer=''
            scelta=box_scelta.get()  
            for val in prolog.query("searchM("+scelta+",X)"):
                answer=answer+str(val["X"])+' - '
            show_result(answer,top)
      
        box_scelta=ttk.Combobox(frame, values=options_attr)
        box_scelta.pack(pady=5)
        box_scelta.set("seleziona")
        box_scelta.bind("<<ComboboxSelected>>",select)
    
    elif number==5:
        frame=tk.LabelFrame(top, text="Seleziona il ristorante o b&b:", padx=20,pady=10,background="lightgray",font=('arial',10,'bold'))  
        frame.pack(pady=5)
        def select(event):
            answer=''
            scelta=box_scelta.get()  
            for val in prolog.query("rate("+scelta+",X)"):
                answer=answer+str(val["X"])+' - '
            show_result(answer,top)
      
        box_scelta=ttk.Combobox(frame, values=options_rist_beb)
        box_scelta.pack(pady=5)
        box_scelta.set("seleziona")
        box_scelta.bind("<<ComboboxSelected>>",select)
        
    elif number==6:
        frame=tk.LabelFrame(top, text="Inserisci la valutazione(0-10):", padx=20,pady=10,background="lightgray",font=('arial',10,'bold'))  
        frame.pack(pady=5)
        
        inp=tk.Entry(frame,width=20, borderwidth=3, font=('Helvetica', 10))
        inp.pack()
        def cerca():
            if float(inp.get())<0 or float(inp.get())>10:
                messagebox.showerror("Errore", "Valore inserito errato")
                inp.delete(0, 'end')
            else:
                rate=inp.get()
                answer='' 
                for val in prolog.query("searchTopB(BeB,Rate,"+rate+")"):
                    answer=answer+str(val["BeB"])+' '+str(val["Rate"])+' - '
                inp.delete(0, 'end')
                show_result(answer,top)
            
            
        btn_cerca=tk.Button(frame,text="Cerca", padx=50, pady=10, bg="yellow",font=('arial',8,'bold'),command=cerca)
        btn_cerca.pack(pady=5)
        
    elif number==7:
        frame=tk.LabelFrame(top, text="Inserisci la valutazione(0-5):", padx=20,pady=10,background="lightgray",font=('arial',10,'bold'))  
        frame.pack(pady=5)
        
        inp=tk.Entry(frame,width=20, borderwidth=3, font=('Helvetica', 10))
        inp.pack()
        def cerca():
            if float(inp.get())<0 or float(inp.get())>5:
                messagebox.showerror("Errore", "Valore inserito errato")
                inp.delete(0, 'end')
            else:
                rate=inp.get()
                answer='' 
                for val in prolog.query("searchTopR(Y,Z,"+rate+")"):
                    answer=answer+str(val["Y"])+' '+str(val["Z"])+' - '
                inp.delete(0, 'end')
                show_result(answer,top)
 
        btn_cerca=tk.Button(frame,text="Cerca", padx=50, pady=10, bg="yellow",command=cerca,font=('arial',8,'bold'))
        btn_cerca.pack(pady=5)
        
    elif number==8:
        frame=tk.LabelFrame(top, text="Scegli il tipo di itenerario:", padx=20,pady=10,background="lightgray",font=('arial',10,'bold'))  
        frame.pack(pady=5)
        
        def cerca_percorso(tipo):
            answer=''
            price=''
            time=''
            tipo=str(tipo.get())
            for val in prolog.query("path(Monument,"+tipo+")"):
                answer=answer+str(val["Monument"])+' -> '      
            for val in prolog.query("pricePath("+tipo+",Prezzo)"):
                price=price+str(val)
            for val in prolog.query("timePath("+tipo+",Tempo)"):
                time=time+str(val)
            result=answer+'\n'+price+'\n'+time
            show_result(result,top)


        
        tipo_percorso=tk.IntVar()
        
        c1=tk.Checkbutton(frame, text="Completo", variable=tipo_percorso, onvalue=1, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:cerca_percorso(tipo_percorso)) 
        c1.deselect()
        c1.pack(side='top', anchor='w', pady=5)

        c2=tk.Checkbutton(frame, text="Medio", variable=tipo_percorso, onvalue=2, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:cerca_percorso(tipo_percorso))
        c2.pack(side='top', anchor='w', pady=5)
        c2.deselect()
        
        c3=tk.Checkbutton(frame, text="Breve", variable=tipo_percorso, onvalue=3, offvalue=0,background="lightgray",font=('arial',13,'bold'),command=lambda:cerca_percorso(tipo_percorso))
        c3.pack(side='top', anchor='w', pady=5)
        c3.deselect()
        
    elif number==9:
        frame=tk.LabelFrame(top, text="Seleziona attrazione di partenza:", padx=20,pady=10,background="lightgray",font=('arial',10,'bold'))  
        frame.pack(pady=5)
        
        #funzioni per stampa della lista da Prolog 
        def format_value(value):
            output = ""
            if isinstance(value, list):
                output = "[ " + ", ".join([format_value(val) for val in value]) + " ]"
            elif isinstance(value, Functor) and value.arity == 2:
                output = "{0}{1}{2}".format(value.args[0], value.name, value.args[1])
            else:
                output = "{}".format(value)

            return output


        def format_result(result):
            result = list(result)

            if len(result) == 0:
                return "false."

            if len(result) == 1 and len(result[0]) == 0:
                return "true."

            output = ""
            for res in result:
                tmpOutput = []
                for var in res:
                    tmpOutput.append(var + " = " + format_value(res[var]))
                output += ", ".join(tmpOutput) + " ;\n"
            output = output[:-3] + " ."

            return output
        
        def select(event):
            luogo_partenza=box_1scelta.get()
            frame_2=tk.LabelFrame(frame, text="Seleziona attrazione di arrivo:", padx=20,pady=10,background="lightgray",font=('arial',10,'bold'))  
            frame_2.pack(pady=5)
            
            def select2(event):
                prolog2.retractall("destinazione(X)")  #cancella i fatti precedenti nel buffer 
                luogo_arrivo=box_2scelta.get()
                prolog2.assertz('destinazione('+luogo_arrivo+')')
                
                result=list(prolog2.query("cercaPercorso("+luogo_partenza+", Percorso)"))

                if len(result)>1:
                    lista=[] #lista per stampare solo i primi 2 percorsi
                    for i in range(2) :
                        lista.append(result[i])
                    show_result(format_result(lista),top)
                    
                else:
                    show_result(format_result(result),top)
                
                    
            box_2scelta=ttk.Combobox(frame_2, values=options_attr)
            box_2scelta.pack(pady=5)
            box_2scelta.set("seleziona")
            box_2scelta.bind("<<ComboboxSelected>>",select2)
                
            
        box_1scelta=ttk.Combobox(frame, values=options_attr)
        box_1scelta.pack(pady=5)
        box_1scelta.set("seleziona")
        box_1scelta.bind("<<ComboboxSelected>>",select)
        
        
        
       
        
      
        
      
    
        
        
        

            
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
    
    
        
    
