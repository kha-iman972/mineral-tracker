# 🌿 Mineral Tracker Dashboard

This is a Streamlit app for tracking and visualizing key mineral levels in soil or water. It was built to support sustainable farming, especially for plant and mushroom growth.

## 🚀 Features

- Enter and store mineral levels (Nitrogen, Phosphorus, Potassium, Magnesium, Calcium, Iron)
- View recent data in a clean table
- Automatically generate line charts for each mineral
- Warning zones:
  - 🔴 Too low
  - 🟢 Healthy range
  - 🟠 Too high
- No coding needed — use it right in your browser

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io)
- Python (Pandas, Matplotlib)
- CSV (for data storage)

## 📦 File List

- `app_mineral_dashboard.py` — main app file
- `mineral_data.csv` — stores your input data
- `requirements.txt` — list of needed Python packages

## 📈 How to Run It

If using **Streamlit Cloud**:
1. Upload the files to GitHub
2. Go to https://streamlit.io/cloud
3. Click “New App” and point it to this repository
4. Choose `app_mineral_dashboard.py` as your main file
5. Click **Deploy**

If running locally:

```bash
pip install streamlit pandas matplotlib
streamlit run app_mineral_dashboard.py
```

## 🌱 Why This Matters

This tool helps farmers, students, and sustainability teams monitor nutrient levels, make better decisions, and keep soil health in check — all without needing to write code.

---
Built with ❤️ by Khaya using Quantum AI training from Vivinate Farms.
