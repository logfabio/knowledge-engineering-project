# -*- coding: utf-8 -*-

import aStar_module_città as Astar



def calcola(start,target):
# Dati 
    Foggia = Astar.City(Astar.Coord(41.46242580760686, 15.545199711345404), 'Foggia') 
    Cerignola = Astar.City(Astar.Coord(41.2675849081224, 15.89058683036433), 'Cerignola')
    Canosa = Astar.City(Astar.Coord(41.22520902849107, 16.065619624108606), 'Canosa di Puglia')
    Minervino = Astar.City(Astar.Coord(41.08812296386393, 16.08067110828517), 'Minervino Murge')
    Poggiorsini = Astar.City(Astar.Coord(40.91479675869128, 16.25486240167788), 'Poggiorsini')
    Gravina = Astar.City(Astar.Coord(40.82133108339727, 16.41691073922572), 'Gravina in Puglia')
    Irsina = Astar.City(Astar.Coord(40.7443176538034, 16.24939041184742), 'Irsina')
    Tolve = Astar.City(Astar.Coord(40.69647954248639, 16.023132647409458), 'Tolve')
    Potenza = Astar.City(Astar.Coord(40.64050215767174, 15.823093594441614), 'Potenza')
    Tricarico = Astar.City(Astar.Coord(40.61618155835437, 16.161994711851804), 'Tricarico')
    Grassano = Astar.City(Astar.Coord(40.63239627530072, 16.284348695705923), 'Grassano')
    Matera = Astar.City(Astar.Coord(40.667866048690904, 16.608484837782242), 'Matera')
    Barletta = Astar.City(Astar.Coord(41.31899306562209, 16.283623352787874), 'Barletta')
    Andria = Astar.City(Astar.Coord(41.227034904682505, 16.300616960213407), 'Andria')
    Trani = Astar.City(Astar.Coord(41.27740899128333, 16.41617350196317), 'Trani')
    Corato = Astar.City(Astar.Coord(41.15469120643664, 16.418115630134082), 'Corato')
    Bisceglie = Astar.City(Astar.Coord(41.24302835958467, 16.501292854610746), 'Bisceglie')
    Bitonto= Astar.City(Astar.Coord(41.10658032110071, 16.685836251196267), 'Bitonto') 
    Molfetta= Astar.City(Astar.Coord(41.20372114701902, 16.606629572130803), 'Molfetta') 
    Bari= Astar.City(Astar.Coord(41.11888458211866, 16.869563090775944), 'Bari') 
    Polignano= Astar.City(Astar.Coord(40.99512187364798, 17.23130081063164), 'Polignano a Mare') 
    Modugno= Astar.City(Astar.Coord(41.083811349959916, 16.79035640737658), 'Modugno') 
    Palo= Astar.City(Astar.Coord(41.056724467186115, 16.720131929029876), 'Palo del Colle') 
    Toritto= Astar.City(Astar.Coord(40.99881965440613, 16.676037489137762), 'Toritto') 
    Altamura= Astar.City(Astar.Coord(40.82444873044704, 16.552179905011865), 'Altamura') 
    Monopoli= Astar.City(Astar.Coord(40.954432593873875, 17.29907560012684), 'Monopoli') 
    Putignano= Astar.City(Astar.Coord(40.856305390354024, 17.11371564194155), 'Putignano') 
    Santeramo= Astar.City(Astar.Coord(40.79586480572451, 16.751307099507784), 'Santeramo in Colle') 
    Fasano= Astar.City(Astar.Coord(40.83777449639673, 17.35460194092233), 'Fasano') 
    Alberobello= Astar.City(Astar.Coord(40.78895169159462, 17.241916151322084), 'Alberobello') 
    Gioia= Astar.City(Astar.Coord(40.79713022621459, 16.91964914532031), 'Gioia del Colle') 
    Ostuni= Astar.City(Astar.Coord(40.7320494785144, 17.577523840220824), 'Ostuni') 
    Brindisi= Astar.City(Astar.Coord(40.631197225875304, 17.94287614143071), 'Brindisi') 
    Taranto= Astar.City(Astar.Coord(40.46310555954633, 17.246274633066857), 'Taranto') 
    Lecce= Astar.City(Astar.Coord(40.35136798103586, 18.17391997087861), 'Lecce') 

# Aggiungo i neighbors per ogni attrazione turistica
    Foggia.add_neighbors([Astar.Bow(Cerignola.coord, 40)])
    Cerignola.add_neighbors([Astar.Bow(Foggia.coord, 40),Astar.Bow(Barletta.coord, 40),Astar.Bow(Canosa.coord, 17)])
    Canosa.add_neighbors([Astar.Bow(Cerignola.coord, 17), Astar.Bow(Barletta.coord, 22), Astar.Bow(Andria.coord, 25),Astar.Bow(Minervino.coord, 17)])
    Minervino.add_neighbors([Astar.Bow(Canosa.coord, 17), Astar.Bow(Poggiorsini.coord, 30)])
    Poggiorsini.add_neighbors([Astar.Bow(Minervino.coord, 30), Astar.Bow(Andria.coord, 46),Astar.Bow(Corato.coord, 35),Astar.Bow(Gravina.coord, 19)])
    Gravina.add_neighbors([Astar.Bow(Poggiorsini.coord, 19), Astar.Bow(Altamura.coord, 13),Astar.Bow(Corato.coord, 42),Astar.Bow(Matera.coord, 28),Astar.Bow(Irsina.coord, 23)])
    Irsina.add_neighbors([Astar.Bow(Gravina.coord, 23), Astar.Bow(Tolve.coord, 33)])
    Tolve.add_neighbors([Astar.Bow(Irsina.coord, 33), Astar.Bow(Potenza.coord, 25)])
    Potenza.add_neighbors([Astar.Bow(Tolve.coord, 25), Astar.Bow(Tricarico.coord, 42)])
    Tricarico.add_neighbors([Astar.Bow(Potenza.coord, 42), Astar.Bow(Grassano.coord, 18)])
    Grassano.add_neighbors([Astar.Bow(Tricarico.coord, 18), Astar.Bow(Matera.coord, 35)])
    Matera.add_neighbors([Astar.Bow(Grassano.coord, 35), Astar.Bow(Gravina.coord, 28), Astar.Bow(Altamura.coord, 19),Astar.Bow(Santeramo.coord, 22),Astar.Bow(Taranto.coord, 73)])
    Taranto.add_neighbors([Astar.Bow(Matera.coord, 73), Astar.Bow(Gioia.coord, 50), Astar.Bow(Brindisi.coord, 71), Astar.Bow(Lecce.coord, 102)])
    Lecce.add_neighbors([Astar.Bow(Taranto.coord, 102), Astar.Bow(Brindisi.coord, 39)])
    Brindisi.add_neighbors([Astar.Bow(Lecce.coord, 39), Astar.Bow(Taranto.coord, 71), Astar.Bow(Ostuni.coord, 38)])
    Ostuni.add_neighbors([Astar.Bow(Brindisi.coord, 38), Astar.Bow(Fasano.coord, 24), Astar.Bow(Alberobello.coord, 36)])
    Fasano.add_neighbors([Astar.Bow(Ostuni.coord, 24), Astar.Bow(Alberobello.coord, 20), Astar.Bow(Monopoli.coord, 16)])
    Alberobello.add_neighbors([Astar.Bow(Fasano.coord, 20), Astar.Bow(Ostuni.coord, 36), Astar.Bow(Putignano.coord, 14)])
    Putignano.add_neighbors([Astar.Bow(Alberobello.coord, 14), Astar.Bow(Gioia.coord, 21), Astar.Bow(Monopoli.coord, 21)])
    Gioia.add_neighbors([Astar.Bow(Putignano.coord, 21), Astar.Bow(Taranto.coord, 50), Astar.Bow(Santeramo.coord, 15)])
    Santeramo.add_neighbors([Astar.Bow(Gioia.coord, 15), Astar.Bow(Matera.coord, 22), Astar.Bow(Altamura.coord, 18)])
    Altamura.add_neighbors([Astar.Bow(Santeramo.coord, 18), Astar.Bow(Matera.coord, 19), Astar.Bow(Gravina.coord, 13),Astar.Bow(Toritto.coord, 25)])
    Toritto.add_neighbors([Astar.Bow(Altamura.coord, 25), Astar.Bow(Palo.coord, 9)])
    Palo.add_neighbors([Astar.Bow(Toritto.coord, 9), Astar.Bow(Modugno.coord, 9), Astar.Bow(Bitonto.coord, 7)])
    Modugno.add_neighbors([Astar.Bow(Palo.coord, 9), Astar.Bow(Bari.coord, 11), Astar.Bow(Bitonto.coord, 10)])
    Bari.add_neighbors([Astar.Bow(Modugno.coord, 11), Astar.Bow(Polignano.coord, 39), Astar.Bow(Molfetta.coord, 35)])
    Polignano.add_neighbors([Astar.Bow(Bari.coord, 39), Astar.Bow(Monopoli.coord, 8)])
    Monopoli.add_neighbors([Astar.Bow(Polignano.coord, 8), Astar.Bow(Fasano.coord, 16), Astar.Bow(Putignano.coord, 21)])
    Bitonto.add_neighbors([Astar.Bow(Modugno.coord, 10), Astar.Bow(Palo.coord, 7), Astar.Bow(Molfetta.coord, 17),Astar.Bow(Corato.coord, 27)])
    Molfetta.add_neighbors([Astar.Bow(Bitonto.coord, 17), Astar.Bow(Bari.coord, 35), Astar.Bow(Corato.coord, 22),Astar.Bow(Bisceglie.coord, 11)])
    Corato.add_neighbors([Astar.Bow(Molfetta.coord, 22), Astar.Bow(Bitonto.coord, 27), Astar.Bow(Bisceglie.coord, 16),Astar.Bow(Trani.coord, 15),Astar.Bow(Andria.coord, 15),Astar.Bow(Poggiorsini.coord, 35),Astar.Bow(Gravina.coord, 42)])
    Andria.add_neighbors([Astar.Bow(Corato.coord, 15), Astar.Bow(Trani.coord, 13), Astar.Bow(Barletta.coord, 12),Astar.Bow(Canosa.coord, 25),Astar.Bow(Poggiorsini.coord, 46)])
    Trani.add_neighbors([Astar.Bow(Andria.coord, 13), Astar.Bow(Corato.coord, 15), Astar.Bow(Bisceglie.coord, 10), Astar.Bow(Barletta.coord, 13)])
    Barletta.add_neighbors([Astar.Bow(Trani.coord, 13), Astar.Bow(Andria.coord, 12), Astar.Bow(Canosa.coord, 22),Astar.Bow(Cerignola.coord, 40)])
    Bisceglie.add_neighbors([Astar.Bow(Trani.coord, 10), Astar.Bow(Corato.coord, 16), Astar.Bow(Molfetta.coord, 11)])
    
# dizioario per rappresentare il grafo
    city_graph = {
        Foggia.coord : Foggia,
        Cerignola.coord : Cerignola,
        Canosa.coord : Canosa,
        Minervino.coord : Minervino,
        Poggiorsini.coord : Poggiorsini,
        Gravina.coord : Gravina,
        Irsina.coord : Irsina,
        Tolve.coord : Tolve,
        Potenza.coord : Potenza,
        Tricarico.coord : Tricarico,
        Grassano.coord : Grassano,  
        Matera.coord : Matera,
        Taranto.coord : Taranto,
        Lecce.coord : Lecce,
        Brindisi.coord : Brindisi,
        Ostuni.coord : Ostuni,
        Fasano.coord : Fasano,
        Alberobello.coord : Alberobello,
        Putignano.coord : Putignano,
        Gioia.coord : Gioia,
        Santeramo.coord : Santeramo,
        Altamura.coord : Altamura,
        Palo.coord : Palo,
        Modugno.coord : Modugno,
        Bari.coord : Bari,
        Polignano.coord : Polignano,
        Monopoli.coord : Monopoli,
        Bitonto.coord : Bitonto,
        Molfetta.coord : Molfetta,
        Corato.coord : Corato,
        Andria.coord : Andria,
        Trani.coord : Trani,
        Toritto.coord : Toritto,
        Barletta.coord : Barletta,
        Bisceglie.coord : Bisceglie,
        }
    
    #Dizionario per costruire l'oggetto city
    city_build = {
        'Foggia' : Foggia,
        'Cerignola': Cerignola,
        'Canosa' : Canosa,
        'Minervino' : Minervino,
        'Poggiorsini' : Poggiorsini,
        'Gravina' : Gravina,
        'Irsina' : Irsina,
        'Tolve' : Tolve,
        'Potenza' : Potenza,
        'Tricarico' : Tricarico,
        'Grassano' : Grassano,  
        'Matera' : Matera,
        'Taranto' : Taranto,
        'Lecce' : Lecce,
        'Brindisi' : Brindisi,
        'Ostuni' : Ostuni,
        'Fasano' : Fasano,
        'Alberobello' : Alberobello,
        'Putignano' : Putignano,
        'Gioia' : Gioia,
        'Santeramo' : Santeramo,
        'Altamura' : Altamura,
        'Palo' : Palo,
        'Modugno' : Modugno,
        'Bari' : Bari,
        'Polignano' : Polignano,
        'Monopoli' : Monopoli,
        'Bitonto' : Bitonto,
        'Molfetta' : Molfetta,
        'Corato' : Corato,
        'Andria' : Andria,
        'Trani' : Trani,
        'Toritto' : Toritto,
        'Barletta' : Barletta,
        'Bisceglie' : Bisceglie,
        }
    
    city_start=city_build[start]
    city_target=city_build[target]
    
    astar = Astar.AStar(map_graph=city_graph, source_coord=city_start.coord, target_coord=city_target.coord)
    lst_route, str_km, lst_city=astar.a_star()
    
    return lst_route, str_km, lst_city
        
























