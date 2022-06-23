s(madonnaDellaStella,ponte).
s(ponte,bastione).
s(ponte,madonnaDellaStella).
s(bastione,ponte).
s(bastione,santaLucia).
s(bastione,sanBasilio).
s(bastione,sanFrancesco).
s(sanFrancesco,bastione).
s(sanFrancesco,santaSofia).
s(sanFrancesco,castello).
s(castello,sanFrancesco).
s(castello,palazzoOrsini).
s(santaSofia,sanFrancesco).
s(santaSofia,sanBasilio).
s(santaSofia,purgatorio).
s(santaLucia,bastione).
s(santaLucia,sanBasilio).
s(sanBasilio,santaLucia).
s(sanBasilio,bastione).
s(sanBasilio,santaSofia).
s(sanBasilio,purgatorio).
s(purgatorio,santaSofia).
s(purgatorio,sanBasilio).
s(purgatorio,palazzoOrsini).
s(purgatorio,museoCivico).
s(purgatorio,bibliotecaFinya).
s(purgatorio,quattroFontane).
s(purgatorio,torreOrologio).
s(palazzoOrsini,castello).
s(palazzoOrsini,torreOrologio).
s(palazzoOrsini,purgatorio).
s(museoCivico,statuaPapa).
s(museoCivico,purgatorio).
s(museoCivico,bibliotecaFinya).
s(statuaPapa,cattedrale).
s(statuaPapa,museoCivico).
s(cattedrale,statuaPapa).
s(cattedrale,sanMichele).
s(sanMichele,cattedrale).
s(sanMichele,bibliotecaFinya).
s(sanMichele,quattroFontane).
s(sanMichele,torreOrologio).
s(bibliotecaFinya,museoCivico).
s(bibliotecaFinya,sanMichele).
s(bibliotecaFinya,purgatorio).
s(bibliotecaFinya,quattroFontane).
s(quattroFontane,purgatorio).
s(quattroFontane,bibliotecaFinya).
s(quattroFontane,sanMichele).
s(quattroFontane,torreOrologio).
s(torreOrologio,palazzoOrsini).
s(torreOrologio,purgatorio).
s(torreOrologio,quattroFontane).
s(torreOrologio,sanMichele).


cercaPercorso(Nodo,Percorso):-
   bfs([[Nodo]],P),
   inverti(P,Percorso).


bfs([[Nodo|Perc]|_],[Nodo|Perc]):-
    destinazione(Nodo).
bfs([Percorso|Percorsi],Soluzione):-
    espansione(Percorso,PercorsiEstesi),
    append(Percorsi,PercorsiEstesi,NuoviPercorsi),
    bfs(NuoviPercorsi,Soluzione).
espansione([N|Perc],Percorsi):-
    findall([NN,N|Perc],(s(N,NN),\+ member(NN,[N|Perc])),Percorsi).


%funzioni per invertire la stampa della lista
inverti(Lista,Invertita):-
    inverti0(Lista,[],Invertita).
inverti0([],Invertita,Invertita).
inverti0([T|C],Parziale,Invertita):-
    inverti0(C,[T|Parziale],Invertita).


