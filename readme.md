Proyecto Final: CatFlix Web Full-Stack
Datos del estudiante

Nombre: Boris Adrián Murillo Yajamín

Carrera: Ingeniería en Desarrollo de Software

// Objetivo

Desarrollar una aplicación web full-stack para manejar catálogos de películas y directores, integrando:

Backend en Django como API REST

Frontend en React

Autenticación mediante OAuth 2.0

El proyecto busca demostrar la integración de tecnologías aprendidas durante el curso y la capacidad de crear una aplicación funcional y segura.

// Modalidad

Trabajo individual o en parejas (2 personas)

Reutilización de proyectos anteriores permitida solo si se adapta a los requisitos y se evidencia aplicación de los contenidos aprendidos.

// Tecnologías utilizadas
Parte	Tecnología
Backend	Django + Django REST Framework
Autenticación	OAuth 2.0 (Django OAuth Toolkit)
Frontend	React + Axios
UI	Bootstrap 5
Base de datos	SQLite (desarrollo) / PostgreSQL (producción)
Control de versiones	Git / GitHub
Deployment	Local / Opcional: Heroku o Render

// Descripción del Proyecto

Aplicación para manejar películas y directores

Relación uno a muchos: un director puede tener varias películas

Funcionalidades principales:

Listado de películas y directores

Crear, editar y eliminar películas y directores

Autenticación y autorización de usuarios mediante OAuth 2.0

// Requisitos del Backend (Django)

API REST:

No se renderizan vistas HTML, solo JSON

Endpoints protegidos con OAuth 2.0

CRUD completo para ambas entidades:

GET → Listar / Detalle

POST → Crear

PUT / PATCH → Actualizar

DELETE → Eliminar

Modelos:

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='directores/', blank=True, null=True)

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='peliculas')
    picture = models.ImageField(upload_to='peliculas/', blank=True, null=True)


Serializers

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'


Vistas API (ViewSets)

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticated]


Rutas (urls.py)

router = DefaultRouter()
router.register(r'directores', DirectorViewSet)
router.register(r'peliculas', PeliculaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]


Protección con OAuth 2.0

Se valida el token en cada request

Endpoints públicos limitados (opcional)

💻 Requisitos del Frontend (React)

Autenticación

Login mediante OAuth 2.0

Almacenar token en localStorage o sessionStorage

Enviar token en cabecera de cada request (Authorization: Bearer <token>)

Consumo de API

Listado de películas y directores

Crear, editar y eliminar registros

Manejo de errores y estado de carga (loading)

Componentes principales

Login.jsx → formulario de login OAuth

PeliculasList.jsx → lista de películas con cards verticales

DirectoresList.jsx → lista de directores

Navbar.jsx → barra de navegación con botones “Todos / Películas / Directores”

Estilos

Fondo oscuro tipo Netflix (#141414)

Cards verticales con imagen arriba, título, descripción y botones

Botones y texto con colores contrastantes (blanco, rojo #e50914)

Responsive usando Bootstrap Grid

⚙️ Instalación y Ejecución
Backend
# Crear entorno virtual
python -m venv .venv
# Activar entorno
# Windows
.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver

Frontend
# Crear proyecto React con Vite (si no existe)
npm create vite@latest catflix-frontend

# Instalar dependencias
npm install axios bootstrap react-router-dom

# Ejecutar
npm run dev
