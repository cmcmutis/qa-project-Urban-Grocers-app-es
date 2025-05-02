import sender_stand_request
import data
import pytest
from sender_stand_request import post_products_kits

# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request.get_users_table()

    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1

# funcion de prueba negativa simbolos
def negative_assert_symbol(first_name):
        # El cuerpo de la solicitud actualizada se guarda en la variable user_body
        user_body = get_user_body(first_name)

        # Comprueba si la variable "response" almacena el resultado de la solicitud.
        response = sender_stand_request.post_new_user(user_body)

        # Comprueba si la respuesta contiene el código 400.
        assert response.status_code == 400

        # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
        assert response.json()["code"] == 400
        # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
        assert response.json()["message"] == "Has introducido un nombre de usuario no válido. " \
                                             "El nombre solo puede contener letras del alfabeto latino,  " \
                                             "la longitud debe ser de 2 a 15 caracteres"

# Función de prueba negativa
# La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"
def negative_assert_no_firstname(user_body):
    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"


    # Prueba 1. Creación de un nuevo usuario o usuaria
def test_create_user_1_letter_in_first_name_get_success_response():
    positive_assert("a")

    # Prueba 2
def test_create_user_511_letter_in_first_name_get_success_response():
    positive_assert({"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"})

# Prueba 3
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_firstname(user_body)

# Prueba 4 no se permite 512 caracteres
def test_create_user_512_letter_in_first_name_get_error_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5 se permiten caracteres especiales
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol({"name": "№%@,"})

# Prueba 6 específica para nombres con espacios no se a podido
def test_kit_name_with_spaces():
    positive_assert(" A Aaa ")


# Prueba 7 se permiten numeros
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(123)

    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 200


# Prueba 8 el parametro no se pasa
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_firstname(user_body)

# Prueba 9 parametro diferente numero
def test_kit_name_invalid_type():
    """Verifica que la API rechace un número en el campo 'name'."""
    kit_body = {"name": 123}  # Valor inválido para el campo 'name'
    response = post_new_kit(kit_body)

    # Validar que la respuesta sea 400
    assert response.status_code == 400, f"Código inesperado: {response.status_code}, Respuesta: {response.text}"

    # Validar el mensaje de error correcto
    response_data = response.json()
    expected_message = "El nombre debe ser una cadena de texto."
    assert expected_message in response_data["message"], f"Mensaje inesperado: {response_data['message']}"
















