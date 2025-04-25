import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Nourhene Rebaï", page_icon="📄", layout="wide")

# En-tête principal
with st.sidebar:
   # st.image("photo.jpg", width=150)  # Optionnel, si tu veux ajouter une photo
    st.title("👩‍💻 Nourhene Rebaï")
    st.markdown("""
    **Ingénieure de données**  
    📍 *Tunis, Tunisie*  
    📧 [rbeii.nourhene@gmail.com](mailto:rbeii.nourhene@gmail.com)  
    📱 +216 29 235 500  
    🌐 [LinkedIn](https://linkedin.com/in/nourhene-rebai-b431931bb/)  
    🗓️ *Née le 6 février 1999*
    """)

   

# Éducation
st.header("🎓 Éducation")
st.markdown("""
- **2020 - 2023** : Diplôme d’ingénieur en informatique, spécialité Ingénierie des systèmes d'information d’aide à la décision – FST, Tunis
- **2018 - 2020** : Cycle préparatoire, spécialité Physique & Chimie – FST, Tunis
- **2018** : Baccalauréat Mathématiques – Lycée Monji Slim, Siliana
""")

# Expériences professionnelles
st.header("💼 Expérience Professionnelle")


st.subheader("TALAN Tunisie Consulting – Ingénieure de données")
st.write("📍 Tunis, Tunisie")
st.write("🗓️ Nov 2024 – Aujourd’hui | Client : BPIFrance")
with st.expander ("Roles et Missions ") : 
    st.markdown("""
- Analyse des besoins métiers et cadrage fonctionnel
- Développement de pipelines avec **AWS Glue**, intégration & transformation des données
- Orchestration via **AWS Airflow**, structuration dans **Dataiku**
- Tests unitaires avec **PyTest**, optimisation des traitements Spark et requêtes SQL
""")

st.write("🗓️ Août 2023 – Nov 2024 | Client : GRDF")
with st.expander ("Roles et Missions ") : 
    st.markdown("""
- Conception de pipelines fiables (CUBE & DWH) avec **Informatica** et **PySpark**
- Résolution d’anomalies, consolidation des données métier (énergie, relève, client)
- Livraison en environnements de **recette** et **production**
""")

st.subheader("TALAN Tunisie Consulting – Stagiaire Data Engineer")
st.write("🗓️ Fév – Juin 2023 | Projet temps réel")
with st.expander ("Roles et Missions ") : 
    st.markdown("""
- Architecture **Lambda** sur Azure Databricks & Event Hubs
- Traitement des flux en temps réel avec **PySpark**
- Modèles prédictifs : prix actions, analyse de sentiment, recommandation
- Tests : **Pytest, DocTest, UnitTest**
""")

st.subheader("BRANDEE – Stagiaire Data Engineer")
st.write("🗓️ Juin – Août 2022 | Projet e-commerce Amazon")
with st.expander ("Roles et Missions ") : 
    st.markdown("""
- Traitement Big Data avec **Apache Spark** sur Data Lake
- NLP, classification (ENN), pondération de termes
- Optimisation des jobs Spark & requêtes SQL
""")

st.subheader("FST Tunis – Projet de Fin d'Études")
st.write("🗓️ Mars – Mai 2022 | Data Engineering & BI")
with st.expander ("Roles et Missions ") : 
    st.markdown("""
- Système de recommandation pour questions de test selon niveau
- Intégration de données avec **Talend**
- Mise en place d’un **Data Lake** et prédiction de niveau candidat
""")

st.subheader("INNOVUP – Stagiaire Développeur Mobile")
st.write("🗓️ Juin – Août 2021 | Calendrier interactif")
with st.expander ("Roles et Missions ") : 
    st.markdown("""
- Création d’événements, gestion de notifications
- Vue intuitive du calendrier pour utilisateurs
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

