from datos import csv_clientes, csv_paquetes, csv_destinos, csv_envios

from clientes import ClienteManager, ClienteDataCleaner, ClienteInteractivo
from productos import PaqueteManager, PaqueteDataCleaner, PaqueteInteractivo
from proveedores import DestinoManager, DestinoDataCleaner, DestinoInteractivo
from ventas import EnvioManager, EnvioInteractivo