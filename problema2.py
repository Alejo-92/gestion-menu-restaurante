# =================================================================
# DATOS DEL ESTUDIANTE
# Nombre: Yesid Alejandro Gomez Gaitan
# Grupo: FUNDAMENTOS DE PROGRAMACIÓN - (213022B_2201) / Foro 213022_799
# Programa: INGENIERIA DE SISTEMAS
# Codigo Fuente: Autoria Propia
# =================================================================
# DESCRIPCIÓN: Gestión de menú con matriz y módulo de promociones.
# =================================================================

# --- R1: CREACIÓN DE LA MATRIZ DEL MENÚ ---
# Estructura: [Nombre del Producto, Categoría, Precio Base]
menu = [
    ["Hamburguesa de la Casa", "Plato Fuerte", 15000],
    ["Papas a la Francesa", "Entrada", 7000],
    ["Limonada de Coco", "Bebida", 9000],
    ["Corte de Res Premium", "Plato Fuerte", 28000],
    ["Volcán de Chocolate", "Postre", 12000],
    ["Chicharrón", "Entrada", 11000]
]

# --- PARAMETROS DE LA PROMOCIÓN (Lógica de negocio) ---
CATEGORIA_OBJETIVO = "Plato Fuerte"
UMBRAL_PRECIO = 12000

# --- R2: MÓDULO (FUNCIÓN) PARA CALCULAR EL PRECIO FINAL ---
def calcular_precio_final(categoria_producto, precio_base):
    # Condición: categoría coincide Y el precio supera el umbral
    if categoria_producto == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        precio_final = precio_base * 0.85 # Aplica el 15% de descuento
    else:
        precio_final = precio_base # Mantiene el precio original
    return precio_final

# --- R3: SALIDA Y RECORRIDO DE LA MATRIZ ---
print("=================================================================")
print("          REPORTE DE MENÚ CON PROMOCIONES APLICADAS              ")
print("=================================================================")
print(f"Promoción válida para: {CATEGORIA_OBJETIVO} mayores a ${UMBRAL_PRECIO}")
print("-----------------------------------------------------------------")

# Recorremos la matriz fila por fila
for producto in menu:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]
    
    # Llamamos a la función para obtener el precio final
    precio_final_calculado = calcular_precio_final(categoria, precio_base)
    
    # Formateamos la salida para el informe
    print(f"Producto: {nombre:<22} | Cat: {categoria:<12} | Base: ${precio_base:<6} | Final: ${precio_final_calculado:.0f}")

print("=================================================================")