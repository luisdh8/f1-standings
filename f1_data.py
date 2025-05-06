import matplotlib.pyplot as plt  # Para graficar los standings

# Diccionario de los pilotos de F1 y sus respectivos equipos
pilotos = {
    'Piastri': {'nombre': 'Oscar Piastri', 'equipo': 'McLaren'},
    'Norris': {'nombre': 'Lando Norris', 'equipo': 'McLaren'},
    'Verstappen': {'nombre': 'Max Verstappen', 'equipo': 'Red Bull Racing'},
    'Russell': {'nombre': 'George Russell', 'equipo': 'Mercedes'},
    'Leclerc': {'nombre': 'Charles Leclerc', 'equipo': 'Ferrari'},
    'Antonelli': {'nombre': 'Andrea Kimi Antonelli', 'equipo': 'Mercedes'},
    'Hamilton': {'nombre': 'Lewis Hamilton', 'equipo': 'Ferrari'},
    'Albon': {'nombre': 'Alexander Albon', 'equipo': 'Williams'},
    'Ocon': {'nombre': 'Esteban Ocon', 'equipo': 'Alpine'},
    'Stroll': {'nombre': 'Lance Stroll', 'equipo': 'Aston Martin'},
    'Tsunoda': {'nombre': 'Yuki Tsunoda', 'equipo': 'RB'},
    'Gasly': {'nombre': 'Pierre Gasly', 'equipo': 'Alpine'},
    'Sainz': {'nombre': 'Carlos Sainz', 'equipo': 'Ferrari'},
    'Hulkenberg': {'nombre': 'Nico Hülkenberg', 'equipo': 'Sauber'},
    'Bearman': {'nombre': 'Oliver Bearman', 'equipo': 'Haas'},
    'Hadjar': {'nombre': 'Isack Hadjar', 'equipo': 'RB'},
    'Alonso': {'nombre': 'Fernando Alonso', 'equipo': 'Aston Martin'},
    'Lawson': {'nombre': 'Liam Lawson', 'equipo': 'Red Bull Racing'},
    'Doohan': {'nombre': 'Jack Doohan', 'equipo': 'Alpine'},
    'Bortoleto': {'nombre': 'Gabriel Bortoleto', 'equipo': 'McLaren'}
}

# Inicializar los puntos
puntos_pilotos = {datos['nombre']: 0 for datos in pilotos.values()}
puntos_equipos = {
    'McLaren': 0,
    'Red Bull Racing': 0,
    'Mercedes': 0,
    'Ferrari': 0,
    'Williams': 0,
    'Alpine': 0,
    'Aston Martin': 0,
    'RB': 0,
    'Sauber': 0,
    'Haas': 0
}

# Sistema de puntos por posición
puntos_por_posicion = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

# Función para asignar puntos
def asignar_puntos(posicion, apellido):
    if posicion <= len(puntos_por_posicion):
        puntos = puntos_por_posicion[posicion - 1]
        nombre_completo = pilotos[apellido]['nombre']
        equipo = pilotos[apellido]['equipo']
        puntos_pilotos[nombre_completo] += puntos
        puntos_equipos[equipo] += puntos

# Graficar Driver Standings
def graficar_driver_standings():
    ordenados = sorted(puntos_pilotos.items(), key=lambda x: x[1], reverse=True)
    nombres = [x[0] for x in ordenados]
    puntos = [x[1] for x in ordenados]

    plt.figure(figsize=(10, 6))
    plt.barh(nombres, puntos, color='skyblue')
    plt.xlabel('Puntos')
    plt.title('Driver Standings')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

# Graficar Constructor Standings
def graficar_constructor_standings():
    ordenados = sorted(puntos_equipos.items(), key=lambda x: x[1], reverse=True)
    equipos = [x[0] for x in ordenados]
    puntos = [x[1] for x in ordenados]

    plt.figure(figsize=(10, 6))
    plt.barh(equipos, puntos, color='lightgreen')
    plt.xlabel('Puntos')
    plt.title('Constructor Standings')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

# Simulación de entrada (puedes modificar esta parte)
entrada = "1 Piastri 2 Norris 3 Verstappen"
lineas = entrada.split()
for i in range(0, len(lineas), 2):
    posicion = int(lineas[i])
    apellido = lineas[i + 1]
    asignar_puntos(posicion, apellido)

# Mostrar gráficas
graficar_driver_standings()
graficar_constructor_standings()