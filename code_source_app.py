# grandict est un dictionnaire qui contient toutes les possibilités de chaque case pour pour être à jour entre chaque méthode de résolution
grandict = {}
for i in range(1, 82):  
    grandict[str(i)] = []

class Parent():
    def __init__(self, cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9):
        self.cp1 = cp1
        self.cp2 = cp2
        self.cp3 = cp3
        self.cp4 = cp4
        self.cp5 = cp5
        self.cp6 = cp6
        self.cp7 = cp7
        self.cp8 = cp8
        self.cp9 = cp9
        self.entier = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
    # Fonction pour déterminer les nombres manquants dans un bloc 
    def manquants(self):
        values = [self.cp1, self.cp2, self.cp3, self.cp4, self.cp5, self.cp6, self.cp7, self.cp8, self.cp9]
        resultat = []

        for i in self.entier:
            if i not in values:
                resultat.append(i)
        return resultat

# Classe qui hérite de la classe parent 
class m_bloc(Parent):
    def __init__(self, cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9, o, a, L1, L2, L3, L4, L5, L6, L7, L8, L9):
            super().__init__(cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9)
            self.o = o
            self.a = a
            self.dict = {}
            self.coordlist ={
                    "L1": L1,
                    "L2": L2,
                    "L3": L3,
                    "L4": L4,
                    "L5": L5,
                    "L6": L6,
                    "L7": L7,
                    "L8": L8,
                    "L9": L9
                }
            self.coords = {
                    "cp1": (0, 0),
                    "cp2": (1, 0),
                    "cp3": (2, 0),
                    "cp4": (0, 1),
                    "cp5": (1, 1),
                    "cp6": (2, 1),
                    "cp7": (0, 2),
                    "cp8": (1, 2),
                    "cp9": (2, 2)
                }
            self.L1 = L1
            self.L2 = L2
            self.L3 = L3
            self.L4 = L4
            self.L5 = L5
            self.L6 = L6
            self.L7 = L7
            self.L8 = L8
            self.L9 = L9

    def cases(self):
        # [values] est liste qui contient tous les composants du bloc
        values = [self.cp1, self.cp2, self.cp3, self.cp4, self.cp5, self.cp6, self.cp7, self.cp8, self.cp9]
        a = 0
        
        # On attribut un état à chaque case pour savoir si elle est libre ou non (dans le dict)
        for e in values:
            a += 1
            key = f"cp{a}"
            if e not in self.entier:
                self.dict[key] = ["free"]
            else:
                self.dict[key] = ["used"]
        
        # On renseigne dans le dict l'indice et la ligne de chaque cp
        for e in self.dict:
            if e in self.coords:
                x, y = self.coords[e]
                self.dict[e].append(self.a + x)
                self.dict[e].append(self.o + y)
        
        for e in self.dict:
            if e in self.coords:
                x, y = self.coords[e]
                # Si la case est libre ...
                if self.dict[e][0] == "free": 
                    # ... on lui ajoute la liste les valeurs manquantes au bloc.
                    self.dict[e].append(m_bloc.manquants(self))
                    lista = [self.L1[self.a + x], self.L2[self.a + x], self.L3[self.a + x], self.L4[self.a + x], self.L5[self.a + x], self.L6[self.a + x], self.L7[self.a + x], self.L8[self.a + x], self.L9[self.a + x]]
                    # On regarde si chaque possibilité du cp se trouve la colone (lista) de celui-ci
                    for z in lista:
                        if z in self.dict[e][3]:
                            # Si oui la valeur est invalide et elle retiré des issues possibles (dict[3])
                            self.dict[e][3].remove(z)
                                            
        nom = self.o + y
        for u in self.dict:
            listo = []
            generaliste = []
            x, y = self.coords[u]
            nom = self.o + y
            # Si la case est libre ...
            if self.dict[u][0] == "free":
                numlist = self.coordlist[f"L{nom}"]
                listo.extend(numlist)
                for elements in self.dict[u][3]:
                        generaliste.append(elements)
                for x in generaliste:
                    # ... on regarde si chaque possibilité du cp se trouve la ligne (listo) de celui-ci
                    if x in listo:
                        # Si oui la est invalide et elle retiré des issues possibles (dict[3])
                        self.dict[u][3].remove(x)

    def apply(self):
        for i in self.dict:
            ind = self.dict[i][1]
            l = self.dict[i][2]
            num_dict = 9 * (l-1) + 1 + ind
            if self.dict[i][0] == "free": 
                grandict[str(num_dict)].extend(self.dict[i][3])
            if self.dict[i][0] == "used":
                grandict[str(num_dict)] = []

    def resolution(self):
        # general est une liste qui contient toutes les issues possibles de chaque cp "free".
        general = [] 
        for n in self.dict:
            if self.dict[n][0] == "free":
                # extend est utilisé pour "unlister" une liste pour ne pas avoir de listes dans [genéral].
                general.extend(self.dict[n][3])
        
        # Règle de résolution 1 : Si une valeur x n'est possible que dans un seul cp, on la lui applique on supprime x des possibilités de tous les autres cp..        
        for w in general:
            # Si dans général une valeur est en un seul exemplaire...
            compte = general.count(w)
            if compte == 1:
                for g in self.dict:
                        if self.dict[g][0] == "free":
                            # ... c'est à dire que cette valeur est forcément la bonne. 
                            # On cherche ou situe w (soit l'issue certaine) 
                            if w in self.dict[g][3]:
                                self.dict[g][3].clear()
                                vart = self.dict[g][2]
                                listname = self.coordlist[f"L{vart}"]
                                # On modifie la cases de la grille associée à ce cp.
                                listname[self.dict[g][1]] = w
                                
        # Règle de résolution 2 : Si un cp n'a qu'une seule possibilité x, l'appliquer et supprimer x des possibilités de tous les autres cp.     
        for z in self.dict:
            if self.dict[z][0] == "free":    
                if len(self.dict[z][3]) == 1: 
                    Line = self.coordlist[f"L{self.dict[z][2]}"]
                    réponse = self.dict[z][3][0]
                    # On modifie la cases de la grille associée à ce cp.
                    Line[self.dict[z][1]] = réponse
                    for b in self.dict:
                        if self.dict[b][0] == "free":
                            if réponse in self.dict[b][3]:
                                self.dict[b][3].remove(réponse)                                                       

# Cette classe permet de résoudre des sudokus plus complexes en élargissant le champ de vision de notre programme du bloc à la ligne
class Advenced_res():
    def __init__(self, A1, B1, C1, A2, B2, C2, A3, B3, C3, ln1, ln2, ln3, ln4, ln5, ln6, ln7, ln8, ln9, L1, L2, L3, L4, L5, L6, L7, L8, L9):
        self.A1 = A1
        self.B1 = B1
        self.C1 = C1
        self.A2 = A2
        self.B2 = B2
        self.C2 = C2
        self.A3 = A3
        self.B3 = B3
        self.C3 = C3
        self.lines = {
            "ln1": ln1,
            "ln2": ln2,
            "ln3": ln3,
            "ln4": ln4,
            "ln5": ln5,
            "ln6": ln6,
            "ln7": ln7,
            "ln8": ln8,
            "ln9": ln9
        }
        self.ultime_liste = []
        self.coordlist ={
        "L1": L1,
        "L2": L2,
        "L3": L3,
        "L4": L4,
        "L5": L5,
        "L6": L6,
        "L7": L7,
        "L8": L8,
        "L9": L9
    }
        
    def catalogue(self):
        # Cette méthode est utilisée pour pour cataloguer ou regrouper toutes les possibilités/issues posibles de chaque compossant elles même enregistrées dans les dictionnaires de chaque bloc
        obj_list = [self.A1, self.B1, self.C1, self.A2, self.B2, self.C2, self.A3, self.B3, self.C3]
        # On appel les méthode de tous les objets
        for obj in obj_list:
            self.ultime_liste.append(obj.dict)
    
    def res(self):
        for dict in self.ultime_liste:
            for keys in dict:
                # Si la case n'est pas déja occupée ...
                if dict[keys][0] == "free":
                    # on stocke le n° de la ligne dans l et on veut dans les 3 prochaines lignes récupérer la liste "ORIGINALE" (celle qui figure dans les arguments de la classe) qui correspond à la ligne du composant mais on veut aussi récupérer les keys pour accéder à grandict. Enfin on stocke cette liste dans listenum.
                    l = dict[keys][2]
                    lnum = self.lines[f"ln{l}"]
                    listnum = self.coordlist[f"L{l}"]
                    # On créer une liste pour la comparer avec la liste "ORIGINALE"
                    compare_list = []
                    for c in lnum:
                        compare_list.extend(list(set(grandict[c])))
                    for i in dict[keys][3]:
                        ni = compare_list.count(i)
                        if ni == 1:
                            listnum[dict[keys][1]] = i

def action(L1, L2, L3, L4, L5, L6, L7, L8, L9):
# Cette fonction correspond à l'action de résolution du sudoku.
    # on défini ln(x) pour avoir un accès (normalement) plus facile à grandict
    ln1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ln2 = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
    ln3 = ["19", "20", "21", "22", "23", "24", "25", "26", "27"]
    ln4 = ["28", "29", "30", "31", "32", "33", "34", "35", "36"]
    ln5 = ["37", "38", "39", "40", "41", "42", "43", "44", "45"]
    ln6 = ["46", "47", "48", "49", "50", "51", "52", "53", "54"]
    ln7 = ["55", "56", "57", "58", "59", "60", "61", "62", "63"]
    ln8 = ["64", "65", "66", "67", "68", "69", "70", "71", "72"]
    ln9 = ["73", "74", "75", "76", "77", "78", "79", "80", "81"]
    
    # On utilise une boucle car la résolution ne se fait pas en une fois
    for i in range(10):
        b1 = [L1[0], L1[1], L1[2], L2[0], L2[1], L2[2], L3[0], L3[1], L3[2]]
        b2 = [L4[0], L4[1], L4[2], L5[0], L5[1], L5[2], L6[0], L6[1], L6[2]]
        b3 = [L7[0], L7[1], L7[2], L8[0], L8[1], L8[2], L9[0], L9[1], L9[2]]
        b4 = [L1[3], L1[4], L1[5], L2[3], L2[4], L2[5], L3[3], L3[4], L3[5]]
        b5 = [L4[3], L4[4], L4[5], L5[3], L5[4], L5[5], L6[3], L6[4], L6[5]]
        b6 = [L7[3], L7[4], L7[5], L8[3], L8[4], L8[5], L9[3], L9[4], L9[5]]
        b7 = [L1[6], L1[7], L1[8], L2[6], L2[7], L2[8], L3[6], L3[7], L3[8]]
        b8 = [L4[6], L4[7], L4[8], L5[6], L5[7], L5[8], L6[6], L6[7], L6[8]]
        b9 = [L7[6], L7[7], L7[8], L8[6], L8[7], L8[8], L9[6], L9[7], L9[8]]
        
        # On redéfinit les objet à chaque itération de la boucle pour actualiser les valeurs de chaque case
        liste = [L1, L2, L3, L4, L5, L6, L7, L8, L9]
        # *b1[:9] permet de "dérouler" la liste affectée à b1 au lieu d'écrire --A1 = m_bloc(L1[0], L1[1], L1[2], L2[0], ...., 1, 0 ...)-- de même pour *liste[:9] qui permet de "dérouler" liste 
        A1 = m_bloc(*b1[:9], 1, 0, *liste[:9])
        A2 = m_bloc(*b2[:9], 4, 0, *liste[:9])
        A3 = m_bloc(*b3[:9], 7, 0, *liste[:9])
        B1 = m_bloc(*b4[:9], 1, 3, *liste[:9])
        B2 = m_bloc(*b5[:9], 4, 3, *liste[:9])
        B3 = m_bloc(*b6[:9], 7, 3, *liste[:9])
        C1 = m_bloc(*b7[:9], 1, 6, *liste[:9])
        C2 = m_bloc(*b8[:9], 4, 6, *liste[:9])
        C3 = m_bloc(*b9[:9], 7, 6, *liste[:9])
        
        
        obj_list = [A1, B1, C1, A2, B2, C2, A3, B3, C3]
        # On appel les méthode de tous les objets
        for obj in obj_list:
            obj.manquants()
            obj.cases()
            obj.apply()
            obj.resolution()
        # On appel la classe advenced_res une seule fois car elle couvre toute la grille
        adres = Advenced_res(A1, B1, C1, A2, B2, C2, A3, B3, C3, ln1, ln2, ln3, ln4, ln5, ln6, ln7, ln8, ln9, L1, L2, L3, L4, L5, L6, L7, L8, L9)
        adres.catalogue()
        adres.res()
