import matplotlib.pyplot as plt  # Para graficar los standings
import mplcursors  # For interactive tooltips

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
    pilotos['Piastri']['nombre']: colores_equipos['McLaren'],
    pilotos['Norris']['nombre']: colores_equipos['McLaren'],
    pilotos['Verstappen']['nombre']: colores_equipos['Red Bull Racing'],
    pilotos['Russell']['nombre']: colores_equipos['Mercedes'],
    pilotos['Leclerc']['nombre']: colores_equipos['Ferrari'],
    pilotos['Antonelli']['nombre']: colores_equipos['Mercedes'],
    pilotos['Hamilton']['nombre']: colores_equipos['Ferrari'],
    pilotos['Albon']['nombre']: colores_equipos['Williams'],
    pilotos['Ocon']['nombre']: colores_equipos['Alpine'],
    pilotos['Stroll']['nombre']: colores_equipos['Aston Martin'],
    pilotos['Tsunoda']['nombre']: colores_equipos['RB'],
    pilotos['Gasly']['nombre']: colores_equipos['Alpine'],
    pilotos['Sainz']['nombre']: colores_equipos['Ferrari'],
    pilotos['Hulkenberg']['nombre']: colores_equipos['Sauber'],
    pilotos['Bearman']['nombre']: colores_equipos['Haas'],
    pilotos['Hadjar']['nombre']: colores_equipos['RB'],
    pilotos['Alonso']['nombre']: colores_equipos['Aston Martin'],
    pilotos['Lawson']['nombre']: colores_equipos['Red Bull Racing'],
    pilotos['Doohan']['nombre']: colores_equipos['Alpine'],
    pilotos['Bortoleto']['nombre']: colores_equipos['McLaren']
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
    
    # Graficar Driver Standings
    bars1 = ax1.barh(list(puntos_pilotos.keys()), list(puntos_pilotos.values()), color=[colores_pilotos[p] for p in puntos_pilotos.keys()])
    ax1.set_xlabel('Puntos')
    ax1.set_title('Driver Standings')
    ax1.invert_yaxis()
    
    # Graficar Constructor Standings
    bars2 = ax2.barh(list(puntos_equipos.keys()), list(puntos_equipos.values()), color=[colores_equipos[e] for e in puntos_equipos.keys()])
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
entrada = "1 Piastri 2 Norris 3 Verstappen"
lineas = entrada.split()
for i in range(0, len(lineas), 2):
    posicion = int(lineas[i])
    apellido = lineas[i + 1]
    asignar_puntos(posicion, apellido)

# Mostrar gráficas
graficar_standings_combinados()
