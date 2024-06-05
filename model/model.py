import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self.pesoMax = 0
        self._deltaMax = []


    def buildGraph(self, genere):
        canzoni = DAO.getAllSongs(genere)
        for c in canzoni:
            self._grafo.add_node(c)
        print("entro")
        self.addEdgesPesati()
        print("esco")

    def addEdgesPesati(self):
        for n1 in self._grafo.nodes:
            for n2 in self._grafo.nodes:
                if n1 != n2:
                    if self._grafo.has_edge(n1, n2) is False:
                        peso = DAO.getArchiPesati(n1.TrackId, n2.TrackId)
                        if peso != []:
                            if peso > 0:
                                self._grafo.add_edge(n1, n2, weight=peso)
                                if peso == self.pesoMax:
                                    self._deltaMax.append((n1, n2, peso))
                                elif peso > self.pesoMax:
                                    self._deltaMax = []
                                    self._deltaMax.append((n1, n2, peso))
                                    self.pesoMax = peso

    def getGenere(self):
        genere = set()
        genre = DAO.getName()
        for g in genre:
            genere.add(g)
        return genere

    def getMaxArco(self):
        return self._deltaMax

    def getCaratteristiche(self):
        return len(self._grafo.nodes), len(self._grafo.edges)