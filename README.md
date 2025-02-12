## 📊 **Sales Data Analysis using SQL, FastAPI, and Streamlit**  
![GitHub repo size](https://img.shields.io/github/repo-size/your-username/sales-data-analysis?color=blue&logo=github)  
![GitHub stars](https://img.shields.io/github/stars/your-username/sales-data-analysis?style=social)  
![GitHub forks](https://img.shields.io/github/forks/your-username/sales-data-analysis?style=social)  

A **real-time sales analytics dashboard** using **SQL for data querying, FastAPI for API services, and Streamlit for visualization**.  

🚀 **Tech Stack:**  
- 👣 **SQL** (PostgreSQL/MySQL) – Data storage & querying  
- ⚡ **FastAPI** – Backend API for fetching sales insights  
- 📊 **Streamlit** – Interactive dashboard for real-time visualization  

---

## 📂 **Project Structure**
```
📦 sales-data-analysis
│── 📋 README.md         # Project documentation  
│── 📂 requirements.txt  # Required Python packages  
│── 📂 streamlit_app.py  # Streamlit dashboard  
│── 📂 api.py            # FastAPI backend  
│── 📂 database.py       # Database connection logic  
│── 📂 data/             # Sales dataset (CSV/SQL)  
```

---

## 🎯 **Features**
✅ **Sales Performance Analysis** – Total revenue, order trends  
✅ **Top-Selling Products** – Identify best-performing products  
✅ **Interactive Dashboard** – Real-time data visualization  
✅ **FastAPI Backend** – Scalable API for data retrieval  

---

## 🛠 **Setup & Installation**
### 🔹 **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/sales-data-analysis.git
cd sales-data-analysis
```

### 🔹 **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 🔹 **3. Set Up Database**
- Load the **sales dataset** into your SQL database (MySQL/PostgreSQL).  
- Update `database.py` with your **DB credentials**.

---

## 🚀 **Running the Project Locally**
### 🖥 **1. Start FastAPI Backend**
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```
📌 **API Endpoints:**  
- `GET /total_revenue` → Returns total revenue  
- `GET /top_products` → Returns top-selling products  

### 📊 **2. Run Streamlit Dashboard**
```bash
streamlit run streamlit_app.py
```
- The dashboard will be available at **http://localhost:8501**  

---

## 🌍 **Deploying the Project**
### 🔹 **1. Deploy FastAPI on Render**
1. Push the project to GitHub.  
2. Go to **[Render.com](https://render.com/)** → **Create a new Web Service**.  
3. Connect GitHub repo → Set **Start Command:**  
   ```bash
   uvicorn api:app --host 0.0.0.0 --port 8000
   ```
4. Click **Deploy**.  
5. Copy the deployed **FastAPI URL**.

### 🔹 **2. Deploy Streamlit on Streamlit Cloud**
1. Go to **[Streamlit Share](https://share.streamlit.io/)**.  
2. Click **New app** → Select your GitHub repo.  
3. Enter:  
   - **Branch:** `main`  
   - **File path:** `streamlit_app.py`  
4. Click **Deploy**.  

🎉 **Your project is now live!**
