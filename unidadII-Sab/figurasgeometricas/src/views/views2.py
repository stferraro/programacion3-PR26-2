import customtkinter

from src.models.rectangulo import Rectangulo
from src.models.cuadrado import Cuadrado
from src.models.triangulo import Triangulo

FIGURAS = {
    "Rectangulo": {
        "clase": Rectangulo,
        "campos": ["base", "altura"],
    },
    "Cuadrado": {
        "clase": Cuadrado,
        "campos": ["lado"],
    },
    "Triangulo": {
        "clase": Triangulo,
        "campos": ["lado1", "lado2", "lado3"],
    },
}


class VentanaFigurasGeometricas(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("Figuras Geométricas")
        self.geometry("380x480")
        self.resizable(False, False)

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")

        self.entradas = {}

        self._crear_selector_figura()
        self._crear_frame_campos()
        self._crear_boton_calcular()
        self._crear_label_resultado()

        self._actualizar_campos(self.selector_figura.get())

    def _crear_selector_figura(self):
        self.label_figura = customtkinter.CTkLabel(self, text="Figura geométrica")
        self.label_figura.pack(pady=(20, 5))

        self.selector_figura = customtkinter.CTkOptionMenu(
            self,
            values=list(FIGURAS.keys()),
            command=self._actualizar_campos,
        )
        self.selector_figura.pack(pady=(0, 15))

    def _crear_frame_campos(self):
        self.frame_campos = customtkinter.CTkFrame(self)
        self.frame_campos.pack(pady=10, padx=20, fill="both")

    def _crear_boton_calcular(self):
        self.boton_calcular = customtkinter.CTkButton(
            self, text="Calcular", command=self._calcular
        )
        self.boton_calcular.pack(pady=15)

    def _crear_label_resultado(self):
        self.label_resultado = customtkinter.CTkLabel(
            self, text="", justify="left", wraplength=320
        )
        self.label_resultado.pack(pady=10, padx=20)

    def _actualizar_campos(self, nombre_figura):
        for widget in self.frame_campos.winfo_children():
            widget.destroy()
        self.entradas = {}

        for campo in FIGURAS[nombre_figura]["campos"]:
            fila = customtkinter.CTkFrame(self.frame_campos, fg_color="transparent")
            fila.pack(fill="x", pady=4, padx=10)

            label = customtkinter.CTkLabel(fila, text=campo.capitalize(), width=80, anchor="w")
            label.pack(side="left")

            entrada = customtkinter.CTkEntry(fila)
            entrada.pack(side="left", fill="x", expand=True)

            self.entradas[campo] = entrada

        self.label_resultado.configure(text="")

    def _calcular(self):
        nombre_figura = self.selector_figura.get()
        clase_figura = FIGURAS[nombre_figura]["clase"]
        campos = FIGURAS[nombre_figura]["campos"]

        try:
            valores = [float(self.entradas[campo].get()) for campo in campos]
        except ValueError:
            self.label_resultado.configure(
                text="Todos los campos deben ser números válidos."
            )
            return

        try:
            figura = clase_figura(*valores)
        except ValueError as error:
            self.label_resultado.configure(text=str(error))
            return

        self.label_resultado.configure(text=str(figura))


def iniciar_aplicacion():
    app = VentanaFigurasGeometricas()
    app.mainloop()
