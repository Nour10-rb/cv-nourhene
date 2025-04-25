import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Nourhene Rebaï", page_icon="📄", layout="wide")

# En-tete principal
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

st.subheader("Ingénieure de données – TALAN Tunisie Consulting")
st.write("📍 Tunis, Tunisie")
st.write("🗓️ Nov 2024 – Aujourd’hui | Client : BPIFrance")
with st.expander("Roles et Missions") :
    st.markdown("""
    ∠ Analyse et cadrage des besoins métiers en collaboration avec les équipes métiers.  
    ∠ Conception et développement de pipelines de données avec **AWS Glue** pour l’intégration et la transformation des données.  
    ∠ Optimisation des performances des traitements des jobs **Spark** et des requêtes **SQL**.  
    ∠ Implémentation de tests unitaires avec **Pytest** afin de garantir la qualité et la fiabilité des traitements.  
    ∠ Supervision et optimisation des flux de données via **AWS Airflow**.  
    ∠ Mise à disposition et structuration des données dans **Dataiku**, en créant des datasets adaptés aux besoins analytiques.  
    """)

st.write("🗓️ Août 2023 – Nov 2024 | Client : GRDF")
with st.expander("Roles et Missions") :
    st.markdown("""
    ∠ Conception et optimisation de pipelines de données fiables **CUBE** et **DataWarehouse**.  
    ∠ Développement de pipelines d’intégration de données en **PySpark** et **Informatica**.  
    ∠ Optimisation des performances des traitements des jobs **Spark** et des requêtes **SQL**.  
    ∠ Mise en place de tests unitaires avec **PyTest**.  
    ∠ Résolution d’anomalies d’alimentation et consolidation des données métiers (relève, demande, énergie, satisfaction client, etc.).  
    ∠ Participation active à la livraison dans les environnements de **recette** et **production**.  
    """)

st.subheader("Ingénieure de données | Stagiaire – TALAN Tunisie Consulting")
st.write("🗓️ Fév – Juin 2023 | Projet temps réel")
with st.expander("Roles et Missions") :
    st.markdown("""
    ∠ Mise en place d’une architecture Big Data basée sur un modèle **Lambda**, assurant une gestion de données évolutive et un accès en temps réel aux informations de marché.  
    ∠ Développement et traitement des flux de données en temps réel avec **PySpark** sur **Azure Databricks**, en intégrant **Azure Event Hubs** pour l’envoi et la réception des données de marché.  
    ∠ Optimisation des performances des jobs **Spark** et réduction du temps d’exécution.  
    ∠ Mise en place de tests unitaires avec **Pytest**, **DocTest**, et **UnitTest**.  
    ∠ Contribution au développement de modèles prédictifs pour : Prédiction des prix des actions, analyse de sentiment de marché, systèmes de recommandation basés sur les événements en temps réel.  
    """)

st.subheader("Ingénieure de données | Stagiaire – BRANDEE")
st.write("🗓️ Juin – Août 2022 | Projet e-commerce Amazon")
with st.expander("Roles et Missions") :
    st.markdown("""
    ∠ Utilisation d’**Apache Spark** pour le traitement des données à grande échelle consommées à partir d’un **Data Lake**.  
    ∠ Mise en œuvre de nouvelles méthodes de pondération des termes, de sélection des caractéristiques et de classification (**ENN**).  
    ∠ Analyse de sentiment par traitement du langage naturel (**NLP**).  
    ∠ Optimisation des jobs **Spark** et des requêtes **SQL** pour améliorer la performance.  
    ∠ Gestion et optimisation des **Data Lakes** pour un accès rapide et efficace aux données (**partitionnement/indexation**).  
    """)

st.subheader("Projet de Fin d'Études – FST Tunis")
st.write("🗓️ Mars – Mai 2022 | Data Engineering & BI")
with st.expander("Roles et Missions") :
    st.markdown("""
    ∠ Extraction de toutes les données relatives aux sujets (questions, réponses, candidats, niveaux, etc.) à partir de différentes sources.  
    ∠ Développement de pipelines de données pour automatiser le flux de données depuis l’intégration avec **Talend** jusqu’à l’analyse.  
    ∠ Mise en place d’un **Data Lake** pour centraliser et organiser les données extraites.  
    ∠ Développement d’un système de recommandation suggérant des questions aux candidats en fonction de leur niveau de compétence actuel.  
    ∠ La prédiction du niveau des candidats et adaptation des questions en conséquence.  
    """)

st.subheader("Stagiaire Développeur Mobile – INNOVUP")
st.write("🗓️ Juin – Août 2021 | Calendrier interactif")
with st.expander("Roles et Missions") :
    st.markdown("""
    ∠ Permettre aux utilisateurs de créer, éditer et gérer leurs événements, avec la possibilité d'ajouter des détails tels que le titre, la description, la date, l’heure, l’emplacement et toute information supplémentaire pertinente.  
    ∠ Fournir une vue de calendrier intuitive et interactive, permettant aux utilisateurs de consulter rapidement tous leurs événements.  
    ∠ Configurer des notifications de rappel pour les événements à venir, assurant que les utilisateurs ne manquent aucune échéance importante.  
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
