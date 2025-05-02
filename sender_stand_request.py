import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH, params={"count": 20})

response = get_docs()
print(response.status_code)
print(response.headers)


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, # Concatenación de URL base y ruta.
                         json=products_ids, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.


response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json()) # Muestra del resultado en la consola


def get_user_token():
    """Obtiene el token de autenticación para las pruebas."""
    user_body = {
        "username": "test_user",
        "password": "secure_password"
    }
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH

    response = requests.post(url, json=user_body)

    if response.status_code == 201:
        return response.json().get("authToken")
    else:
        raise Exception(f"Error al crear el usuario: {response.text}")


def negative_assert_invalid_name_type(kit_body):
    """Verifica que la API rechace un número en el campo 'name'."""
    auth_token = get_user_token()
    response = post_new_kit(kit_body, auth_token)

    # Validar que la respuesta sea 400
    assert response.status_code == 400, f"Código inesperado: {response.status_code}, Respuesta: {response.text}"

    # Validar el mensaje de error
    response_data = response.json()
    expected_message = "El nombre debe ser una cadena de texto."
    assert expected_message in response_data["message"], f"Mensaje inesperado: {response_data['message']}"



















