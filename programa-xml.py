import xml.etree.ElementTree as ET

tree = ET.parse('FullOct2007.xml')
root = tree.getroot()

new_root = ET.Element('data')

# Recorremos todas las etiquetas <document>
for document in root.findall('.//document'):
    # Buscamos la etiqueta <cat> dentro de cada <document>
    cat = document.find('.//cat')
    # Si la categoría es "Business & Finance", agregamos el <document> al nuevo árbol XML
    if cat is not None and (cat.text == 'Formula One' or cat.text == 'Small Business'):
        print("entra")
        new_root.append(document)

# Guardamos el nuevo árbol XML en un archivo
new_tree = ET.ElementTree(new_root)
new_tree.write('categorias.xml', encoding='utf-8')