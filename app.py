import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Ejercicios NumPy y Pandas", layout="wide")
st.markdown(
    """
    <style>
        .main { background-color: #f9fafc; }
        .stTabs [role="tablist"] button {
            font-size: 16px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True
)

st.title("🌟 Proyecto Interactivo con NumPy y Pandas")
st.write("Selecciona un ejercicio en las pestañas inferiores para explorar NumPy y Pandas:")

tabs = st.tabs([
    "Ejercicio 1",
    "Ejercicio 2",
    "Ejercicio 3",
    "Ejercicio 4",
    "Ejercicio 5 (Pandas)",
    "Ejercicio 6 (Matplotlib)"  # 👈 Nueva pestaña
])

with tabs[0]:
    st.header("🧮 Ejercicio 1: Estadísticos básicos del 1 al 100")
    arr = np.arange(1, 101)
    media = np.mean(arr)
    mediana = np.median(arr)
    varianza = np.var(arr)
    percentil_90 = np.percentile(arr, 90)
    st.code(f"{arr}", language="python")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Media", f"{media:.2f}")
    col2.metric("Mediana", f"{mediana:.2f}")
    col3.metric("Varianza", f"{varianza:.2f}")
    col4.metric("Percentil 90", f"{percentil_90:.2f}")

# ================== EJERCICIO 2 ==================
with tabs[1]:
    st.header("🎲 Ejercicio 2: Matriz aleatoria 5x5")
    matriz = np.random.randn(5, 5)
    determinante = np.linalg.det(matriz)
    traza = np.trace(matriz)
    st.dataframe(pd.DataFrame(matriz, columns=[f"C{i+1}" for i in range(5)]))
    col1, col2 = st.columns(2)
    col1.metric("Determinante", f"{determinante:.4f}")
    col2.metric("Traza", f"{traza:.4f}")

# ================== EJERCICIO 3 ==================
with tabs[2]:
    st.header("📈 Ejercicio 3: Distribución de frecuencias")
    enteros = np.random.randint(0, 11, 1000)
    valores, frecuencias = np.unique(enteros, return_counts=True)
    df_frecuencia = pd.DataFrame({"Valor": valores, "Frecuencia": frecuencias})
    st.dataframe(df_frecuencia)
    st.bar_chart(df_frecuencia, x="Valor", y="Frecuencia")

# ================== EJERCICIO 4 ==================
with tabs[3]:
    st.header("📏 Ejercicio 4: Normalización de un vector")
    opcion = st.radio("Selecciona una opción:", ["Usar vector por defecto", "Ingresar manualmente"])
    if opcion == "Usar vector por defecto":
        v = np.array([2, 4, 6, 8, 10])
    else:
        entrada = st.text_input("Ingresa números separados por comas:", "2, 4, 6, 8, 10")
        try:
            v = np.array([float(x.strip()) for x in entrada.split(",")])
        except:
            st.error("⚠️ Ingrese solo números válidos.")
            v = np.array([])
    if len(v) > 0:
        v_normalizado = (v - np.mean(v)) / np.std(v)
        col1, col2 = st.columns(2)
        col1.code(f"{v}", language="python")
        col2.code(f"{np.round(v_normalizado, 3)}", language="python")

    st.divider()
    st.header("Sección adicional: Datos de jóvenes del ciclo")

    materias_posibles = [
        "Aplicaciones seguras", "IA", "Formulación de proyectos",
        "Proyectos tecnológicos", "Aplicación en la nube"
    ]

    nombres_completos = [
        "Mariuxi Andrea Calle Dumaguala", "Maura Mileth Calle Leon",
        "Steven Alexander Carpio Chillogallo", "Erick Fernando Chacon Avila",
        "Edwin Alexander Choez Dominguez", "Adriana Valentina Cornejo Ulloa",
        "David Alfonso Espinoza Chévez", "Anthony Mauricio Fajardo Vasquez",
        "Freddy Ismael Gomez Ordoñez", "Wendy Nicole Llivichuzhca Mayancela",
        "Alexander Ismael Loja Llivichuzhca", "David Alexander Lopez Saltos",
        "Victor Jonnathan Mendez Villa", "John Sebastian Montenegro Calle",
        "Carmen Elizabeth Neira Inga", "Joel Stalyn Pesantez Berrezueta",
        "Gilson Stalyn Tenemea Aguilar", "Kenny Alexander Valdivieso Coronel"
    ]

    nombres, apellidos = [], []
    for n in nombres_completos:
        partes = n.split()
        nombres.append(" ".join(partes[:-2]))
        apellidos.append(" ".join(partes[-2:]))

    datos_iniciales = {
        "nombres": nombres,
        "apellidos": apellidos,
        "edad": np.random.randint(20, 26, size=18),
        "notas": np.random.uniform(6, 10, size=18).round(2),
        "materias": np.random.choice(materias_posibles, size=18)
    }

    df_jovenes = pd.DataFrame(datos_iniciales)
    st.data_editor(df_jovenes, use_container_width=True)

# ================== EJERCICIO 5 (PANDAS) ==================
with tabs[4]:
    st.header("🧩 Ejercicio 5: Análisis de Datos con Pandas")

    st.header("📂 Descargar CSV de ejemplo para Pandas")

    data = {
        "producto": ["A","A","A","B","B","B","C","C","C","D","D","D","E","E","E"],
        "mes": ["Enero","Febrero","Marzo","Enero","Febrero","Marzo","Enero","Febrero","Marzo","Enero","Febrero","Marzo","Enero","Febrero","Marzo"],
        "venta": [200,150,None,300,250,280,100,50,120,400,420,None,350,330,360],
        "cantidad": [10,8,12,15,None,18,5,3,4,20,21,19,16,None,18]
    }

    df_csv = pd.DataFrame(data)
    st.dataframe(df_csv, use_container_width=True)

    csv = df_csv.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar CSV de ejemplo",
        data=csv,
        file_name="ventas_productos.csv",
        mime="text/csv",
    )

    st.markdown("""
    ### 🧩 Ejercicios (Pandas)
    1. Carga un CSV propio (o exporta `df` a CSV y vuelve a leerlo).  
    2. Calcula la **venta total por producto** y ordénala de mayor a menor.  
    3. Identifica valores faltantes y aplica imputación.  
    4. Construye una **tabla dinámica** (*pivot_table*) por mes y producto.  
    5. Realiza un **merge** entre dos DataFrames y valida el resultado.
    """)

    archivo = st.file_uploader("📂 Carga tu archivo CSV", type=["csv"])
    
    if archivo is not None:
        df = pd.read_csv(archivo)
        st.success("✅ Archivo cargado correctamente.")
        st.subheader("Vista previa de las primeras 10 filas:")
        st.dataframe(df.head(10), use_container_width=True)

        # ================== VENTA TOTAL ==================
        if "producto" in df.columns and "venta" in df.columns:
            st.subheader("💰 Venta total por producto:")
            venta_total = df.groupby("producto")["venta"].sum().sort_values(ascending=False)
            st.dataframe(venta_total)
        else:
            st.warning("⚠️ Asegúrate de que existan columnas llamadas 'producto' y 'venta'.")

        # ================== VALORES FALTANTES ==================
        st.subheader("🧩 Valores faltantes e imputación:")
        st.write(df.isnull().sum())

        estrategia = st.selectbox("Selecciona estrategia de imputación:", ["media", "mediana", "moda"])
        df_imputado = df.copy()

        for col in df.select_dtypes(include=["float64", "int64"]).columns:
            if df[col].isnull().any():
                if estrategia == "media":
                    df_imputado[col].fillna(df[col].mean(), inplace=True)
                elif estrategia == "mediana":
                    df_imputado[col].fillna(df[col].median(), inplace=True)
                else:
                    df_imputado[col].fillna(df[col].mode()[0], inplace=True)

        st.success("✅ Imputación realizada con éxito.")
        st.dataframe(df_imputado.head(10))

        if {"mes", "producto", "venta"}.issubset(df_imputado.columns):
            st.subheader("📊 Tabla dinámica (ventas por mes y producto):")
            tabla = pd.pivot_table(df_imputado, values="venta", index="mes", columns="producto", aggfunc="sum", fill_value=0)
            st.dataframe(tabla, use_container_width=True)
            st.bar_chart(tabla)
        else:
            st.info("ℹ️ No se encontraron columnas 'mes', 'producto' y 'venta' para la tabla dinámica.")

        st.subheader("🔗 Merge entre DataFrames")
        st.write("Ejemplo simple de unión entre `productos` y `ventas` (creados automáticamente):")

        productos = pd.DataFrame({
            "producto": ["A", "B", "C"],
            "categoria": ["Electrónica", "Ropa", "Comida"]
        })
        ventas = pd.DataFrame({
            "producto": ["A", "A", "B", "C", "C"],
            "venta": [200, 150, 300, 100, 50]
        })

        merge_df = pd.merge(productos, ventas, on="producto", how="inner")
        st.dataframe(merge_df)

    else:
        st.info("📥 Carga un archivo CSV para comenzar el análisis.")

with tabs[5]:
    st.header("📊 Ejercicio 6: Visualización con Matplotlib")

    import matplotlib.pyplot as plt

    # 🔹 Simulamos un DataFrame con ventas
    np.random.seed(42)
    productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora"]
    categorias = ["Electrónica", "Accesorios", "Oficina"]
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

    data = {
        "producto": np.random.choice(productos, 60),
        "categoria": np.random.choice(categorias, 60),
        "mes": np.random.choice(meses, 60),
        "cantidad": np.random.randint(1, 20, 60),
        "precio_unitario": np.random.uniform(10, 500, 60)
    }

    df = pd.DataFrame(data)
    df["total"] = df["cantidad"] * df["precio_unitario"]

    st.subheader("📋 Datos simulados")
    st.dataframe(df.head(10), use_container_width=True)

    st.markdown("### 1️⃣ Gráfico de líneas — Precio promedio mensual")
    promedio_mensual = df.groupby("mes")["precio_unitario"].mean().reindex(meses)
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(promedio_mensual, marker='o', color='blue')
    ax1.set_title("Evolución del precio promedio mensual")
    ax1.set_xlabel("Mes")
    ax1.set_ylabel("Precio promedio ($)")
    ax1.grid(True)
    st.pyplot(fig1)

    st.markdown("### 2️⃣ Gráfico de barras — Top 5 combinaciones producto–mes con mayor total")
    top5 = df.groupby(["producto", "mes"])["total"].sum().nlargest(5)
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    top5.plot(kind='bar', color='teal', ax=ax2)
    ax2.set_title("Top 5 combinaciones producto–mes con mayor total")
    ax2.set_xlabel("Producto - Mes")
    ax2.set_ylabel("Total ($)")
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

    st.markdown("### 3️⃣ Boxplot — Total por categoría")
    valores = [df[df["categoria"] == c]["total"] for c in df["categoria"].unique()]
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    ax3.boxplot(valores, labels=df["categoria"].unique(), patch_artist=True)
    ax3.set_title("Distribución del total por categoría")
    ax3.set_xlabel("Categoría")
    ax3.set_ylabel("Total ($)")
    ax3.grid(True)
    st.pyplot(fig3)

    st.markdown("### 4️⃣ Histograma — Cantidad (bins=10)")
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    ax4.hist(df["cantidad"], bins=10, color='purple', edgecolor='black')
    ax4.set_title("Distribución de la cantidad")
    ax4.set_xlabel("Cantidad vendida")
    ax4.set_ylabel("Frecuencia")
    ax4.grid(True)
    st.pyplot(fig4)

    st.markdown("""
    #### 📈 Análisis del histograma:
    - Si los valores se concentran a la izquierda ➜ la mayoría de compras tienen pocas unidades.  
    - Si está uniforme ➜ las cantidades varían mucho entre transacciones.  
    - Si tiene varios picos ➜ existen distintos patrones de compra según el producto.
    """)
