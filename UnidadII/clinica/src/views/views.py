from ..models.doctor import Doctor
from ..models.paciente import Paciente
from ..models.consulta import Consulta

doctor1 = Doctor('Gerardo', 'Ferraro','V-15693290', '0412-0794588', 'correo@gmail.com', 'cardiologo', [])
doctor2 = Doctor('Marco', 'Fittipaldi','V-15693280', '0412-0793388', 'correo2@gmail.com', 'internista', [])

paciente1 = Paciente('Pedro', 'Perez', 'V-1223345', '04123344556','correo3@gmail.com', 41, 'F', [])
paciente2 = Paciente('Pablo', 'Rojas', 'V-12233452', '04123344554','correo4@gmail.com', 47, 'F', [])

consulta1 = Consulta(1, '15/11/2026', '11:15', 'Fiebre', 'denge', 'paracetamol', 2000)

doctor1.add_consulta(consulta1)
paciente1.add_consulta(consulta1)

print(consulta1)
print(doctor1)
print(paciente1)
print(paciente2)
consulta1.print_txt()