# ✅ TaskFlow • To-Do List Django

Aplicación web moderna y profesional de lista de tareas desarrollada con **Django** y **Vanilla CSS**, diseñada con estética SaaS, métricas en tiempo real, búsqueda y filtrado dinámico.

---

## ✨ Características Principales

- **📝 Crear tareas**: Formulario rápido e integrado con validación visual en tiempo real.
- **📊 Dashboard de métricas**: Contadores interactivos para *Total*, *Pendientes*, *En Progreso* y *Completadas*.
- **🔍 Búsqueda y filtrado instantáneo**: Buscador en vivo por texto y pestañas por estado sin recargar la página.
- **👀 Vista de detalle ejecutiva**: Visualización completa con fecha local formateada, badge de estado y navegación.
- **🔄 Edición de tareas**: Actualización sencilla del título, descripción y estado.
- **🗑️ Eliminación segura**: Modal de confirmación con alerta destructiva para prevenir borrados accidentales.
- **🛡️ Panel de Administración**: Modelo `Task` registrado en Django Admin (`/admin/`) con columnas, filtros y búsqueda.
- **🧪 Pruebas unitarias**: Suite de tests automatizados incluida para validar la integridad del modelo y las vistas.

---

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.10+ / Django 5+ & 6+
- **Frontend**: HTML5 Semántico, Vanilla CSS Moderno, JavaScript Nativo (sin dependencias pesadas).
- **Tipografía**: Google Fonts (*Plus Jakarta Sans* & *Inter*).
- **Base de Datos**: 
  - **SQLite** (por defecto para desarrollo local sin requerir configuración adicional).
  - **Oracle Database** (compatible mediante `oracledb` a través de variables en `.env`).
- **Servicio de Estáticos**: WhiteNoise.
- **Variables de Entorno**: `python-dotenv`.

---

## 🚀 Guía de Inicialización Rápida

Sigue estos sencillos pasos para clonar, configurar e iniciar el proyecto en tu entorno local.

### 1. Prerrequisitos
- Tener instalado **Python 3.10** o superior: [python.org](https://www.python.org/downloads/)
- Tener instalado **Git**: [git-scm.com](https://git-scm.com/)

---

### 2. Clonar el repositorio
Abre tu terminal y clona el proyecto en tu máquina:
```bash
git clone https://github.com/vTriiXxy/Todolist.git
cd Todolist
```

---

### 3. Crear y activar el entorno virtual

#### En Windows:
```powershell
python -m venv venv
venv\Scripts\activate
```

#### En macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Instalar dependencias
Con el entorno virtual activado, instala los paquetes requeridos:
```bash
pip install -r requirements.txt
```

---

### 5. Configurar Variables de Entorno (Opcional)

> [!TIP]
> **Inicio rápido sin configuración:** El proyecto está programado con un *fallback* inteligente a **SQLite**. Si no creas un archivo `.env`, funcionará de inmediato con una base de datos local `db.sqlite3` sin configuraciones extra.

Si deseas utilizar una base de datos **Oracle** o personalizar la clave secreta y zona horaria, crea un archivo `.env` en la raíz del proyecto (al nivel de `manage.py`):

```env
# Clave secreta de Django
SECRET_KEY='tu-clave-secreta-personalizada'

# Zona horaria (ejemplo: America/Santiago, America/Buenos_Aires, America/Mexico_City)
TIME_ZONE='America/Santiago'

# Configuración de Base de Datos Oracle (opcional)
DB_NAME='nombre-de-tu-bd'
DB_USER='usuario-de-tu-bd'
DB_PASSWORD='password-de-tu-bd'
DB_HOST='host-de-tu-bd'
DB_PORT='1521'
```

---

### 6. Aplicar las migraciones
Crea las tablas necesarias en la base de datos:
```bash
python manage.py migrate
```

---

### 7. (Opcional) Crear un superusuario para el Admin
Si deseas acceder al panel de administración de Django:
```bash
python manage.py createsuperuser
```
*(Sigue las instrucciones en consola para definir usuario y contraseña).*

---

### 8. Iniciar el servidor de desarrollo
Ejecuta el servidor local de Django:
```bash
python manage.py runserver
```

¡Listo! Abre tu navegador en:
- 🌐 **Aplicación Web**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- ⚙️ **Panel de Administración**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

### 9. Ejecutar pruebas unitarias
Para validar que todo funcione correctamente:
```bash
python manage.py test
```

---

## 📂 Estructura del Proyecto

```
Todolist/
├── .gitignore              # Reglas de exclusión de Git (db.sqlite3, .env, staticfiles, etc.)
├── LICENSE                 # Licencia de uso con cláusula de atribución e integridad
├── README.md               # Documentación general y guía de inicialización
├── manage.py               # Punto de entrada de comandos de gestión de Django
├── requirements.txt        # Lista de dependencias del proyecto (Django, dotenv, whitenoise, oracledb)
├── nameproject/            # Configuración global del proyecto
│   ├── settings.py         # Ajustes de base de datos, middlewares, zona horaria y estáticos
│   ├── urls.py             # Enrutador principal
│   ├── asgi.py
│   └── wsgi.py
└── tasks/                  # Aplicación de gestión de tareas
    ├── admin.py            # Registro y personalización de TaskAdmin
    ├── apps.py             # Configuración de la app tasks
    ├── forms.py            # Formulario TaskForm con widgets estilizados
    ├── models.py           # Modelo Task (título, descripción, fecha, estado)
    ├── tests.py            # Pruebas unitarias para el modelo y vistas del CRUD
    ├── urls.py             # Rutas internas de la aplicación
    ├── views.py            # Lógica de las vistas (list, detail, update, delete)
    ├── static/
    │   └── tasks/
    │       └── css/
    │           └── modern-styles.css  # Sistema de diseño moderno en Vanilla CSS
    └── templates/
        └── tasks/
            ├── base.html              # Plantilla base con navbar y footer con firma
            ├── task_list.html         # Panel con métricas, filtros y lista
            ├── task_detail.html       # Ficha ejecutiva de detalle
            ├── task_update.html       # Formulario de edición
            └── task_delete.html       # Modal de confirmación de eliminación
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas mediante la apertura de solicitudes de incorporación (*Pull Requests*) y discusión de sugerencias vía *Issues*. Consulta la política en la sección de licencia antes de colaborar.

---

## 📄 Licencia

Este proyecto está protegido bajo su propia licencia de uso con atribución obligatoria. Consulta el archivo [LICENSE](LICENSE) para más detalles.

- **Autor**: Cristopher Macaya ([vTriiXxy](https://github.com/vTriiXxy))
- **Condición indispensable**: Mantener visible la firma y créditos de autoría en la interfaz y en el código fuente ante cualquier uso o derivación.
- **Integridad del repositorio**: No se permiten envíos directos (`git push`) al repositorio principal; las contribuciones deben realizarse mediante `fork` y `Pull Request`.
