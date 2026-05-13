csv_clientes = """id_cliente,email,telefono,fecha_nacimiento,nombre_cliente,tipo_cliente
101,carlos@gmail.com,3001112233,2001-05-10,Carlos Perez,Empresarial
102,ana@gmail.com,3004445566,2002-08-15,Ana Torres,Frecuente
103,luis@gmail.com,3007778899,1999-11-20,Luis Ramirez,Premium
104,maria@gmail.com,3011112233,2000-01-10,Maria Gomez,Frecuente
105,sofia@gmail.com,3022223344,1998-03-25,Sofia Lopez,Premium
"""

csv_paquetes = """id_paquete,peso,destino,tipo_paquete,costo_envio,estado
1,0.5,Bogota,Documento,2500,En Bodega
2,5,Medellin,Paqueteria,25000,En Ruta
3,12,Cali,Carga,60000,Entregado
4,3,Barranquilla,Paqueteria,15000,En Ruta
5,20,Pasto,Carga,100000,Retrasado
"""

csv_destinos = """id_destino,ciudad,departamento,zona
1,Bogota,Cundinamarca,Centro
2,Medellin,Antioquia,Noroccidente
3,Cali,Valle,Suroccidente
4,Barranquilla,Atlantico,Caribe
5,Pasto,Nariño,Sur
"""

csv_envios = """id_envio,id_cliente,id_paquete,id_destino,fecha_envio,estado_envio
1,101,1,1,2026-05-01,En Ruta
2,102,2,2,2026-05-02,Entregado
3,103,3,3,2026-05-03,Retrasado
"""