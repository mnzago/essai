import streamlit as st
import requests
import pandas as pd
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.title("Application de fraude par carte de crédit")
    st.subheader("Auteur: Meri-Nut ZAGO")
    
    #Fonction d'importation des données
    @st.cache(persist=True) #permet de ne pas utiliser trop de mémoire
    # mettre la fonction pour lire le dataset pickle
    
    if st.sidebar.checkbox("Afficher les données brutes", False):
        st.subheader("Jeu de données 'credit card': Echantillon de 100 observations")
        st.write(df_sample)
       
    classifier = st.sidebar.selectbox("Choix du Classifier",
                                      ("Random Forest")
                                     )
    
# Random Forest
    if classifier == "Random Forest":
                
        # Bouton d'execution 
        if st.sidebar.button("Execution", key="classify"):
            st.subheader("Random Forest Results")
            
            response = requests.get(f"/predict/").json()
            
            # Affiche les métriques dans l'application
            st.write("Accuracy:", accuracy)
            st.write("precision:", precision)
            st.write("recall:", recall)
      
        
if __name__ == '__main__':
    main()
    
(f"{API_BASE_URL}/customer/{id_}").json()