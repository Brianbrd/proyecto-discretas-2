from src.proyecto_discretas_2.graph import (
    has_cycle,
    is_connected,
    is_forest,
    is_tree,
    load_graph_from_file,
)

# Prueba cargando el archivo ejemplo_1.csv
g = load_graph_from_file('ejemplo_1.csv', directed=False)

print('--- Resultados para ejemplo_1.csv ---')
is_connected(g)
has_cycle(g)
is_tree(g)
is_forest(g)    