#1. Clase de conductor.
class Conductor:
    def _init_(self, nombre):
        self.nombre = nombre
        self.horarios = []

    def agregar_horario(self, horario):
        if horario in self.horarios:
            return False
        self.horarios.append(horario)
        return True

#2. Clase de bus.
class Bus:
    def _init_(self, numero_bus):
        self.numero_bus = numero_bus
        self.ruta = None
        self.horarios = []
        self.conductores_asignados = []

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def asignar_conductor(self, conductor, horario):
        if horario in self.horarios:
            return False  
        for c in self.conductores_asignados:
            if horario in c.horarios:
                return False  
        self.horarios.append(horario)
        self.conductores_asignados.append(conductor)
        conductor.agregar_horario(horario)
        return True

#3. Clase Administrador.
class Admin:
    def _init_(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, numero_bus):
        bus = Bus(numero_bus)
        self.buses.append(bus)
        return bus

    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        return conductor

    def registrar_horario_bus(self, numero_bus, horario):
        for bus in self.buses:
            if bus.numero_bus == numero_bus:
                if horario not in bus.horarios:
                    bus.horarios.append(horario)
                    return True
        return False

    def asignar_conductor_a_bus(self, numero_bus, nombre_conductor, horario):
        conductor = next((c for c in self.conductores if c.nombre == nombre_conductor), None)
        bus = next((b for b in self.buses if b.numero_bus == numero_bus), None)
        if not conductor or not bus:
            return False
        return bus.asignar_conductor(conductor, horario)

    def mostrar_buses(self):
        for bus in self.buses:
            print(f"Bus {bus.numero_bus}, Ruta: {bus.ruta}, Horarios: {bus.horarios}, Conductores: {[c.nombre for c in bus.conductores_asignados]}")

    def mostrar_conductores(self):
        for conductor in self.conductores:
            print(f"Conductor: {conductor.nombre}, Horarios: {conductor.horarios}")


#4. Ejemplo de uso
admin = Admin()

#5. Buses y Conductores
bus1 = admin.agregar_bus(1)
bus2 = admin.agregar_bus(2)
conductor1 = admin.agregar_conductor("Alejandra")
conductor2 = admin.agregar_conductor("Britney")

#6. Rutas y horarios
bus1.agregar_ruta("Ruta A")
admin.registrar_horario_bus(1, "10:00")
admin.registrar_horario_bus(1, "12:00")

#7. Conductores de los buses
admin.asignar_conductor_a_bus(1, "Alejandra", "10:00")
admin.asignar_conductor_a_bus(1, "Britney", "12:00")

#8. Ejecutando información 
admin.mostrar_buses()
admin.mostrar_conductores()