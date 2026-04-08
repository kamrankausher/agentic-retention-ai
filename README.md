# 🤖 Agentic Churn Intelligence  
### Customer Retention Intelligence Using Agentic AI  

A **production-grade full-stack Agentic AI application** that predicts customer churn, explains the reasoning using SHAP, and utilizes a multi-agent orchestrated workflow to proactively recommend and simulate business actions.

This project demonstrates real-world ML deployment, LLM orchestration, backend–frontend architecture, and a premium interactive dashboard designed for business intelligence.

---

## 📸 Application Preview

<p align="center">
  <em>(Add screenshots of your UI here)</em><br/><br/>
  <img src="https://via.placeholder.com/850x400/1e1e24/eeeeee?text=Home+Dashboard" width="850" alt="Home Dashboard placeholder"/>
  <br/><br/>
  <img src="https://via.placeholder.com/850x400/1e1e24/eeeeee?text=Agentic+Pipeline" width="850" alt="Agentic Pipeline placeholder"/>
</p>

---

## 🏗️ System Architecture

The system utilizes an event-driven flow managed by `FastAPI` and `LangGraph`.

1️⃣ **Input:** A customer profile is captured by the React UI and sent to the FastAPI backend.  
2️⃣ **Orchestrator:** LangGraph initializes the state and kicks off the sequence.  
3️⃣ **Risk Agent:** Evaluates the probability of churn via our trained XGBoost system.  
4️⃣ **Explainability Agent:** Extracts core drivers using SHAP logic.  
5️⃣ **Strategy Agent:** Formulates a precise intervention policy (Groq).  
6️⃣ **Simulation Agent:** Predicts the new churn probability post-intervention (Groq).  
7️⃣ **Communication Agent:** Drafts a highly tailored retention message (Groq).  
8️⃣ **Output:** The JSON results are rendered iteratively across the React dashboard.  

---

## ✨ Project Highlights

- **Agentic AI Orchestration:** Leverages LangGraph to manage a cyclic workflow of specific AI sub-agents.
- **XGBoost Risk Assessor:** Accurately predicts churn probability based on customer profiles.
- **Explainable AI (SHAP):** Extracts specific friction points for high-risk customers, feeding exact data points to the Strategy Agent rather than using generic assumptions.
- **Groq-Powered Reasoning Engine:** Uses the lightning-fast `llama-3.3-70b-versatile` via Groq API to formulate strategic interventions, simulate probabilistic outcomes, and draft precise customer outreach.
- **FAANG-Tier React UI:** A stunning, ultra-premium React dashboard using `Vite` and `Framer Motion` for staggered data revelation, animated pipelines, and beautiful CSS aesthetics.

---

## 🧠 Problem Statement

Most customer retention systems provide a static churn probability, leaving business teams without actionable context or follow-up strategy. 

Real-world business systems require:
- Accurate predictive analytics (Risk Scoring)
- Clear explanations of model decisions (Explainable AI)
- Prescriptive solutions and interventions (Strategic Planning)
- Direct actionability (Simulations and Drafted Outreach)

Agentic Churn Intelligence solves this gap by transforming raw ML predictions into comprehensive, simulated retention campaigns utilizing LLM-based multi-agent workflows.

---

## 🖥️ Tech Stack

### 💻 Backend
- Python 3.9+ 
- FastAPI
- Uvicorn
- LangGraph
- Groq API (`llama-3.3-70b-versatile`)
- Pandas & NumPy
- Scikit-learn
- XGBoost & SHAP

### 🎨 Frontend
- Node.js (v16+)
- React (Vite)
- Framer Motion (Animations)
- Custom CSS (Premium UI aesthetics)

### ☁️ Deployment
- **Backend:** Render.com
- **Frontend:** Vercel.com

---

## 📁 Project Structure

```text
major project/
│
├── frontend/               # React UI elements, Vite configuration, Framer Motion
├── backend/                # FastAPI application, LangGraph orchestrator
│   ├── api/
│   │   └── main.py
│   └── agents/             # Risk, Explainability, Strategy, Simulation, Communication
├── ml_pipeline/            # Generates synthetic data, trains XGBoost & SHAP explainer
│   ├── data_generator.py
│   └── train.py
├── data/                   # telecom_churn.csv and saved models
├── requirements.txt        # Python backend dependencies
├── .env                    # Environment variables (Groq API Key)
└── README.md
```

---

## ▶️ Run Locally

### Prerequisites
- Python 3.9+
- Node.js (v16+)
- A Groq API Key (`gsk_...`)

### 1️⃣ Installation

```bash
# Clone repository
git clone https://github.com/kamrankausher/agentic-retention-ai.git
cd agentic-retention-ai

# Backend Setup
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

# Frontend Setup
cd frontend
npm install
cd ..
```

### 2️⃣ Prepare the ML Pipeline
Generates synthetic data (`telecom_churn.csv`) and fits the XGBoost models & SHAP explainers.
```bash
cd ml_pipeline
python data_generator.py
python train.py
cd ..
```

### 3️⃣ Environment Variables
Create a file named `.env` in the root folder with the following content:
```env
GROQ_API_KEY="your_api_key_here"
```

### 4️⃣ Run the Stack (Two Terminals Required)

**Terminal 1 (Backend API):**
```bash
# Windows
.\venv\Scripts\uvicorn.exe backend.api.main:app --reload

# Mac/Linux
uvicorn backend.api.main:app --reload
```

**Terminal 2 (Frontend React UI):**
```bash
cd frontend
npm run dev
```

Navigate to `http://localhost:5173/` safely connected to your `8000` backend API.

---

## ☁️ Deployment Guide (Production)

### 🚀 1. Github Repository
Always push your code to GitHub first. Create a blank repo on Github, then run:
```bash
git init
git add .
git commit -m "Final Product Release"
git branch -M main
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

### ⚙️ 2. Deploy Backend (Render.com)
1. Create a new "Web Service" on Render and link your Github Repo.
2. **Build Command**: `pip install -r requirements.txt`
3. **Start Command**: `uvicorn backend.api.main:app --host 0.0.0.0 --port $PORT`
4. *Important*: Add your `GROQ_API_KEY` in Render's Environment Variables settings!

### 🌐 3. Deploy Frontend (Vercel.com)
1. Import the same GitHub repo into Vercel.
2. **Wait!** Before deploying, you must edit `frontend/src/App.jsx` and `frontend/vite.config.js`. You need to replace `/api/v1/run-agents` in `axios.post` with the fully deployed Render URL you just got (e.g., `https://your-backend.onrender.com/api/v1/run-agents`). 
3. Change the Root Directory in Vercel settings to `frontend/`.
4. Deploy! Vercel will automatically run `npm run build`.

---

## 🎯 Use Cases

- Final-Year University Major Project Presentable
- FAANG Interview Demonstration  
- Production Deployment Example  
- Multi-Agent Orchestration & Explainable AI Showcase  

---

## 👤 Author

**Kamran Kausher**  
Final-Year B.Tech CSE  
AI/ML & Generative AI Engineer  

---

## 🌐 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=plastic&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kamran-kausher-7585b0370)  
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=plastic&logo=github&logoColor=white)](https://github.com/kamrankausher)  
[![Email](https://img.shields.io/badge/Email-D14836?style=plastic&logo=gmail&logoColor=white)](mailto:kamrankausher@gmail.com)

---

⭐ This project rigorously demonstrates the fusion of scalable predictive Machine Learning and advanced multi-agent workflows (powered by LLMs)—bringing proactive, explainable intelligence to customer retention pipelines.
