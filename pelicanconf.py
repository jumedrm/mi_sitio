AUTHOR = 'Juan Luis Medrano Miguel'
SITENAME = 'Juan Luis Medrano - Web Personal de Taller Transversal 1'
SITEURL = 'https://jumedrm.github.io/mi_sitio'  # Se deja vacío para que funcione en local (localhost:8000)

PATH = "content"

# Configuración regional
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'

# --- Configuración de la Interfaz ---
DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 50

# --- Blogroll (Enlaces de interés y tecnologías de la práctica) ---
LINKS = (
    ('Pelican (Python)', 'https://getpelican.com/'),
    ('Hugo (Go)', 'https://gohugo.io/'),
    ('Jekyll (Ruby)', 'https://jekyllrb.com/'),
    ('Python.org', 'https://www.python.org/'),
)

# --- Redes Sociales ---
SOCIAL = (
    ('GitHub', 'https://github.com/jumedrm'),
    ('LinkedIn', 'https://www.linkedin.com/in/juan-luis-medrano-miguel/'),
    ('Email', 'mailto:medranojuanlu@gmail.com'),
)

# --- Configuración de Feeds (Desactivados para desarrollo) ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Ajustes de Generación ---
# Esto limpia la carpeta 'output' antes de generar la nueva versión,
# evitando que se queden archivos viejos o borrados.
DELETE_OUTPUT_DIRECTORY = True

# --- Rutas de temas y estáticos (Opcional para futuro) ---
# THEME = 'notmyidea' # Este es el tema por defecto

#Para cambiar el color de fondo
STATIC_PATHS = ['extras']
EXTRA_PATH_METADATA = {
    'extras/custom.css': {'path': 'static/custom.css'}
}
CUSTOM_CSS = 'static/custom.css'