import tkinter as tk
from tkinter import messagebox

# ==========================================
# SECCIÓN: Excepciones Personalizadas
# ==========================================

class InvalidFieldException(Exception):
    """Excepción para campos de texto inválidos (con números o muy largos)."""
    def __init__(self, message="Campo inválido"):
        self.message = message
        super().__init__(self.message)

class TeamFullException(Exception):
    """Excepción para cuando el equipo ya tiene sus 3 integrantes."""
    def __init__(self, message="El equipo está lleno"):
        self.message = message
        super().__init__(self.message)

# ==========================================
# SECCIÓN: Lógica de Negocio (Clases)
# ==========================================

class Programador:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class EquipoMaratonProgramacion:
    def __init__(self, nombreEquipo: str, universidad: str, lenguajeProgramacion: str):
        self.nombreEquipo = nombreEquipo
        self.universidad = universidad
        self.lenguajeProgramacion = lenguajeProgramacion
        self.tamañoEquipo_max = 3  # Tamaño fijo según requerimiento
        # El diagrama UML original no muestra esta lista de forma explícita
        # como atributo en el código de EquipoMaratónProgramación, pero
        # la relación de composición la requiere. En Python lo manejamos así.
        self._programadores = []

    def estáLleno(self) -> bool:
        """Determina si el equipo está completo (3 integrantes)."""
        return len(self._programadores) >= self.tamañoEquipo_max

    def validarCampo(self, campo: str) -> bool:
        """
        Valida que un campo reciba solo texto (sin números) y longitud < 20.
        Lanza InvalidFieldException si falla.
        """
        if not campo:
            raise InvalidFieldException("El campo no puede estar vacío.")

        # Requerimiento: no se permiten datos numéricos (solo texto)
        # Una forma rápida es buscar dígitos. isalpha() puede ser muy estricto
        # con espacios o acentos, así que buscamos si contiene un número.
        if any(char.isdigit() for char in campo):
            raise InvalidFieldException(f"El campo '{campo}' no puede contener números.")

        # Requerimiento: longitud inferior a 20 caracteres
        if len(campo) >= 20:
            raise InvalidFieldException(f"El campo '{campo}' es muy largo (20 chars máx).")

        return True

    def añadirProgramador(self, p: Programador):
        """
        Añade un programador si hay espacio y valida sus datos.
        Lanza excepciones específicas.
        """
        if self.estáLleno():
            raise TeamFullException(f"No se puede añadir a {p}. El equipo '{self.nombreEquipo}' ya está lleno (max {self.tamañoEquipo_max}).")

        # Validar nombre y apellidos antes de añadir
        # El UML muestra validarCampo(String), lo aplicamos a cada campo
        self.validarCampo(p.nombre)
        self.validarCampo(p.apellidos)

        self._programadores.append(p)

    def get_lista_programadores(self):
        """Método helper para obtener la lista actual."""
        return self._programadores

    def __str__(self):
        return (f"Equipo: {self.nombreEquipo}\n"
                f"Universidad: {self.universidad}\n"
                f"Lenguaje: {self.lenguajeProgramacion}\n"
                f"Integrantes ({len(self._programadores)}/{self.tamañoEquipo_max}):")

# ==========================================
# SECCIÓN: Interfaz Gráfica (GUI con Tkinter)
# ==========================================

class AppMaraton:
    def __init__(self, root):
        self.root = root
        self.root.title("Inscripción de Equipo de Programación")
        self.root.geometry("600x650")
        self.team = None  # Instancia de EquipoMaratonProgramacion se creará luego

        self.create_widgets()

    def create_widgets(self):
        """Crea todos los componentes visuales."""
        # --- SECCIÓN 1: Creación del Equipo ---
        self.label_team_title = tk.Label(self.root, text="Paso 1: Registrar Datos del Equipo", font=("Arial", 14, "bold"))
        self.label_team_title.pack(pady=(20, 10))

        frame_team = tk.Frame(self.root)
        frame_team.pack(padx=20, pady=10)

        self.create_label_entry(frame_team, "Nombre del Equipo:", 0)
        self.create_label_entry(frame_team, "Universidad:", 1)
        self.create_label_entry(frame_team, "Lenguaje a utilizar:", 2)

        self.btn_create_team = tk.Button(self.root, text="Crear/Actualizar Equipo", command=self.create_team_instance, bg="#e1f5fe")
        self.btn_create_team.pack(pady=10)

        # Separador visual
        self.separator = tk.Frame(self.root, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.pack(fill=tk.X, padx=10, pady=15)

        # --- SECCIÓN 2: Añadir Integrantes (Inhabilitada inicialmente) ---
        self.label_prog_title = tk.Label(self.root, text="Paso 2: Añadir Programadores (Máx 3)", font=("Arial", 14, "bold"), fg="gray")
        self.label_prog_title.pack(pady=(10, 5))

        self.frame_prog = tk.Frame(self.root)
        self.frame_prog.pack(padx=20, pady=10)

        self.create_label_entry_prog(self.frame_prog, "Nombre:", 0)
        self.create_label_entry_prog(self.frame_prog, "Apellidos:", 1)

        self.btn_add_prog = tk.Button(self.root, text="Añadir Integrante", command=self.add_programmer, bg="#e8f5e9", state=tk.DISABLED)
        self.btn_add_prog.pack(pady=10)

        # --- SECCIÓN 3: Visualización del Estado ---
        self.label_list_title = tk.Label(self.root, text="Estado Actual del Equipo", font=("Arial", 12, "bold"))
        self.label_list_title.pack(pady=(20, 5))

        # Texto para info del equipo y lista de integrantes
        self.txt_team_display = tk.Text(self.root, height=12, width=65, wrap=tk.WORD, font=("Courier", 10), bg="#fafafa")
        self.txt_team_display.config(state=tk.DISABLED)  # Solo lectura
        self.txt_team_display.pack(pady=10, padx=20)

    # --- Helpers para crear labels y entries rápidos ---
    def create_label_entry(self, parent, label_text, row):
        label = tk.Label(parent, text=label_text, anchor="w", width=20)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        
        entry_var_name = f"entry_team_{row}"
        setattr(self, entry_var_name, tk.Entry(parent, width=35))
        getattr(self, entry_var_name).grid(row=row, column=1, padx=10, pady=5)

    def create_label_entry_prog(self, parent, label_text, row):
        label = tk.Label(parent, text=label_text, anchor="w", width=20)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        
        entry_var_name = f"entry_prog_{row}"
        setattr(self, entry_var_name, tk.Entry(parent, width=35, state=tk.DISABLED))
        getattr(self, entry_var_name).grid(row=row, column=1, padx=10, pady=5)

    # ==========================================
    # SECCIÓN: Acciones de la Interfaz
    # ==========================================

    def create_team_instance(self):
        """Obtiene los datos del GUI, crea la instancia del equipo y habilita la zona de integrantes."""
        name = self.entry_team_0.get().strip()
        uni = self.entry_team_1.get().strip()
        lang = self.entry_team_2.get().strip()

        # Validación simple para la creación del equipo
        if not name or not uni or not lang:
            messagebox.showwarning("Atención", "Por favor rellene todos los campos para crear el equipo.")
            return

        # Crea o actualiza la instancia de la lógica
        self.team = EquipoMaratonProgramacion(name, uni, lang)
        
        messagebox.showinfo("Éxito", f"¡Equipo '{name}' creado exitosamente!")

        # Habilita la interfaz para añadir programadores
        self.enable_programmer_section()
        self.update_display() # Limpia/actualiza la vista inferior
        self.btn_create_team.config(text="Actualizar Equipo") # Cambia texto para ediciones

    def enable_programmer_section(self):
        """Habilita los widgets de la segunda sección."""
        self.label_prog_title.config(fg="black")
        self.entry_prog_0.config(state=tk.NORMAL)
        self.entry_prog_1.config(state=tk.NORMAL)
        self.btn_add_prog.config(state=tk.NORMAL)

    def add_programmer(self):
        """Lógica principal de captura de excepciones al intentar añadir un integrante."""
        if not self.team:
            messagebox.showerror("Error", "Primero debe crear el equipo.")
            return

        p_name = self.entry_prog_0.get().strip()
        p_surname = self.entry_prog_1.get().strip()

        # Crea la instancia temporal del programador
        temp_prog = Programador(p_name, p_surname)

        try:
            # BLOQUE TRY: Intenta ejecutar la lógica del negocio
            # que lanza excepciones controladas
            self.team.añadirProgramador(temp_prog)
            
            # Si tiene éxito
            messagebox.showinfo("Éxito", f"¡Programador {temp_prog} añadido!")
            
            # Limpia los campos
            self.entry_prog_0.delete(0, tk.END)
            self.entry_prog_1.delete(0, tk.END)
            
            # Actualiza visualización y verifica si se llenó
            self.update_display()
            self.check_if_full()

        except TeamFullException as e:
            # BLOQUE CATCH (except) específico: El equipo ya está lleno
            # Se muestra la "excepción correspondiente" como un mensaje de error claro
            messagebox.showerror("Error de Capacidad", str(e))
            self.btn_add_prog.config(state=tk.DISABLED) # Deshabilita el botón

        except InvalidFieldException as e:
            # BLOQUE CATCH (except) específico: Validación de campos falló (texto < 20)
            # Requisito: validar solo texto y longitud < 20
            messagebox.showerror("Error de Validación de Campos", str(e))
            # No deshabilita nada, permite corregir el texto

        except Exception as e:
            # Catch genérico para errores inesperados
            messagebox.showerror("Error Inesperado", f"Ha ocurrido un error inesperado:\n{e}")

    def check_if_full(self):
        """Comprueba el estado del equipo y deshabilita controles si está lleno."""
        if self.team.estáLleno():
            self.btn_add_prog.config(state=tk.DISABLED)
            # También deshabilitamos las entradas de texto
            self.entry_prog_0.config(state=tk.DISABLED)
            self.entry_prog_1.config(state=tk.DISABLED)

    def update_display(self):
        """Actualiza el cuadro de texto inferior con la información actual."""
        self.txt_team_display.config(state=tk.NORMAL) # Habilita temporalmente
        self.txt_team_display.delete('1.0', tk.END) # Limpia contenido
        
        if self.team:
            # Usamos los métodos mágicos __str__ que definimos arriba
            self.txt_team_display.insert(tk.END, str(self.team) + "\n\n")
            
            programadores = self.team.get_lista_programadores()
            if not programadores:
                self.txt_team_display.insert(tk.END, "  - (No hay integrantes registrados aún)\n")
            else:
                for i, p in enumerate(programadores, 1):
                    # Formato: 1. Nombre Apellidos
                    self.txt_team_display.insert(tk.END, f"  {i}. {p}\n")
        
        self.txt_team_display.config(state=tk.DISABLED) # Solo lectura otra vez

# ==========================================
# SECCIÓN: Punto de Entrada de la App
# ==========================================

if __name__ == "__main__":
    root = tk.Tk()
    app = AppMaraton(root)
    root.mainloop()
