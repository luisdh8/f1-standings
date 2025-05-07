import matplotlib.pyplot as plt  # Para graficar los standings
import mplcursors  # For interactive tooltips

# Diccionario de los pilotos de F1 y sus respectivos equipos
pilotos = {
    'PIASTRI': {'nombre': 'Oscar Piastri', 'equipo': 'McLaren'},
    'NORRIS': {'nombre': 'Lando Norris', 'equipo': 'McLaren'},
    'VERSTAPPEN': {'nombre': 'Max Verstappen', 'equipo': 'Red Bull Racing'},
    'RUSSELL': {'nombre': 'George Russell', 'equipo': 'Mercedes'},
    'LECLERC': {'nombre': 'Charles Leclerc', 'equipo': 'Ferrari'},
    'ANTONELLI': {'nombre': 'Andrea Kimi Antonelli', 'equipo': 'Mercedes'},
    'HAMILTON': {'nombre': 'Lewis Hamilton', 'equipo': 'Ferrari'},
    'ALBON': {'nombre': 'Alexander Albon', 'equipo': 'Williams'},
    'OCON': {'nombre': 'Esteban Ocon', 'equipo': 'Alpine'},
    'STROLL': {'nombre': 'Lance Stroll', 'equipo': 'Aston Martin'},
    'TSUNODA': {'nombre': 'Yuki Tsunoda', 'equipo': 'RB'},
    'GASLY': {'nombre': 'Pierre Gasly', 'equipo': 'Alpine'},
    'SAINZ': {'nombre': 'Carlos Sainz', 'equipo': 'Ferrari'},
    'HULKENBERG': {'nombre': 'Nico Hülkenberg', 'equipo': 'Sauber'},
    'BEARMAN': {'nombre': 'Oliver Bearman', 'equipo': 'Haas'},
    'HADJAR': {'nombre': 'Isack Hadjar', 'equipo': 'RB'},
    'ALONSO': {'nombre': 'Fernando Alonso', 'equipo': 'Aston Martin'},
    'LAWSON': {'nombre': 'Liam Lawson', 'equipo': 'Red Bull Racing'},
    'DOOHAN': {'nombre': 'Jack Doohan', 'equipo': 'Alpine'},
    'BORTOLETO': {'nombre': 'Gabriel Bortoleto', 'equipo': 'McLaren'}
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

# Diccionario de los colores de los equipos
colores_equipos = {
    'McLaren': 'orange',      # Naranja
    'Red Bull Racing': 'blue', # Azul
    'Mercedes': '#00D2BE',     # Verde
    'Ferrari': '#D91C2B',      # Rojo
    'Williams': '#00A9E0',     # Azul Claro
    'Alpine': '#00A9E0',       # Rosa
    'Aston Martin': '#1E5323', # Verde Oscuro
    'RB': '#1E41FF',           # Azul
    'Sauber': '#000000',       # Negro
    'Haas': '#000000'          # Negro
}

# Asignar colores de equipo a los pilotos
colores_pilotos = {
    pilotos['PIASTRI']['nombre']: colores_equipos['McLaren'],
    pilotos['NORRIS']['nombre']: colores_equipos['McLaren'],
    pilotos['VERSTAPPEN']['nombre']: colores_equipos['Red Bull Racing'],
    pilotos['RUSSELL']['nombre']: colores_equipos['Mercedes'],
    pilotos['LECLERC']['nombre']: colores_equipos['Ferrari'],
    pilotos['ANTONELLI']['nombre']: colores_equipos['Mercedes'],
    pilotos['HAMILTON']['nombre']: colores_equipos['Ferrari'],
    pilotos['ALBON']['nombre']: colores_equipos['Williams'],
    pilotos['OCON']['nombre']: colores_equipos['Alpine'],
    pilotos['STROLL']['nombre']: colores_equipos['Aston Martin'],
    pilotos['TSUNODA']['nombre']: colores_equipos['RB'],
    pilotos['GASLY']['nombre']: colores_equipos['Alpine'],
    pilotos['SAINZ']['nombre']: colores_equipos['Ferrari'],
    pilotos['HULKENBERG']['nombre']: colores_equipos['Sauber'],
    pilotos['BEARMAN']['nombre']: colores_equipos['Haas'],
    pilotos['HADJAR']['nombre']: colores_equipos['RB'],
    pilotos['ALONSO']['nombre']: colores_equipos['Aston Martin'],
    pilotos['LAWSON']['nombre']: colores_equipos['Red Bull Racing'],
    pilotos['DOOHAN']['nombre']: colores_equipos['Alpine'],
    pilotos['BORTOLETO']['nombre']: colores_equipos['McLaren']
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
    colores_pilotos_list = [colores_pilotos[piloto] for piloto in nombres]

    bars = plt.barh(nombres, puntos, color=colores_pilotos_list)
    plt.xlabel('Puntos')
    plt.title('Driver Standings')
    plt.gca().invert_yaxis()
    plt.tight_layout()

    # Add interactive tooltips
    cursor = mplcursors.cursor(bars, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{sel.target[0]:.0f} puntos"))

# Graficar Constructor Standings
def graficar_constructor_standings():
    ordenados = sorted(puntos_equipos.items(), key=lambda x: x[1], reverse=True)
    equipos = [x[0] for x in ordenados]
    puntos = [x[1] for x in ordenados]
    colores_equipos_list = [colores_equipos[equipo] for equipo in equipos]

    bars = plt.barh(equipos, puntos, color=colores_equipos_list)
    plt.xlabel('Puntos')
    plt.title('Constructor Standings')
    plt.gca().invert_yaxis()
    plt.tight_layout()

    # Add interactive tooltips
    cursor = mplcursors.cursor(bars, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{sel.target[0]:.0f} puntos"))

# Graficar ambas gráficas en la misma ventana
def graficar_standings_combinados():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Ordenar los pilotos por puntos
    pilotos_ordenados = sorted(puntos_pilotos.items(), key=lambda x: x[1], reverse=True)
    nombres_pilotos = [nombre for nombre, _ in pilotos_ordenados]
    puntos_pilotos_ordenados = [p for _, p in pilotos_ordenados]
    colores_pilotos_list = [colores_pilotos[nombre] for nombre in nombres_pilotos]

    # Graficar Driver Standings
    bars1 = ax1.barh(nombres_pilotos, puntos_pilotos_ordenados, color=colores_pilotos_list)
    ax1.set_xlabel('Puntos')
    ax1.set_title('Driver Standings')
    ax1.invert_yaxis()

    # Ordenar los equipos por puntos
    equipos_ordenados = sorted(puntos_equipos.items(), key=lambda x: x[1], reverse=True)
    nombres_equipos = [equipo for equipo, _ in equipos_ordenados]
    puntos_equipos_ordenados = [p for _, p in equipos_ordenados]
    colores_equipos_list = [colores_equipos[equipo] for equipo in nombres_equipos]

    # Graficar Constructor Standings
    bars2 = ax2.barh(nombres_equipos, puntos_equipos_ordenados, color=colores_equipos_list)
    ax2.set_xlabel('Puntos')
    ax2.set_title('Constructor Standings')
    ax2.invert_yaxis()

    plt.tight_layout()

    # Add interactive tooltips
    cursor1 = mplcursors.cursor(bars1, hover=True)
    cursor1.connect("add", lambda sel: sel.annotation.set_text(f"{sel.target[0]:.0f} puntos"))

    cursor2 = mplcursors.cursor(bars2, hover=True)
    cursor2.connect("add", lambda sel: sel.annotation.set_text(f"{sel.target[0]:.0f} puntos"))

    plt.show()

# Simulación de entrada (puedes modificar esta parte)
def handleInput(FinalResult):
    entrada = FinalResult # FinalResult es un vector de 3 arrays donde cada array solo tiene el nombre del piloto. Cada array es una carrera.
    
    for carrera in entrada:
        for posicion, apellido in enumerate(carrera):
            # Asignar puntos a cada piloto según su posición
            asignar_puntos(posicion + 1, apellido)
