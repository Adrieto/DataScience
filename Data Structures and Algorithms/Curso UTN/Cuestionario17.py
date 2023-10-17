# import pickle
# import os.path
# import io
#
# m = open("Notas Alumnos.txt", "r+b")
# tamaño = os.path.getsize("Notas Alumnos.txt")
# m.seek(tamaño+20000, io.SEEK_SET)
#
# #m.readline()
# #m.write("Tu vieja")


import pickle
import os.path
import io

a = 25
b = 2.876
c = 'Hola mundo'

m = open('prueba.dat', 'wb')
pickle.dump(a, m)  # suponer que aquí se grabaron 5 bytes...
pickle.dump(b, m)  # suponer que aquí se grabaron 12 bytes...
pickle.dump(c, m)  # suponer que aquí se grabaron 20 bytes..
print(m.seek(0, io.SEEK_CUR))
m.close()

