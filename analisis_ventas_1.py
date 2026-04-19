# Ejercicios Listas, Tuplas y Diccionarios (Core)
# Análisis de datos de ventas

print("=" * 60)
print("ANÁLISIS DE VENTAS - SISTEMA DE REPORTES")
print("=" * 60)

# 1. Carga de Datos
print("\n1. CARGANDO DATOS DE VENTAS...")
print("-" * 40)

ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 800.00},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.00},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45.00},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 800.00},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 8, "precio": 25.00},
    {"fecha": "2024-01-03", "producto": "Monitor", "cantidad": 2, "precio": 300.00},
    {"fecha": "2024-01-04", "producto": "Teclado", "cantidad": 4, "precio": 45.00},
    {"fecha": "2024-01-04", "producto": "Laptop", "cantidad": 1, "precio": 800.00},
    {"fecha": "2024-01-05", "producto": "Monitor", "cantidad": 3, "precio": 300.00},
    {"fecha": "2024-01-05", "producto": "Mouse", "cantidad": 6, "precio": 25.00}
]

print(f"Se cargaron {len(ventas)} ventas registradas")
print("\nLista de ventas original:")
for i, venta in enumerate(ventas, 1):
    print(f"  {i}. {venta}")

# 2. Cálculo de Ingresos Totales
print("\n" + "=" * 60)
print("2. CÁLCULO DE INGRESOS TOTALES")
print("-" * 40)

ingresos_totales = 0
for venta in ventas:
    ingreso_venta = venta["cantidad"] * venta["precio"]
    ingresos_totales += ingreso_venta

print(f"Ingresos totales generados: ${ingresos_totales:,.2f}")

# 3. Análisis del Producto Más Vendido
print("\n" + "=" * 60)
print("3. ANÁLISIS DEL PRODUCTO MÁS VENDIDO")
print("-" * 40)

ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

print("Cantidad vendida por producto:")
for producto, cantidad in ventas_por_producto.items():
    print(f"  - {producto}: {cantidad} unidades")

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

print(f"\n Producto más vendido: {producto_mas_vendido}")
print(f"   Cantidad total vendida: {cantidad_mas_vendida} unidades")

# 4. Promedio de Precio por Producto
print("\n" + "=" * 60)
print("4. PRECIO PROMEDIO POR PRODUCTO")
print("-" * 40)

precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    
    if producto in precios_por_producto:
        suma_precios, total_unidades = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_precios + (precio * cantidad), total_unidades + cantidad)
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)

print("Precio promedio por producto:")
for producto, (suma_precios, total_unidades) in precios_por_producto.items():
    precio_promedio = suma_precios / total_unidades if total_unidades > 0 else 0
    print(f"  - {producto}: ${precio_promedio:.2f} por unidad (basado en {total_unidades} unidades)")

# 5. Ventas por Día
print("\n" + "=" * 60)
print("5. INGRESOS POR DÍA")
print("-" * 40)

ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print("Ingresos totales por día:")
for fecha in sorted(ingresos_por_dia.keys()):
    print(f"  - {fecha}: ${ingresos_por_dia[fecha]:,.2f}")

# 6. Representación de Datos (Resumen por Producto)
print("\n" + "=" * 60)
print("6. RESUMEN DE VENTAS POR PRODUCTO")
print("-" * 40)

resumen_ventas = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ingreso = venta["cantidad"] * venta["precio"]
    
    if producto not in resumen_ventas:
        resumen_ventas[producto] = {
            "cantidad_total": 0,
            "ingresos_totales": 0,
            "precio_promedio": 0.0
        }
    
    resumen_ventas[producto]["cantidad_total"] += cantidad
    resumen_ventas[producto]["ingresos_totales"] += ingreso

# Calcular precio promedio para cada producto
for producto in resumen_ventas:
    if resumen_ventas[producto]["cantidad_total"] > 0:
        resumen_ventas[producto]["precio_promedio"] = (
            resumen_ventas[producto]["ingresos_totales"] / 
            resumen_ventas[producto]["cantidad_total"]
        )

print("Resumen detallado por producto:")
for producto, datos in resumen_ventas.items():
    print(f"\n {producto}:")
    print(f"     - Cantidad total vendida: {datos['cantidad_total']} unidades")
    print(f"     - Ingresos totales: ${datos['ingresos_totales']:,.2f}")
    print(f"     - Precio promedio: ${datos['precio_promedio']:.2f} por unidad")

# 7. Reporte Final
print("\n" + "=" * 60)
print("REPORTE FINAL DE ANÁLISIS DE VENTAS")
print("=" * 60)
print(f"""
RESULTADOS DEL ANÁLISIS:

1. INGRESOS TOTALES: ${ingresos_totales:,.2f}

2. PRODUCTO MÁS VENDIDO: {producto_mas_vendido}
   - Unidades vendidas: {cantidad_mas_vendida}

3. PRECIOS PROMEDIO POR PRODUCTO:
""")

for producto, (suma_precios, total_unidades) in precios_por_producto.items():
    precio_promedio = suma_precios / total_unidades if total_unidades > 0 else 0
    print(f"   - {producto}: ${precio_promedio:.2f}")

print(f"""
4. INGRESOS POR DÍA:
""")
for fecha in sorted(ingresos_por_dia.keys()):
    print(f"   - {fecha}: ${ingresos_por_dia[fecha]:,.2f}")

print(f"""
5. RESUMEN POR PRODUCTO (DICCIONARIO ANIDADO):
""")
for producto, datos in resumen_ventas.items():
    print(f"   '{producto}': {{")
    print(f"       'cantidad_total': {datos['cantidad_total']},")
    print(f"       'ingresos_totales': {datos['ingresos_totales']:.2f},")
    print(f"       'precio_promedio': {datos['precio_promedio']:.2f}")
    print(f"   }},")

print("\n" + "=" * 60)
print("ANÁLISIS COMPLETADO CON ÉXITO")
print("=" * 60)