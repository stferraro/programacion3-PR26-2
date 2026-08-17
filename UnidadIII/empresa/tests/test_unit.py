import pytest

from src.models import empleado, empleado_contratado, empleado_planta, empresa


@pytest.fixture
def gerente():
    return empleado_planta.EmpleadoPlanta(
        nombre="Carlos",
        apellido="Pérez",
        cedula="V-12345678",
        salario=1200.0,
        antiguedad=10,
        cargo=empleado_planta.EmpleadoPlanta.GERENTE,
    )


@pytest.fixture
def supervisor_1():
    return empleado_planta.EmpleadoPlanta(
        nombre="María",
        apellido="Rodríguez",
        cedula="V-23456789",
        salario=900.0,
        antiguedad=6,
        cargo=empleado_planta.EmpleadoPlanta.SUPERVISOR1,
    )


@pytest.fixture
def supervisor_2():
    return empleado_planta.EmpleadoPlanta(
        nombre="Luis",
        apellido="Torres",
        cedula="V-34567890",
        salario=850.0,
        antiguedad=4,
        cargo=empleado_planta.EmpleadoPlanta.SUPERVISOR2,
    )


@pytest.fixture
def contratado():
    return empleado_contratado.EmpleadoContratado(
        nombre="Sofía",
        apellido="Martínez",
        cedula="V-45678901",
        salario=700.0,
        proyecto_asignado="Migración de sistemas",
        meses_contrato=6,
    )


class TestEmpleado:
    def test_salario_total_es_el_salario_base(self):
        emp = empleado.Empleado(nombre="Ana", apellido="Gómez", cedula="V-11111111", salario=500.0)
        assert emp.salario_total() == 500.0


class TestEmpleadoPlanta:
    def test_gerente_gana_20_por_ciento_extra(self, gerente):
        assert gerente.salario_total() == pytest.approx(1440.00)

    def test_supervisor1_gana_15_por_ciento_extra(self, supervisor_1):
        assert supervisor_1.salario_total() == pytest.approx(1035.00)

    def test_supervisor2_gana_10_por_ciento_extra(self, supervisor_2):
        assert supervisor_2.salario_total() == pytest.approx(935.00)


class TestEmpleadoContratado:
    def test_contratado_gana_10_por_ciento_menos(self, contratado):
        assert contratado.salario_total() == pytest.approx(630.00)


class TestEmpresa:
    def test_calcular_nomina_suma_el_salario_total_de_cada_empleado(
        self, gerente, supervisor_1, supervisor_2, contratado
    ):
        mi_empresa = empresa.Empresa(
            nombre="Tech Solutions C.A.", rif="J-12345678-9", direccion="Av. Principal, Caracas"
        )
        for emp in (gerente, supervisor_1, supervisor_2, contratado):
            mi_empresa.agregar_empleado(emp)

        assert mi_empresa.calcular_nomina() == pytest.approx(4040.00)

    def test_agregar_y_eliminar_empleado(self, gerente):
        mi_empresa = empresa.Empresa(
            nombre="Tech Solutions C.A.", rif="J-12345678-9", direccion="Av. Principal, Caracas"
        )

        mi_empresa.agregar_empleado(gerente)
        assert gerente in mi_empresa._empleados

        mi_empresa.eliminar_empleado(gerente)
        assert gerente not in mi_empresa._empleados

    def test_str_contiene_los_datos_de_cada_empleado(self, gerente, contratado):
        mi_empresa = empresa.Empresa(
            nombre="Tech Solutions C.A.", rif="J-12345678-9", direccion="Av. Principal, Caracas"
        )
        mi_empresa.agregar_empleado(gerente)
        mi_empresa.agregar_empleado(contratado)

        texto = str(mi_empresa)

        assert "Tech Solutions C.A." in texto
        assert "Carlos" in texto
        assert "Sofía" in texto
        assert "Salario Total:  1440.00" in texto
        assert "Salario Total:  630.00" in texto
