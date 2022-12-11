import conexion_tabla

db = conexion_tabla.conexion()

class crud_producto:
    def consultar_productos(self):
        return db.consultar("select * from productos")
        
    def administrar_productos(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql="INSERT INTO productos (codigo, nombre, precio, cantidad) VALUES(%s,%s,%s,%s)"
                val=(contenido["codigo"], contenido["nombre"], contenido["precio"], contenido["cantidad"])
            elif contenido["accion"]=="modificar":
                sql="UPDATE productos SET codigo=%s, nombre=%s, precio=%s, cantidad=%s WHERE idProducto=%s"
                val=(contenido["codigo"], contenido["nombre"], contenido["precio"], contenido["cantidad"], contenido["idProducto"])
            elif contenido["eliminar"]:
                sql="DELETE productos FROM productos WHERE idProducto=%s"
                val=(contenido["idProducto"],)
            return db.ejecutar_consultas(sql, val)
        except Exception as e:
            return str(e)
