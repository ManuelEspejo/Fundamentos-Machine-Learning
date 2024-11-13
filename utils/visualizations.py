import matplotlib.pyplot as plt
import networkx as nx


def draw_neural_net(layers, node_size=500, arrowsize=10):
    """
    layers: lista que contiene el número de neuronas en cada capa
    node_size: tamaño de los nodos
    arrowsize: tamaño de las flechas
    """
    plt.figure(figsize=(10, 6))  # Tamaño explícito de la figura
    G = nx.DiGraph()
    n_layers = len(layers)
    vertical_spacing = 1
    horizontal_spacing = 2
    node_counter = 0

    # Crear diccionario de posiciones desde el inicio
    pos = {}
    layer_nodes = []

    for i in range(n_layers):
        layer_size = layers[i]
        current_layer = []
        x = i * horizontal_spacing
        y_offset = (max(layers) - layer_size) / 2.0
        
        for j in range(layer_size):
            y = (j + y_offset) * vertical_spacing
            pos[node_counter] = (x, y)
            G.add_node(node_counter)
            current_layer.append(node_counter)
            node_counter += 1
            
        layer_nodes.append(current_layer)

    # Agregar conexiones entre capas
    for i in range(len(layer_nodes)-1):
        for source in layer_nodes[i]:
            for target in layer_nodes[i+1]:
                G.add_edge(source, target)

    # Dibujar el grafo con configuraciones específicas
    nx.draw(G, pos,
            with_labels=False,
            node_size=node_size,
            node_color='orange',
            arrowsize=arrowsize,
            edge_color='gray',
            arrows=True,
            width=0.5)
    
    plt.title('Red Neuronal Fully Connected')
    plt.axis('off')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.show()