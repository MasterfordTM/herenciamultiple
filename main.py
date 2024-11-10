from Classpersona import Persona
from departamento import  DEpartamento
from empleado import Empleado
from ClassArea import Area
from ClassDirector import  director
from  ClassGerente import gerente
from  ClassJefedeArea import  jefedeArea

def main():
    persona = Persona()
    persona.set_nombre("cesar")
    persona.set_apellido("reyes")
    persona.set_edad(18)

    departamento = DEpartamento()
    departamento.set_codigo_departamento("v46515")
    departamento.set_sede("principal")
    departamento.set_tipo("operacional")

    empleado = Empleado()
    empleado.set_nombre("cesar")
    empleado.set_apellido("reyes")
    empleado.set_edad(18)
    empleado.set_email("tilino@")
    empleado.set_fecha_contratacion("24/01/2004")
    empleado.set_id_empleado("e25156")

    area = Area()
    area.set_tipo("humanidades")
    area.set_vision("Liderar la innovación en nuevos productos")
    area.set_horario("Lunes a Viernes, 9:00 a.m. - 6:00 p.m.")
    area.set_sede("principal")
    area.set_tipo("empleado")

    direc = director()
    direc.set_nombre("cesar")
    direc.set_apellido("reyes")
    direc.set_edad(18)
    direc.set_sede("principal")
    direc.set_tipo("operacional")
    direc.set_certificado("inge")
    direc.set_habilidades("hablar")
    direc.set_codigo_departamento("v46515")

    Gerente = gerente()
    Gerente.set_nombre("cesar")
    Gerente.set_apellido("reyes")
    Gerente.set_edad(18)
    Gerente.set_sede("principal")
    Gerente.set_tipo("operacional")
    Gerente.set_objetivos_mensuales("sobrevivir")
    Gerente.set_evaluacion_desempeno("informes")

    JEFEDEAREA = jefedeArea()
    JEFEDEAREA.set_nombre("LOLITO")
    JEFEDEAREA.set_sede("principal")
    JEFEDEAREA.set_tipo("de humanidades ")
    JEFEDEAREA.set_area_especifica("recursos humanos")
    JEFEDEAREA.set_normativas("no comer a la hora de comer ")
    JEFEDEAREA.set_codigo_departamento("v46515")







    print("persona")
    print(persona.mostrar_informacion())

    print("departamento")
    print(departamento.mostrar_informacion())

    print("empleado")
    print(empleado.mostrar_informacion())

    print("area")
    print(area.mostrar_informacion())

    print("direc")
    print(direc.mostrar_informacion())

    print("Gerente")
    print(Gerente.mostrar_informacion())

    print("JEFEDEAREA")
    print(JEFEDEAREA.mostrar_informacion())



if __name__ == "__main__":
    main()