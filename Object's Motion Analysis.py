def calculate_motion(initial_params):
    # Creamos un diccionario donde guardamos las variables posicion inicial, velociddad inicial, aceleración y el tiempo.
    x0 = initial_params['initial_position']
    v0 = initial_params['initial_velocity']
    a = initial_params['acceleration']
    t = initial_params['time']
    # Calculamos con la fórmula la posición final 
    x = x0 + (v0 * t) + (0.5 * a * t**2)
    # Valculamos la velocidad
    v = v0 + (a * t)
    # Calculamos la aceleración
    a_final = a
    # Pintamos los resultados
    print(f"Final Position: {x}")
    print(f"Velocity: {v}")
    print(f"Acceleration: {a_final}")
# Ponemmos input para que sea el usuario el que de los parametros iniciales
initial_params = {
    'initial_position': float(input("Enter the initial position (x0): ")),
    'initial_velocity': float(input("Enter the initial velocity (v0): ")),
    'acceleration': float(input("Enter the acceleration (a): ")),
    'time': float(input("Enter the time (t): "))
}
# Ponemos el resultado
calculate_motion(initial_params)
 