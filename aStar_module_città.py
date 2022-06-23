# -*- coding: utf-8 -*-


from math import cos, asin, sqrt
import sys

# funzione per calcolare la distanza tra due punti in base alla loro latitudine e longitudine

def distance(c1, c2):
    
    p = 0.017453292519943295   
    a = 0.5 - cos((c2.lat - c1.lat) * p)/2 + cos(c1.lat * p) * cos(c2.lat * p) * (1 - cos((c2.lon - c1.lon) * p)) / 2
    d=int((12742 * asin(sqrt(a))))  
    return d

# funzione per verificare se due nodi sono uguali
def is_same_node(c1, c2):
    return c1.lat==c2.lat and c1.lon==c2.lon

#classe che rappresenta le coordinate della città con lat(latitudine) e lon(longitudine)
class Coord:   
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# classe per rappresentare ogni nodo del grafo
class City:
    def __init__(self, coord, name):
        self.coord = coord
        self.name = name
        self.costG = 0      #funzione che somma il costo sugli archi di ogni nodo, per raggiungere n dal nodo start
        self.costH = 0      #funzione euristica, fornisce una stima ottimista della distanza che separe n dal nodo di arrivo. Distanza in linea d'aria
        self.costF = 0      #funzione di costo F(n) che somma g(n)+h(n). E' una stima di costo associato al percorso che congiunge il nodo di partenza a quello di arrivo passando per n
        self.parent = None
        self.neighbors = None

    def add_neighbors(self, neighbors):
        self.neighbors = neighbors

# classe per rappresentare il collegamento tra due città con un costo che è la distance(integer) in questo caso 
class Bow:    
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost

#classe che implementa l'algoritmo A*
class AStar:
   
    current_coord = Coord(0,0)
    open_set = dict()       #nodi terminali dei tracciati parziali
    close_set = dict()      #nodi intermedi dei tracciati già esaminati, dai quali non si deve più passare

    def __init__(self, map_graph, source_coord, target_coord):
        super().__init__()
        self.map_graph = map_graph
        self.source_coord = source_coord
        self.target_coord = target_coord
        
        self.current_coord = self.source_coord

    # calcola il valore g per qualsiasi nodo, g value è il costo dalla sorgente al nodo (variabile passata nel parametro)
    def compute_g(self, node):
       
        if is_same_node(node.coord, self.source_coord):
            return 0
        ci = 0
        for c in node.neighbors:
            if is_same_node(node.parent, c.dest):
                ci = c.cost
                break
        return ci + self.compute_g(self.map_graph[node.parent])

    # convalida i vicini del nodo corrente
    def validate_neighbors(self):
        
        for bow in self.map_graph[self.current_coord].neighbors:

            if bow.dest in self.close_set:
                continue

            tmp_node = self.map_graph[bow.dest]
            tmp_node.parent = self.current_coord
            tmp_node.costG = self.compute_g(tmp_node)

            if tmp_node.costH == 0:
                tmp_node.costH = distance(bow.dest, self.target_coord)
                self.map_graph[bow.dest].costH = tmp_node.costH
            tmp_node.costF = tmp_node.costG + tmp_node.costH
            
            if tmp_node.coord in self.open_set:
                if tmp_node.costF < self.open_set[tmp_node.coord].costF:
                    self.open_set[tmp_node.coord] = tmp_node
            else:
                self.open_set[tmp_node.coord] = tmp_node
        
    # cerca il miglior vicino del nodo corrente e lo restituisce
    def searching_good_neighbor(self):

        min_cost = sys.maxsize
        min_coord = Coord(0,0)
        
        for key, value in self.open_set.items():
            if min_cost > value.costF:
                min_cost = value.costF
                min_coord = key

        return min_coord

    #funzione che ricostruisce il percorso dalla destinazione alla sorgente
    def rebuild_route(self):
        tmp = self.close_set[self.target_coord]
        lst_city=[tmp.name]
        lst_route=''

        while tmp.parent is not None:
            tmp = self.close_set[tmp.parent]
            lst_city.insert(0,tmp.name)
        
        trg= self.close_set[self.target_coord]
        for city in lst_city:
            if city==trg.name:
                lst_route=lst_route+str(city)
            else:
                lst_route=lst_route+str(city)+' => '
                
        dtot=trg.costG
        str_km="Lunghezza totale del percorso = "+str(dtot)+"km"
        return lst_route, str_km, lst_city
        
            
        
    # a star algorithm funzione main        
    def a_star(self):
        # inizializza current_coord, open_set and close_set
        self.map_graph[self.source_coord].costF = self.map_graph[self.source_coord].costH = distance(self.source_coord, self.target_coord)
        self.close_set[self.current_coord] = self.open_set[self.current_coord] = self.map_graph[self.current_coord]
        while not is_same_node(self.current_coord, self.target_coord) and self.open_set:

            # chiama la funzione validate_neighbors 
            self.validate_neighbors()
            # chiama la funzione searching_good_neighbor e change current_coord value
            self.current_coord = self.searching_good_neighbor()

            # aggiunge la nuova current_coord a close_set e la elimina da open_set
            self.close_set[self.current_coord] = self.open_set[self.current_coord]
            del self.open_set[self.current_coord]
        
        if is_same_node(self.current_coord, self.target_coord):
            lst_route, str_km,lst_city=self.rebuild_route()
        else:
            print('Non abbiamo trovato nessun percorso.')
            
        
        return lst_route, str_km, lst_city
            
            
            
            
            
            
            
            
            
            
            
            
            
            