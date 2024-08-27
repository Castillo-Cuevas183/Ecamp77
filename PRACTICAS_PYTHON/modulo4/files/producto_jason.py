#Leer archivo jason_py
import json

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
    
#Escribir en el archivo Json
def write_json(filename, jsdata):
    with open(filename, 'w') as file:
        data = json.dump(jsdata, file, indent=4)
        
#Agregar producto
def add_product(data, product):
    data["products"].append(product)
    return data

#Actualizar producto
def update_product(products, product_id, new_quantity):
    for product in data["products"]:
        if product['id'] == product_id:
            product['quantity'] = new_quantity
            break

# Eliminar un producto

def remove_product(data, product_id):
    data["products"] = [product for product in data["products"] if product['id']!=product_id]
    return data

#Mostrar productos
def show_products(data):
    for product in data["products"]:
        print(f"ID: {product['id']}, Precio: ${product['price']}, Nombre: {product.get('name', "N/A")},Cantidad: {product.get('quantity', "N/A")}")
        

#Main
filename = "/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/json/products.json"
data = read_json(filename)
show_products(data)
update_product(data,2,30)
show_products(data)

remove_product(data,3)
show_products(data)
write_json(filename,data)

new_product = {"id":4, "name": "Taza", "price":5.5, "quantity":5}
add_product = product.objects.create
write_jason(filename, data)
