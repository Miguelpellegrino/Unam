
# unam_addons

### Descripción
El módulo **unam_addons** ha sido desarrollado para la versión **17 de Odoo** y está diseñado para gestionar las inscripciones de alumnos y las materias de una institución educativa. Este módulo agrega dos nuevos modelos y configura menús y accesos específicos para los usuarios.

### Dependencias
Este módulo depende de los siguientes módulos de Odoo:
- `base`
- `contacts`
- `product`

### Grupos de Usuarios
Para poder visualizar y usar las funcionalidades del módulo, es necesario que el usuario esté asignado a uno de los siguientes grupos:

- **Administrador UNAM**: Con acceso completo (crear, leer, modificar, eliminar) a los registros de inscripciones y materias.
- **Usuario Solo Lectura UNAM**: Con acceso solo de lectura a los registros de inscripciones y materias.

### Modelos

El módulo introduce dos nuevos modelos:

1. **`unam.registrations`**: Este modelo es responsable del manejo de las inscripciones de los alumnos, permitiendo registrar y gestionar las inscripciones en el sistema.
   
2. **`unam.subject`**: Este modelo es usado para la administración de las materias, donde se registran y gestionan las asignaturas disponibles para los estudiantes.

### Menú y Navegación

El módulo incluye un menú básico con las siguientes opciones para facilitar la navegación y operación dentro de Odoo:

#### Operaciones
- **Registro**:
  - **Alumnos**: Enlaza al listado de alumnos registrados (contactos).
  - **Maestros**: Enlaza al listado de maestros registrados (contactos).
  - **Inscripciones**: Permite gestionar las inscripciones de los alumnos (modelo `unam.registrations`).

#### Configuración
- **Materias**: Permite gestionar las materias registradas en el sistema (modelo `unam.subject`).
- **Cursos**: Enlaza a la gestión de productos que representan los cursos ofrecidos (basado en el modelo `product.template` de Odoo).

### Menú Completo en XML

A continuación, el código de configuración del menú que se incluye en el módulo:

```xml
<menuitem name="Operaciones" id="unam_addons_operaciones" sequence="1" parent="unam_addons_menu">
    <menuitem name="Registro" id="unam_addons_operaciones_registro" sequence="2">
        <menuitem id="unam_addons_operaciones_registro_menu" name="Alumnos" sequence="1" action="unam_addons.action_contacts_3" />
        <menuitem id="unam_addons_operaciones_registro_menu_2" name="Maestros" sequence="2" action="unam_addons.action_contacts_2"/>
        <menuitem id="unam_addons_operaciones_registro_menu_3" name="Inscripciones" sequence="3" action="unam_addons.action_unam_registrations"/>
    </menuitem>
</menuitem>

<menuitem name="Configuración" id="unam_addons_configuracion" sequence="2" parent="unam_addons_menu">
    <menuitem id="unam_addons_operaciones_configuracion_menu_1" name="Materias" sequence="1" action="unam_addons.action_unam_subject"/>
    <menuitem id="unam_addons_operaciones_configuracion_menu_2" name="Cursos" sequence="2" action="unam_addons.unam_product_template__action_all"/>
</menuitem>
```

### Instalación

1. Clona o descarga este repositorio en tu instancia de Odoo 17.
2. Asegúrate de tener instaladas las dependencias mencionadas.
3. Instala el módulo desde la interfaz de Odoo a través del menú de **Aplicaciones**.
