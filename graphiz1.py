from graphviz import Digraph

BasesdeDatos = ["Bd1","Bd2","Bd3","Bd4","Bd5","Bd6","Bd7","Bd1","Bd2","Bd3","Bd4","Bd5","Bd6","Bd7"]

g = Digraph('G', filename='hello.gv')

g.edge('Hello', 'World')

for i in BasesdeDatos:
    actual=

g.view()