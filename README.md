# 🚚 Meta-Logística S.A.S.
## Proyecto Final - Sistema Ruta-Óptima
---
# 📌 Descripción del Proyecto
Meta-Logística S.A.S. es una empresa enfocada en la optimización de procesos logísticos.
Este proyecto desarrolla un sistema llamado **Ruta-Óptima**, diseñado para registrar, clasificar y gestionar paquetes antes de ser cargados en camiones de distribución.
El sistema integra:
- Programación Orientada a Objetos (POO)
- SQLite
- Pandas
- Tkinter
- Power BI
permitiendo construir un ecosistema completo de backend, frontend y analítica empresarial.
---
# 🎯 Objetivo
El objetivo principal del proyecto es automatizar procesos logísticos mediante un sistema que permita:
- Registrar clientes.
- Registrar paquetes.
- Clasificar paquetes automáticamente según su peso.
- Calcular el costo de envío.
- Registrar destinos.
- Registrar envíos.
- Consultar información almacenada en SQLite.
- Conectar la base de datos a Power BI para generar visualizaciones gerenciales.
---
# 🚀 Reto Seleccionado
## Logística - Ruta-Óptima
Una empresa de envíos en Bogotá necesita clasificar paquetes antes de cargarlos a los camiones.
### Clasificación automática de paquetes
- Documento → peso menor a 1 kg.
- Paquetería → peso menor a 10 kg.
- Carga → peso igual o mayor a 10 kg.
### Cálculo del costo de envío
```python
🏗️ Arquitectura del Proyecto
costo_envio = peso * 5000
Proyecto_final/
│
├── main.py
├── datos.py
├── clientes.py
├── productos.py
├── proveedores.py
├── ventas.py
├── __init__.py
├── meta_logistica.db
│
└── Frontend/
    ├── __init__.py
    ├── app_central.py
    ├── app_clientes.py
    ├── app_productos.py
    ├── app_proveedores.py
    └── app_ventas.py
