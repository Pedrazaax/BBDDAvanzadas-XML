import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def init(self):
        self.data = {}
        self.tag_set = set()
        self.tag_list = []
        self.categorias = []

    def startElement(self, name, attrs):
        if name not in self.tag_set:
            self.tag_set.add(name)
            self.tag_list.append(name)

    def characters(self, content):  #Lee el contenido que hay entre la etiqueta start y end
            self.contenidoEtiqueta = content #Lo uso en endElement

    def endElement(self, name):
         if name == 'cat':
            self.categorias.append(self.contenidoEtiqueta)


# Crear el analizador SAX y el controlador
parser = xml.sax.make_parser()
handler = MyHandler()
parser.setContentHandler(handler)
parser.parse('FullOct2007.xml')


print(handler.categorias)