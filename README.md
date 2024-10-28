<img src="./Aditionals/LogoFinal.svg" width="150px"/>

# Asambly - Gestión de Asambleas Universitarias

Este proyecto es una API para gestionar asambleas universitarias de manera eficiente, facilitando la creación, modificación, consulta y eliminación de asambleas, participantes y sus votaciones. Es un proyecto CRUD desarrollado utilizando Django y Django REST Framework.

>[!IMPORTANT]
Revista el funcionamiento del proyecto en la siguiente [url](https://github.com/Cristian7B/Asambly/blob/main/Aditionals/FuncionamientoProyecto.pdf). Allí puedes ver todas las funcionalidades en acción.

## Características del Proyecto

- **CRUD completo** para la gestión de asambleas.
- **Registro de participantes** de forma anónima o con datos completos.
- **Registro de decisiones** y votaciones dentro de cada asamblea.
- **Manejo de mociones** y votaciones con estados: Aprobadas, Rechazadas, En Espera.
- **Visualización y búsqueda** de asambleas existentes a través de una interfaz amigable.
- **Actualización de participantes y sus votaciones** con la posibilidad de eliminar o modificar información.

## Tecnologías Utilizadas 

- **Backend**: Django
  - Django REST Framework
  - Serialización y deserialización de datos con serializers.
  - Gestión de relaciones muchos a muchos entre asambleas y participantes.
- **Base de Datos**: PostgreSQL(Desplegada en Supabase)
- **Despliegue**: Northflank, utilizando una imagen de **Docker**.

## Instalación y Configuración ⚙️

1. **Clonar el repositorio**:

```bash
git clone https://github.com/Cristian7B/Asambly.git
cd Asambly
```

2. **Instalar las dependencias:**
>[!TIP]
Crea un entorno virtual para instalar las dependencias, usa el comando **python -m venv venv.**

```bash
pip install -r requirements.txt
```

3. **Entra a la carpeta *Asambly* e inicia el servidor:**

```bash
cd Asambly
python manage.py runserver
```

## Endpoints Disponiblea de Asambly ⚫
- **Crear una asamblea:** Enviar una solicitud **POST** a /api/creat-asamblea/ con los datos de la asamblea, participantes, mociones y votaciones.
  
- **Buscar asambleas:** Enviar una solicitud **GET** a /api/get-asamblea/{id_asamblea}/ para obtener la lista de asambleas existentes. Añade el **ID** de la asamblea al final de la url.
  
- **Modificar una asamblea:** Enviar una solicitud **PUT** a /api/update-asamblea/{id_asamblea}/ con los datos actualizados.
  
- **Eliminar una asamblea:** Enviar una solicitud **DELETE** a /api/delete-asamblea/{id_asamblea}/ para eliminar una asamblea y sus datos relacionados.

> [!NOTE] 
Además de eliminar una asamblea completa, la API permite eliminar de forma individual los participantes y votaciones asociados sin necesidad de borrar la asamblea en su totalidad.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar la aplicación, por favor abre un issue o envía un pull request.


## Contacto

Para cualquier pregunta o sugerencia, puedes abrir un issue en el repositorio o contactarme a través de dev.cristianb@gmail.com.