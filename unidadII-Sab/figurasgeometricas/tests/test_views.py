import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from src.views.views import iniciar_aplicacion


def ejecutar_con_entradas(entradas):
    salida = io.StringIO()
    with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
        iniciar_aplicacion()
    return salida.getvalue()


class TestViewsCLI(unittest.TestCase):

    def test_salir_de_inmediato(self):
        salida = ejecutar_con_entradas(["0"])
        self.assertIn("Hasta luego.", salida)

    def test_opcion_invalida(self):
        salida = ejecutar_con_entradas(["9", "0"])
        self.assertIn("Opción inválida.", salida)

    def test_rectangulo_valido(self):
        salida = ejecutar_con_entradas(["1", "4", "5", "0"])
        self.assertIn("Rectángulo: base = 4.00, altura = 5.00, área = 20.00, perímetro = 18.00", salida)

    def test_cuadrado_valido(self):
        salida = ejecutar_con_entradas(["2", "3", "0"])
        self.assertIn("Cuadrado: lado = 3.00, área = 9.00, perímetro = 12.00", salida)

    def test_triangulo_valido(self):
        salida = ejecutar_con_entradas(["3", "3", "4", "5", "0"])
        self.assertIn("área = 6.00, perímetro = 12.00", salida)

    def test_triangulo_invalido_muestra_error(self):
        salida = ejecutar_con_entradas(["3", "1", "1", "10", "0"])
        self.assertIn("Error:", salida)
        self.assertIn("triángulo válido", salida)

    def test_valor_no_numerico_muestra_error(self):
        salida = ejecutar_con_entradas(["1", "abc", "5", "0"])
        self.assertIn("Error:", salida)


if __name__ == "__main__":
    unittest.main()
