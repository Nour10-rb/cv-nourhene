import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Nourhene Rebaï", page_icon="📄", layout="wide")

# En-tête principal
st.title("👩‍💻 Nourhene Rebaï")
st.subheader("Ingénieure de données")
st.write("📧 rbeii.nourhene@gmail.com | 📱 +216 29 235 500 | [LinkedIn](https://linkedin.com/in/nourhene-rebai-b431931bb/)")
st.write("📍 Tunis, Tunisie | 🗓️ Née le 6 février 1999")

# Éducation
st.header("🎓 Éducation")
st.markdown("""
- **2020 - 2023** : Diplôme d’ingénieur en informatique, spécialité Ingénierie des systèmes d'information d’aide à la décision – FST, Tunis
- **2018 - 2020** : Cycle préparatoire, spécialité Physique & Chimie – FST, Tunis
- **2018** : Baccalauréat Mathématiques – Lycée Monji Slim, Siliana
""")

# Expériences professionnelles
st.header("💼 Expérience Professionnelle")

with st.expander("Depuis Nov 2024 : TALAN @ BPIFrance - Ingénieure de données"):
    st.markdown("""
    - Analyse des besoins métiers
    - Pipelines de données avec AWS Glue
    - Optimisation des jobs Spark/SQL
    - Tests unitaires avec PyTest
    - Orchestration via AWS Airflow
    - Structuration des datasets dans Dataiku
    """)

with st.expander("Août 2023 - Nov 2024 : TALAN @ GRDF - Ingénieure de données"):
    st.markdown("""
    - Pipelines de données CUBE & DataWarehouse
    - PySpark, Informatica
    - Résolution d’anomalies & consolidation métier
    - Livraison en recette & production
    """)

with st.expander("Fév - Juin 2023 : TALAN - Stage Ingénieure de données"):
    st.markdown("""
    - Dashboard de suivi de revenu temps réel
    - Architecture Lambda avec Azure Databricks, Event Hubs
    - Modèles prédictifs & analyse de sentiment
    - Tests : PyTest, DocTest, UnitTest
    """)

with st.expander("Juin - Août 2022 : BRANDEE - Stage Data Engineer"):
    st.markdown("""
    - Traitement big data Amazon avec Apache Spark
    - NLP, sélection de features, classification ENN
    - Optimisation requêtes SQL & gestion de Data Lake
    """)

with st.expander("Mars - Mai 2022 : Projet académique Data Engineering / BI"):
    st.markdown("""
    - Prédiction de niveau candidat
    - Intégration de données avec Talend
    - Système de recommandation intelligent
    """)

with st.expander("Juin - Août 2021 : INNOVUP - Stage Dév. Mobile"):
    st.markdown("""
    - Calendrier d’événements interactif
    - Notifications & gestion intuitive
    """)

# Compétences
st.header("🛠️ Compétences")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Cloud")
    st.write("AWS, Microsoft Azure")
    st.subheader("Langages")
    st.write("Python, PySpark, Java")

with col2:
    st.subheader("BI & Data")
    st.write("Informatica, Power BI, Microstrategy, Dataiku")
    st.subheader("Bases de données")
    st.write("Oracle, MySQL, PostgreSQL, SQL Server")

with col3:
    st.subheader("Tests & DevOps")
    st.write("PyTest, UnitTest, DocTest, Mocking")
    st.subheader("Méthodologies")
    st.write("Scrum, SAFe, CRISP-DM")

# Langues
st.header("🌍 Langues")
st.markdown("""
- **Français** : Courant  
- **Anglais** : Professionnel  
- **Arabe** : Langue maternelle
""")

st.markdown("---")
st.caption("Dernière mise à jour : Avril 2025")

