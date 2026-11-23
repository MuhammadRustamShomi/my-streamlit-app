# 📊 My Streamlit App — Multi-page Dashboard

A small multi-page Streamlit app (Home, Dashboard, Settings) that runs without any external API.
Built for the AIBYTEC Generative AI course, lesson 4.4 *Customization & Sharing*.

## Project structure
```
my_streamlit_app/
├── streamlit_app.py          # Home page (entry point)
├── pages/
│   ├── 1_Dashboard.py        # KPIs, chart, raw data
│   └── 2_Settings.py         # Name + data size
├── utils/
│   ├── __init__.py
│   └── helpers.py            # Sample data + summary functions
├── .streamlit/
│   ├── config.toml           # Theme (colours, font)
│   └── secrets.toml.example  # Copy to secrets.toml — never commit the real one
├── requirements.txt
└── .gitignore
```

## Run on your computer
Windows (PowerShell) and Mac/Linux:
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
Optional: copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`.
The app also works without it.

## Deploy free on Streamlit Community Cloud
1. Create a **public GitHub repo** and upload all these files (keep the folder structure).
2. Go to https://share.streamlit.io → **Create app** → choose your repo and branch.
3. Main file path: `streamlit_app.py` → **Deploy**.
4. (Optional) **App → Settings → Secrets**, paste:
   ```toml
   [app_settings]
   environment = "cloud"
   admin_passcode = "your-own-passcode"
   ```

Your app gets a link like `https://your-app-name.streamlit.app`.
Free apps go to sleep when nobody uses them; the next visitor clicks **"Wake up"**.

## Customise
- **Colours and font:** edit `.streamlit/config.toml`.
- **Page names and order:** rename the files in `pages/` (the number sets the order).
