from pyeasyga import pyeasyga

#todos los dias de cursadas
data = [

        #tupla para una materia, tiene un identificador 'a'
        [('00000010110', '11011111111', 'a'), #curso lunes de 0 a 5 noche
            ('01000010110', '11011111111', 'a')],  #curso miercoles de 0 a 5 noche
    
        #tupla para una materia, tiene un identificador 'b'
        [('01100010110', '11011111111', 'b'),  #curso jueves de 0 a 5 noche
            ('10100010111', '11011111111', 'b')], #curso sabado de 0 a 5 mañana
        ]

recompensa = 10
castigo = 5



ga = pyeasyga.GeneticAlgorithm(data)

def fitness (individual, data):
    fitness = 0
    #aca iria las comparaciones de cada uno y sumar o restar puntos
    return fitness

ga.fitness_function = fitness

ga.run()

print(ga.best_individual())