# Streamlit Agences Internationales

Application Streamlit pour explorer les données collectées auprès d’agences de l’ONU, IFI et organes étatiques, par thème et région, avec un chatbot intelligent et mise à jour automatique.

## Fonctionnalités

- Interface Streamlit interactive
- Base SQLite locale
- Chatbot Gemini pour requêtes naturelles
- Collecte automatique via script
- Déploiement sur Streamlit Cloud
- Mise à jour hebdomadaire via GitHub Actions

## Installation

```bash
git clone https://github.com/ton_utilisateur/streamlit_agences.git
cd streamlit_agences
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
