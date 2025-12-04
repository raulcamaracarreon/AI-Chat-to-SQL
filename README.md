# 💬 NL-to-SQL Chat (CSV a SQLite)

Esta aplicación web en Flask y Python permite a los usuarios cargar un archivo CSV y luego generar y ejecutar consultas SQL en lenguaje natural (NL) utilizando la API de OpenAI. Los datos se almacenan temporalmente en una base de datos SQLite en memoria.

**Características principales:**
- **Traducción NL &rarr; SQL:** Convierte preguntas humanas a consultas SQL seguras (`SELECT` únicamente).
- **Gestión de la Clave API:** Permite al usuario ingresar su clave de OpenAI directamente en la interfaz (guardada solo en la sesión de Flask).
- **Control de Tema:** Incluye un *switch* funcional para alternar entre los modos Claro y Oscuro.
- **Seguridad:** Usa una capa de `sql_guard` para prevenir consultas que modifiquen o eliminen datos (como `DROP` o `DELETE`).

## 🚀 Instalación y Configuración

Sigue estos pasos para poner en marcha la aplicación en tu entorno local.

### 1. Clonar el Repositorio

```bash
git clone [URL_DE_TU_REPOSITORIO]
cd [nombre-del-repositorio]
2. Crear y Activar el Entorno VirtualEs fundamental aislar las dependencias del proyecto.Bash# Crear el entorno virtual (usar 'python' si 'python3' falla)
python3 -m venv .venv

# Activar el entorno virtual (según tu sistema operativo)
# Linux / macOS:
source .venv/bin/activate
# Windows (Command Prompt):
.venv\Scripts\activate.bat
3. Instalar DependenciasInstala todas las librerías listadas en requirements.txt:Bashpip install -r requirements.txt
4. Configurar Variables de EntornoCrea un archivo llamado .env en la raíz del proyecto para definir las variables sensibles:# .env

# CLAVE SECRETA: Esencial para la seguridad de la sesión de Flask (flash messages y API Key)
FLASK_SECRET_KEY="UNA_CADENA_LARGA_ALEATORIA_Y_UNICA"

# CLAVE API DE OPENAI (Opcional, puede ingresarse por la interfaz)
# Si se provee aquí, la aplicación se iniciará lista para cargar CSV.
# Ejemplo: OPENAI_API_KEY="sk-proj-xxxxxxxx..."
OPENAI_API_KEY="" 
⚙️ Flujo de Trabajo de la AplicaciónLa aplicación sigue un flujo de 5 pasos claros:Configurar Clave API: Ingresa tu clave sk-... o sk-proj-... de OpenAI. Esta se guarda temporalmente en tu sesión. Puedes usar el botón Limpiar Clave para eliminarla de tu sesión de inmediato.Cargar CSV: Sube un archivo CSV desde tu equipo.Esquema de la Tabla: Una vez cargado, el sistema muestra el esquema normalizado (columnas) de la tabla, que se utiliza como contexto para la IA.Pregunta en Lenguaje Natural: Escribe tu consulta (ej: "Suma total de ventas por región"). El sistema genera el SQL.Resultado: El SQL generado se ejecuta de forma segura en la base de datos en memoria y los resultados se muestran en una tabla.🎨 Personalización de la InterfazTema Claro / OscuroLa aplicación incluye un switch de tema en la esquina superior derecha que:Almacena tu preferencia (light o dark) en el localStorage del navegador.Respeta la preferencia de tema de tu sistema operativo como valor predeterminado.🛡️ Notas de SeguridadSolo Lectura: El archivo sql_guard.py y la configuración de db.py fuerzan que solo se permitan consultas SELECT. Palabras clave como DROP, DELETE, UPDATE, INSERT, TRUNCATE, y comandos de administración están estrictamente prohibidos.Clave API: La clave API ingresada por el usuario solo se almacena en la sesión de Flask, no en la base de datos ni en el servidor, y se puede borrar explícitamente con el botón "Limpiar Clave".🛠️ Archivos ClaveArchivoDescripciónapp.pyLógica principal de Flask, manejo de rutas, sesiones, carga de archivos y renderizado de plantillas.nlp2sql.pyClase que maneja la comunicación con la API de OpenAI para la traducción de NL a SQL.db.pyClase para cargar archivos CSV en una base de datos SQLite en memoria (aislada por sesión).sql_guard.pyMódulo que previene y filtra cualquier consulta SQL peligrosa o mutadora.templates/index.htmlInterfaz de usuario, incluyendo el flujo de 5 pasos y la funcionalidad de tema oscuro.requirements.txtLista de dependencias necesarias (Flask, pandas, openai, etc.).
