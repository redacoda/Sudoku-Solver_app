! Si vous téléchargez les fichiers il risque d'y avoir des erreurs d'emplacement alors prétez y attention !

Explication: 
Je voulais résoudre des sudokus plus rapidement j'ai donc créer un code pour le faire à ma place.

---------------------------------------------------------------------

Organisation des cp (composants) dans les blocs:

cp1, cp2, cp3
cp4, cp5, cp6
cp7, cp8, cp9

Chaque cp a un dictionnaire associé qui se présente sous les formes suivantes : 

Pour les cases libres :
dict = {"free", [i], n° de ligne}

Pour les cases occupées :
dict = {"used", [i], n° de ligne, [issues possibles]}

---------------------------------------------------------------------

Dispositions des blocs :

A1, B1, C1
A2, B2, C2
A3, B3, C3

---------------------------------------------------------------------

self.a et self.o :

Ils donnent la position du cp1 et sont utilisés pour situer le bloc.
