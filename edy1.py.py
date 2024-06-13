import pandas as pd
import streamlit as st

class DatasetManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dataset = None
    
    def read_dataset(self):
        try:
            self.dataset = pd.read_csv(self.file_path)
            return True
        except Exception as e:
            st.error(f"Error al leer el archivo CSV: {e}")
            return False

    def show_dataset(self):
        if self.dataset is not None:
            st.subheader("Las primeras 10 filas del dataset son:")
            st.write(self.dataset.head(10))
        else:
            st.error("Por favor, carga el dataset antes de intentar visualizarlo.")

    def compute_statistics(self):
        if self.dataset is not None:
            st.subheader("Estadísticas del dataset:")
            st.write(self.dataset.describe())
        else:
            st.error("Por favor, carga el dataset antes de calcular las estadísticas.")

def main():
    st.title("Herramienta de Análisis de Datos")

    st.sidebar.header("Subir Dataset")
    uploaded_file = st.sidebar.file_uploader("Subir archivo CSV", type=["csv"])

    if uploaded_file is not None:
        dataset_manager = DatasetManager(uploaded_file)
        if dataset_manager.read_dataset():
            st.success("Dataset cargado exitosamente.")
            dataset_manager.show_dataset()
            dataset_manager.compute_statistics()

if __name__ == "__main__":
    main()
