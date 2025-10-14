import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Ejercicios NumPy", layout="wide")
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

st.title("🌟 Proyecto Interactivo con NumPy")
st.write("Selecciona un ejercicio en las pestañas inferiores para ver los resultados:")

tabs = st.tabs([
    "Ejercicio 1",
    "Ejercicio 2",
    "Ejercicio 3",
    "Ejercicio 4",
])

with tabs[0]:
    st.header("🧮 Ejercicio 1: Estadísticos básicos del 1 al 100")

    arr = np.arange(1, 101)
    media = np.mean(arr)
    mediana = np.median(arr)
    varianza = np.var(arr)
    percentil_90 = np.percentile(arr, 90)

    st.write("**Array del 1 al 100:**")
    st.code(f"{arr}", language="python")

    st.markdown("### 📊 Resultados:")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Media", f"{media:.2f}")
    col2.metric("Mediana", f"{mediana:.2f}")
    col3.metric("Varianza", f"{varianza:.2f}")
    col4.metric("Percentil 90", f"{percentil_90:.2f}")

    st.success("✅ Cálculos realizados correctamente.")

with tabs[1]:
    st.header("🎲 Ejercicio 2: Matriz aleatoria 5x5")

    matriz = np.random.randn(5, 5)
    determinante = np.linalg.det(matriz)
    traza = np.trace(matriz)

    st.markdown("### 🧮 Matriz generada (Distribución normal estándar N(0,1)):")
    st.dataframe(
        pd.DataFrame(matriz, columns=[f"C{i+1}" for i in range(5)]),
        use_container_width=True
    )

    st.markdown("### 📈 Resultados:")
    col1, col2 = st.columns(2)
    col1.metric("Determinante", f"{determinante:.4f}")
    col2.metric("Traza", f"{traza:.4f}")

    st.info("💡 Cada vez que recargas la página, la matriz cambia aleatoriamente.")

with tabs[2]:
    st.header("📈 Ejercicio 3: Distribución de frecuencias")

    enteros = np.random.randint(0, 11, 1000)
    valores, frecuencias = np.unique(enteros, return_counts=True)

    df_frecuencia = pd.DataFrame({"Valor": valores, "Frecuencia": frecuencias})
    st.markdown("### 📊 Tabla de frecuencias:")
    st.dataframe(df_frecuencia, use_container_width=True)

    st.markdown("### 📉 Gráfico de barras:")
    st.bar_chart(data=df_frecuencia, x="Valor", y="Frecuencia", use_container_width=True)

    st.success("✅ Distribución generada correctamente (1000 valores entre 0 y 10).")

with tabs[3]:
    st.header("📏 Ejercicio 4: Normalización de un vector")

    st.write("Puedes usar el vector por defecto o ingresar uno nuevo:")

    opcion = st.radio("Selecciona una opción:", ["Usar vector por defecto", "Ingresar manualmente"])

    if opcion == "Usar vector por defecto":
        v = np.array([2, 4, 6, 8, 10])
    else:
        entrada = st.text_input("Ingresa números separados por comas:", "2, 4, 6, 8, 10")
        try:
            v = np.array([float(x.strip()) for x in entrada.split(",")])
        except:
            st.error("⚠️ Ingrese solo números válidos separados por comas.")
            v = np.array([])

    if len(v) > 0:
        v_normalizado = (v - np.mean(v)) / np.std(v)
        st.markdown("### 📋 Resultados:")
        col1, col2 = st.columns(2)
        col1.write("**Vector original:**")
        col1.code(f"{v}", language="python")
        col2.write("**Vector normalizado:**")
        col2.code(f"{np.round(v_normalizado, 3)}", language="python")

    st.divider()
st.header("👩‍🎓👨‍🎓 Sección adicional: Datos de jóvenes del ciclo")

materias_posibles = [
    "Aplicaciones seguras",
    "IA",
    "Formulación de proyectos",
    "Proyectos tecnológicos",
    "Aplicación en la nube"
]

datos_iniciales = {
    "nombres": [f"Nombre{i+1}" for i in range(18)],
    "apellidos": [f"Apellido{i+1}" for i in range(18)],
    "edad": np.random.randint(18, 25, size=18),
    "notas": np.random.uniform(6, 10, size=18).round(2),
    "materias": np.random.choice(materias_posibles, size=18)
}

df_jovenes = pd.DataFrame(datos_iniciales)

st.markdown("### ✏️ Edita los datos libremente:")
df_editado = st.data_editor(df_jovenes, use_container_width=True, num_rows="fixed")

st.markdown("### 📋 Vista previa de los datos editados:")
st.dataframe(df_editado, use_container_width=True)

csv = df_editado.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Descargar CSV",
    data=csv,
    file_name="datos_jovenes.csv",
    mime="text/csv",
)





