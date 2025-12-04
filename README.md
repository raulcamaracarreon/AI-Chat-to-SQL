# 🤖 AI-Chat-to-SQL (Soporte Híbrido: OpenAI / Ollama Local)

Esta aplicación es una herramienta inteligente de análisis de datos que permite interactuar con archivos CSV utilizando lenguaje natural.

A diferencia de otras soluciones, **AI-Chat-to-SQL** está diseñada con una arquitectura flexible que permite alternar entre la **API de OpenAI** (para máxima potencia) y modelos **Locales con Ollama** (para privacidad total y costo cero), simplemente ajustando las variables de entorno.

## 🌟 Características Técnicas

* **Arquitectura LLM Agnóstica:** Utiliza el cliente estándar de OpenAI pero permite reescribir la `BASE_URL`. Esto habilita compatibilidad nativa con **Ollama**, **LocalAI**, o **LM Studio**.
* **Privacidad de Datos (Modo Local):** Al usar Ollama, tus datos y preguntas nunca salen de tu red local.
* **SQL Guard (Seguridad Activa):** Implementa un analizador sintáctico en `sql_guard.py` que bloquea la ejecución de cualquier sentencia que no sea `SELECT`. Previene inyecciones SQL destructivas (`DROP`, `DELETE`, `UPDATE`).
* **Base de Datos Efímera:** Los CSV se cargan en una instancia de SQLite `:memory:`. Los datos existen solo durante la sesión del usuario.
* **Interfaz Reactiva:** Frontend limpio con soporte para modo oscuro/claro y feedback visual de las consultas generadas.

## 🛠️ Requisitos Previos

* **Python 3.8+**
* **Dependencias:** Listadas en `requirements.txt`.
* **(Opcional) Ollama:** Si planeas usar la IA localmente, necesitas tener [Ollama](https://ollama.com/) instalado y ejecutándose.

## ⚙️ Instalación y Configuración

### 1. Clonar y preparar entorno

```bash
git clone [https://github.com/raulcamaracarreon/AI-Chat-to-SQL.git](https://github.com/raulcamaracarreon/AI-Chat-to-SQL.git)
cd AI-Chat-to-SQL

# Crear entorno virtual
python -m venv .venv

# Activar (Windows)
.venv\Scripts\activate

# Activar (Linux/Mac)
source .venv/bin/activate

# Instalar librerías
pip install -r requirements.txt
2. Configuración del LLM (El paso crucial)El comportamiento de la IA se define en el archivo .env. Puedes configurar la app para usar OpenAI (Nube) o Ollama (Local).Crea un archivo .env en la raíz del proyecto:Opción A: Usar IA Local (Ollama) - 🔒 Privacidad MáximaAsegúrate de tener un modelo descargado (ej. ollama pull llama3).Ini, TOML# .env para OLLAMA
FLASK_SECRET_KEY="tu_clave_secreta_random"

# Apunta al servidor local de Ollama
OPENAI_BASE_URL="http://localhost:11434/v1"

# La API Key es irrelevante en local, pero necesaria por la librería.
OPENAI_API_KEY="ollama"

# Define el modelo que tienes instalado en Ollama (ej. llama3, mistral, qwen2.5-coder)
LLM_MODEL_NAME="llama3"
Opción B: Usar OpenAI (GPT-4/3.5) - ⚡ Mayor PotenciaIni, TOML# .env para OPENAI
FLASK_SECRET_KEY="tu_clave_secreta_random"

# URL por defecto de OpenAI
OPENAI_BASE_URL="[https://api.openai.com/v1](https://api.openai.com/v1)"

# Tu API Key real de OpenAI
OPENAI_API_KEY="sk-proj-xxxxxxxxxxxxxxxx"

# Modelo de OpenAI
LLM_MODEL_NAME="gpt-3.5-turbo"
🚀 UsoEjecuta la aplicación:Bashpython app.py
Abre el navegador: Ve a http://127.0.0.1:5000.

Sube tu CSV: La app detectará automáticamente las columnas.

Pregunta: Escribe consultas como:"¿Cuál es el promedio de edad por departamento?""Muestra los 5 productos más vendidos ordenados descendentemente"

📂 Estructura del CódigoPara entender cómo funciona la integración local, revisa estos archivos:ArchivoFunción Técnicanlp2sql.pyCore de IA. Inicializa el cliente openai.OpenAI() usando las variables de entorno. Si detecta una URL local, dirige las peticiones a tu máquina en lugar de los servidores de OpenAI.sql_guard.pyFirewall SQL. Analiza la cadena de texto SQL generada por la IA antes de enviarla a la BD. Si detecta palabras clave prohibidas (DROP, INSERT, EXEC), lanza una excepción de seguridad.db.pyGestor de Datos. Maneja la conexión a SQLite usando pd.to_sql con index=False para una carga limpia del CSV en memoria.prompts.pyIngeniería de Prompts. Contiene las instrucciones del sistema (System Prompt) que guían al modelo para actuar como un experto en SQL y adherirse al esquema de la tabla provista.

🤝 ContribucionesLas Pull Requests son bienvenidas. Especialmente interesan mejoras en:Soporte para más formatos de archivo (Excel, JSON).Optimización de prompts para modelos locales más pequeños (ej. Phi-3).Visualización de datos (gráficos) basada en los resultados SQL.

📄 LicenciaDistribuido bajo la licencia MIT.

Desarrollado por Raúl Cámara Carreón
