# Urban Grocers App Proyecto 
Autor Claudia Carrillo Mutis 
Sprint 7 
Cohorte 28 

Este proyecto forma parte del aprendizaje en pruebas automatizadas con Python y Pytest. 
Se enfoca en la validación de la API de Urban Grocers App, verificando restricciones de datos y asegurando que las respuestas sean correctas.

Las pruebas incluyen:

-Creación de usuarios con distintos tipos de nombres.
-Validación de parámetros incorrectos (números en lugar de texto, valores vacíos, caracteres especiales).
-Manejo de respuestas HTTP (códigos 201 y 400).
-Integración de solicitudes a la API con requests.

Tecnologias utilizadas 
_ Python 3.13 
- Python para pruebas automatizadas 
- Requests para la integracion de la API 
- JSON para el manejo de respuesta API

Estructira del Proyecto 
Cinfiguration py: Configuracion del servicio y rutas de la API 
Data py : Datos de prueba y encabezados de solicitud
Sender_stand_request.py: Archivo para realizar solicitudes a la API
Create_kit_name_kit_test.py: Archivo con pruebas automatizadas
gitignore: Contiene ciertos archivos y carpetas innecesarios 

Intalaciones y Configuaracion
1 Clonar el repositorio 
git clone https://github.com/tuusuario/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es

2 Crear un entorno virtual 
python -m venv env
source env/bin/activate  # En Windows usa: env\Scripts\activate

3 Intalar las dependencias necesarias 
pip install -r requirements.txt


