<div align="center">
  
# 🤖 Agentic Churn Intelligence  
**Advanced Customer Retention Powered by Multi-Agent AI Orchestration**

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blueviolet?style=for-the-badge&logo=python)](https://python.org/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-FF4F00?style=for-the-badge&logo=langchain&logoColor=white)](https://python.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-API-black?style=for-the-badge&logo=openai)](https://groq.com/)

A **production-grade, full-stack enterprise application** that predicts customer churn, unpacks model reasoning via **SHAP**, and orchestrates a specialized multi-agent AI swarm to proactively execute and simulate business interventions.

</div>

---

## 👁️‍🗨️ Application Preview

<p align="center">
  <em>Sleek, staggered data revelation designed for FAANG-level business intelligence.</em><br/><br/>
  <!-- Replace the 'src' below with your actual project screenshots when ready -->
  <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2670&auto=format&fit=crop" width="850" alt="Dashboard Cover Placeholder" style="border-radius: 8px; border: 1px solid #333;" />
  <br/><br/>
  <img src="https://images.unsplash.com/photo-1618761714954-0b8cd0026356?q=80&w=2670&auto=format&fit=crop" width="850" alt="Agent Pipeline Placeholder" style="border-radius: 8px; border: 1px solid #333;" />
</p>

---

## 🦾 The Agent Swarm (Architecture)

The intelligence layer runs on a cyclic, event-driven flow managed by **LangGraph** & **FastAPI**. Every customer goes through a rigorous evaluation by 5 distinct AI nodes:

| Node ID | Agent Module | Primary Function | Core Technology |
| :---: | :--- | :--- | :--- |
| **01** | **Risk Agent** | Evaluates the baseline probability of churn | XGBoost + Scikit-learn |
| **02** | **Explainability Agent** | Extracts core friction drivers from raw data | SHAP Mathematics |
| **03** | **Strategy Agent** | Formulates a hyper-precise intervention policy | Groq `llama-3.3-70b` |
| **04** | **Simulation Agent** | Predicts the exact new churn probability post-policy| Groq `llama-3.3-70b` |
| **05** | **Communication Agent** | Drafts a highly tailored retention email / script | Groq `llama-3.3-70b` |

> **System Note:** The React UI sequentially renders the output of each agent, generating an immersive, real-time data-flow experience for the end user.

---

## ✨ System Capabilities

- **Autonomous Agentic Orchestration:** Operates autonomously via LangGraph, managing state and looping between sub-agents to synthesize final decisions.
- **Explainable AI (XAI):** Moves beyond "black box" prediction. Feeds specific friction points (calculated via SHAP) directly into the LLM logic gates.
- **Lightning-Fast Reasoning:** Utilizes Groq's LPU inference engine to run `llama-3.3-70b-versatile` with instantaneous latency.
- **Glassmorphic React UI:** Built with Vite and Framer Motion, featuring smooth pipeline visualizations, animated widgets, and premium dark-mode styling.

---

## 🧠 The Intelligence Gap

Most existing CRM systems provide a static churn probability, leaving corporate teams without actionable context or a follow-up strategy. 

**Agentic Churn Intelligence** solves this matrix. It moves beyond passive analytics by deploying a swarm of AI agents that automatically:
1. **Identify the threat** (Machine Learning Risk Scoring)
2. **Explain the cause** (Mathematical SHAP Analysis)
3. **Prescribe the cure** (Generative AI Strategic Planning & Simulation)

---

## ⚙️ Core Technology Matrix

### 💻 Backend Cluster
- **Language / Framework:** Python 3.9+, FastAPI, Uvicorn
- **AI Orchestrator:** LangGraph
- **LLM Engine:** Groq API (`llama-3.3-70b-versatile`)
- **Data & ML:** Pandas, NumPy, Scikit-learn, XGBoost, SHAP

### 🎨 Frontend Terminal
- **Framework:** React.js (Node.js v16+ / Vite)
- **Engine Animations:** Framer Motion
- **Aesthetic Core:** Custom Premium CSS (Dark Glassmorphism)

### ☁️ Deployment Pipeline
- **Backend Infrastructure:** Render.com
- **Frontend Edge Network:** Vercel.com

---

## 📁 Architecture Tree

```text
major_project/
│
├── frontend/               # React UI layers, Vite config, Framer animations
├── backend/                # API Gateway & LangGraph Nodes
│   ├── api/
│   │   └── main.py
│   └── agents/             # The swarm: Risk, Explainability, Strategy...
├── ml_pipeline/            # Deep Learning & ML routines
│   ├── data_generator.py   # Synthetic telecom_churn engine
│   └── train.py            # Model fitting logic
├── data/                   # Encrypted states & saved models
├── requirements.txt        # System dependencies
└── .env                    # Secure API keys
```

---

## 🚀 Boot Sequence (Local Execution)

### System Prerequisites
- `Python 3.9+`
- `Node.js (v16+)`
- `Groq API Key` initialized

### 1️⃣ Repository Initialization
```bash
git clone https://github.com/kamrankausher/agentic-retention-ai.git
cd agentic-retention-ai

# Activate Python Virtual Environment
python -m venv venv
# Windows: venv\Scripts\activate || Mac/Linux: source venv/bin/activate

# Install Core ML & Backend Dependencies
pip install -r requirements.txt

# Initialize UI Terminal
cd frontend && npm install
cd ..
```

### 2️⃣ ML Pipeline Compilation
Generates baseline synthetic data (`telecom_churn.csv`) and compiles the XGBoost predictor & SHAP models.
```bash
cd ml_pipeline
python data_generator.py
python train.py
cd ..
```

### 3️⃣ Security Environment
Create an `.env` file at the root to inject your Groq credentials:
```env
GROQ_API_KEY="your_api_key_here"
```

### 4️⃣ Engage System (Dual Terminal Setup)
**Terminal Alpha (Backend):**
```bash
# Windows
.\venv\Scripts\uvicorn.exe backend.api.main:app --reload

# Mac/Linux
uvicorn backend.api.main:app --reload
```
**Terminal Beta (Frontend):**
```bash
cd frontend
npm run dev
```
🟢 System Online: Navigate to `http://localhost:5173/` 

---

## ☁️ Production Deployment sequence

To deploy the intelligence network globally:

### 1. Global Git Push
```bash
git init
git add .
git commit -m "System: Deploying Agentic AI Cluster"
git branch -M main
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

### 2. Backend Orchestrator (Render)
1. Initialize a Web Service via Render.com and attach the GitHub repository.
2. **Build CMD:** `pip install -r requirements.txt`
3. **Start CMD:** `uvicorn backend.api.main:app --host 0.0.0.0 --port $PORT`
4. ⚠️ **Critical:** Inject `GROQ_API_KEY` into Render's Environment Variables.

### 3. Frontend Terminal (Vercel)
1. Attach the same repository into Vercel.
2. Edit `frontend/src/App.jsx` and `frontend/vite.config.js`. You must redirect your API calls (e.g. `axios.post`) to the live Render backend config (e.g., `https://your-backend.onrender.com/api/v1/run-agents`).
3. Set the Vercel **Root Directory** to `frontend/`.
4. Deploy pipeline.

---

## 🎯 Strategic Implementations

- **University Final-Year Major Project** (Distinction-level validation)
- **FAANG / Enterprise Interview Demonstration**
- **Production-Grade Analytics Concept Showcase**
- **Multi-Agent Orchestration & Explainable AI Proof of Concept**

---

## 👨‍💻 Engineering Core

**Kamran Kausher**  
Final-Year B.Tech CSE  
*AI/ML & Generative AI Systems Engineer*

<div align="left">
  <a href="https://www.linkedin.com/in/kamran-kausher-7585b0370">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/kamrankausher">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="mailto:kamrankausher@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</div>

---

<div align="center">
  <p>⭐ <i>This system rigorously highlights the fusion of actionable ML prediction and multi-agent AI execution, bringing fully autonomous reasoning to modern enterprise retention.</i></p>
</div>
