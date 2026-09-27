from ..models import ServicioConsulta, ServicioHospedaje, ClinicaVeterinaria

def main():
    clinica = ClinicaVeterinaria("CLINICA VETERINARIA", "12345678", [])
    servicio_consulta1 = ServicioConsulta("1", "2026-06-01", "Simba", "Gerardo Ferraro", 100.0, "Julio Cesar", "dermatología")
    servicio_consulta2 = ServicioConsulta("2", "2022-01-01", "Firulays", "Charly Sheen", 50.0, "Julio Cesar", "cirugia")
    servicio_hospedaje1 = ServicioHospedaje("3", "2026-06-01", "Firulays", "Charly Sheen", 140, "premium", 3)
    servicio_hospedaje2 = ServicioHospedaje("4", "2022-01-01", "Simba", "Gerardo Ferraro", 100, "normal", 1)

    clinica.add_servicio(servicio_consulta1)
    clinica.add_servicio(servicio_consulta2)
    clinica.add_servicio(servicio_hospedaje1)
    clinica.add_servicio(servicio_hospedaje2)

    print(clinica)