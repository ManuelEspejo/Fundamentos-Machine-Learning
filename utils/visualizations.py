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
    
# Notebook 03 - Aprendizaje por refuerzo

def visualize_q_learning_path(path, grid_size=5):
    """
    Visualiza el camino recorrido por el agente en una cuadrícula.
    
    Args:
        path (list): Lista de tuplas (x,y) que representan el camino recorrido por el agente
        q_table (numpy.ndarray): Tabla Q con los valores aprendidos por el agente
        grid_size (int, opcional): Tamaño de la cuadrícula. Por defecto es 5
        
    Returns:
        None. Muestra una figura con la visualización del camino
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Dibujar la cuadrícula
    for i in range(grid_size+1):
        ax.axhline(y=i, color='gray', linestyle='-', alpha=0.3)
        ax.axvline(x=i, color='gray', linestyle='-', alpha=0.3)
    
    # Marcar obstáculos
    obstacles = [(0,3), (1,2), (2,1)]
    for obs in obstacles:
        ax.add_patch(plt.Rectangle((obs[1], grid_size-1-obs[0]), 1, 1, 
                                 facecolor='gray', alpha=0.3))
    
    # Marcar inicio y meta
    ax.add_patch(plt.Rectangle((0, grid_size-1), 1, 1, facecolor='green', alpha=0.3))
    ax.add_patch(plt.Rectangle((4, grid_size-3), 1, 1, facecolor='red', alpha=0.3))
    
    # Dibujar el camino con flechas
    for i in range(len(path)-1):
        start = path[i]
        end = path[i+1]
        # Convertir coordenadas para matplotlib
        y_start = grid_size - 1 - start[0]
        x_start = start[1]
        y_end = grid_size - 1 - end[0]
        x_end = end[1]
        
        dx = x_end - x_start
        dy = y_end - y_start
        
        ax.arrow(x_start + 0.5, y_start + 0.5, dx, dy,
                head_width=0.1, head_length=0.1, fc='blue', ec='blue')
    
    ax.set_xticks(range(grid_size+1))
    ax.set_yticks(range(grid_size+1))
    ax.set_title('Camino óptimo del agente')
    plt.grid(True)
    plt.show()