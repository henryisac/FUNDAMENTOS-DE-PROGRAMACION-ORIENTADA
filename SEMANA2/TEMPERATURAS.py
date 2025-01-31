# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: semanas (4 semanas)
# Segunda dimensión: ciudades (3 ciudades)
# Tercera dimensión: Días de la semana (7 días)
matriz_temp = [
    [   # Ciudad
        [   # Semana
            {"semana 1", "loja", "lunes", 78}, #dia
            {"semana 1", "loja", "martes", 80},
            {"semana 1", "loja", "miercoles", 82},
            {"semana 1", "loja", "jueves", 79},
            {"semana 1", "loja", "viernes", 85},
            {"semana 1", "loja", "sabado", 88},
            {"semana 1", "loja", "domingo", 92}
        ],
        [
            {"semana 2", "loja", "lunes", 76},
            {"semana 2", "loja", "martes", 79},
            {"semana 2", "loja", "miercoles", 83},
            {"semana 2", "loja", "jueves", 81},
            {"semana 2", "loja", "viernes", 87},
            {"semana 2", "loja", "sabado", 89},
            {"semana 2", "loja", "domingo", 93}
        ],
        [
            {"semana 3", "loja", "lunes", 77},
            {"semana 3", "loja", "martes", 81},
            {"semana 3", "loja", "miercoles", 85},
            {"semana 3", "loja", "jueves", 82},
            {"semana 3", "loja", "viernes", 88},
            {"semana 3", "loja", "sabado", 91},
            {"semana 3", "loja", "domingo", 95}
        ],
        [
            {"semana 4", "loja", "lunes", 75},
            {"semana 4", "loja", "martes", 78},
            {"semana 4", "loja", "miercoles", 80},
            {"semana 4", "loja", "jueves", 79},
            {"semana 4", "loja", "viernes", 84},
            {"semana 4", "loja", "sabado", 87},
            {"semana 4", "loja", "domingo", 91}
        ]
    ],
    [
        [
            {"semana 1", "quito", "lunes", 62},
            {"semana 1", "quito", "martes", 64},
            {"semana 1", "quito", "miercoles", 68},
            {"semana 1", "quito", "jueves", 70},
            {"semana 1", "quito", "viernes", 73},
            {"semana 1", "quito", "sabado", 75},
            {"semana 1", "quito", "domingo", 79}
        ],
        [
            {"semana 2", "quito", "lunes", 63},
            {"semana 2", "quito", "martes", 66},
            {"semana 2", "quito", "miercoles", 70},
            {"semana 2", "quito", "jueves", 72},
            {"semana 2", "quito", "viernes", 75},
            {"semana 2", "quito", "sabado", 77},
            {"semana 2", "quito", "domingo", 81}
        ],
        [
            {"semana 3", "quito", "lunes", 61},
            {"semana 3", "quito", "martes", 65},
            {"semana 3", "quito", "miercoles", 68},
            {"semana 3", "quito", "jueves", 70},
            {"semana 3", "quito", "viernes", 72},
            {"semana 3", "quito", "sabado", 76},
            {"semana 3", "quito", "domigno", 80}
        ],
        [
            {"semana 4", "quito", "lunes", 64},
            {"semana 4", "quito", "martes", 67},
            {"semana 4", "quito", "miercoles", 69},
            {"semana 4", "quito", "jueves", 71},
            {"semana 4", "quito", "viernes", 74},
            {"semana 4", "quito", "sabado", 77},
            {"semana 4", "quito", "domigno", 80}
        ]
    ],
    [
        [
            {"semana 1", "cuenca", "lunes", 90},
            {"semana 1", "cuenca", "martes", 92},
            {"semana 1", "cuenca", "miercoles", 94},
            {"semana 1", "cuenca", "jueves", 91},
            {"semana 1", "cuenca", "viernes", 88},
            {"semana 1", "cuenca", "sabado", 85},
            {"semana 1", "cuenca", "domigno", 82}
        ],
        [
            {"semana 2", "cuenca", "lunes", 89},
            {"semana 2", "cuenca", "martes", 91},
            {"semana 2", "cuenca", "miercoles", 93},
            {"semana 2", "cuenca", "jueves", 90},
            {"semana 2", "cuenca", "viernes", 87},
            {"semana 2", "cuenca", "sabado", 84},
            {"semana 2", "cuenca", "domigno", 81}
        ],
        [
            {"semana 3", "cuenca", "lunes", 91},
            {"semana 3", "cuenca", "martes", 93},
            {"semana 3", "cuenca", "miercoles", 95},
            {"semana 3", "cuenca", "jueves", 92},
            {"semana 3", "cuenca", "viernes", 89},
            {"semana 3", "cuenca", "sabado", 86},
            {"semana 3", "cuenca", "domigno", 83}
        ],
        [
            {"semana 4", "cuenca", "lunes", 88},
            {"semana 4", "cuenca", "martes", 90},
            {"semana 4", "cuenca", "miercoles", 92},
            {"semana 4", "cuenca", "jueves", 89},
            {"semana 4", "cuenca", "viernes", 86},
            {"semana 4", "cuenca", "sabado", 83},
            {"semana 4", "cuenca", "domigno", 80}
         ],
    ]
]


for ciudad in range (len(matriz_temp)):#bucles for aninados para recorrer los elmentos
    suma_mes = []
    for semana in range (len(matriz_temp[ciudad])):
        suma = 0
        for dia in range (len(matriz_temp[ciudad][semana])):
            for i in matriz_temp [ciudad][semana][dia]:
                if i in range (0,100):
                    suma += i
                suma_promedio = suma/7
        if "Loja" in matriz_temp[ciudad][semana][dia]:
            suma_mes.append(suma_promedio)
            print(f"el promedio de la semana {semana + 1} es: {suma_promedio: .2f}para la ciudad de", "loja")
            if len(suma_mes) == 4:
                suma_mes_prom = sum (suma_mes)/4
                print (f"el promedio de la temperatura en loja en este mes fue de {suma_mes_prom: 2f}")
        if "quito" in matriz_temp[ciudad][semana][dia]:
            suma_mes.append(suma_promedio)
            print(f"el promedio de la semana {semana + 1} es: {suma_promedio: .2f}para la ciudad de", "quito")
            if len(suma_mes) == 4:
                suma_mes_prom = sum (suma_mes)/4
                print (f"el promedio de la temperatura en quito en este mes fue de {suma_mes_prom: 2f}")
        if "cuenca" in matriz_temp[ciudad][semana][dia]:
            suma_mes.append(suma_promedio)
            print(f"el promedio de la semana {semana + 1} es: {suma_promedio: .2f}para la ciudad de", "cuenca")
            if len(suma_mes) == 4:
                suma_mes_prom = sum (suma_mes)/4
                print (f"el promedio de la temperatura en cuenca en este mes fue de {suma_mes_prom: 2f}")
