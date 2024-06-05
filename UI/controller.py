import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        for g in self._model.getGenere():
            self._view.ddgenere.options.append(ft.dropdown.Option(text=f"{g.Name}", key=g.GenreId))


    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        genere = self._view.ddgenere.value
        if genere is None:
            self._view.txt_result.controls.append(ft.Text(f"devi selezionare un valore"))
            self._view.update_page()
            return
        self._model.buildGraph(genere)
        nNodes, nEdges = self._model.getCaratteristiche()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {nNodes} nodi e {nEdges} vertici"))
        self._view.update_page()

    def handle_delta_max(self, e):
        self._view.txt_result.controls.clear()
        pm = self._model.getMaxArco()
        for peso_max in pm:
            self._view.txt_result.controls.append(ft.Text(f"{peso_max[0].Name}***{peso_max[1].Name}-->{peso_max[2]}"))
        self._view.update_page()

    def handle_path(self, e):
        pass
