distancia_percorrida = 300
combustivel_gasto = 25

consumo = distancia_percorrida / combustivel_gasto

print("Dados de consumo:\n")
print(f"Distancia percorrida: {distancia_percorrida} km")
print(f"Combustivel gasto: {combustivel_gasto} litros")
print(f"Consumo medio: {round(consumo, 2)} km/l")