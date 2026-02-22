# 🚀 End-to-End MLOps: Production-Grade ML Pipelines

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![MLOps](https://img.shields.io/badge/MLOps-Production--Ready-brightgreen?style=flat-square)](https://mlops.org/)
[![DVC](https://img.shields.io/badge/DVC-Data--Versioning-orange?style=flat-square&logo=dvc)](https://dvc.org/)
[![MLflow](https://img.shields.io/badge/MLflow-Experiment--Tracking-blueviolet?style=flat-square&logo=mlflow)](https://mlflow.org/)
[![GitHub License](https://img.shields.io/github/license/lakshya-hidau/MLOps-Learning?style=flat-square&color=blue)](LICENSE)

A comprehensive repository showcasing the implementation of modern MLOps practices, inspired by [The Ultimate MLOPS Course](https://youtube.com/playlist?list=PLupK5DK91flV45dkPXyGViMLtHadRr6sp&si=58s-jIiTSMy00USr). This workspace contains two major projects demonstrating end-to-end machine learning lifecycles, from automated data ingestion to containerized cloud deployment.
***

## 🏗️ MLOps Architecture

```mermaid
graph TD
    subgraph "Data & Feature Pipeline"
        A[Raw Data Source] -->|Ingest & Store| B[Data Lake/Local Storage]
        B -->|Track & Version| C[DVC]
        C --> D[Data Validation & Cleaning]
        D --> E[Feature Engineering]
    end

    subgraph "Model Development & Experiments"
        E --> F[Model Training]
        F -->|Log Metrics, Params, Artifacts| G[MLflow Tracking]
        F -->|Register Candidate Models| H[MLflow Model Registry]
        G --> I[Experiment Comparison]
    end

    subgraph "Packaging & Deployment"
        F --> J[Model Packaging (FastAPI/Flask)]
        J --> K[Docker Image Build]
        K --> L[Container Registry (DockerHub/ECR)]
        L --> M[Deployment Target (EC2/Cloud/On-Prem)]
    end

    subgraph "CI/CD & Automation"
        N[GitHub Push] --> O[GitHub Actions]
        O -->|Test, Lint, Train, Build| K
        O -->|Trigger Promotion| M
    end

    subgraph "Monitoring & Feedback"
        M --> P[Application Metrics (Prometheus)]
        P --> Q[Dashboards & Alerts (Grafana)]
        Q --> R[Continuous Improvement Loop]
        R --> F
    end
```

***

## 🛠️ Tech Stack & Tools

| Category | Tools & Services |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Core ML** | scikit-learn, pandas, numpy (per-project specific libraries defined in `requirements.txt`) |
| **Data Versioning & Pipelines** | DVC (data, model, and pipeline versioning) |
| **Experiment Tracking & Registry** | MLflow Tracking, MLflow Model Registry, Dagshub (remote tracking backend) |
| **APIs & Serving** | FastAPI, Flask for production-grade REST inference services |
| **Containerization** | Docker for reproducible, portable runtime environments |
| **CI/CD & Automation** | GitHub Actions for testing, building, training, and deployment workflows |
| **Storage & Cloud** | AWS S3 (artifacts and data), AWS EC2 (deployment target) |
| **Model Hosting** | Hugging Face Hub for model distribution and hosting |
| **Monitoring & Observability** | Prometheus for metrics scraping, Grafana Cloud for dashboards and alerts |
| **Version Control** | Git & GitHub for source code and workflow automation |
| **Configuration & Environment** | `.env` files, environment variables, configurable settings per project |

***

## 📂 Project Catalog

### 🚙 Project 01: Vehicle Insurance Prediction  
Path: [`Project_01_Vehicle_Insurance_Data`](Project_01_Vehicle_Insurance_Data)

Predict whether a customer is interested in vehicle insurance using a fully modular and versioned MLOps pipeline.  

- **Problem:** Binary classification on structured tabular data for customer insurance interest prediction.  
- **Pipeline:** Data ingestion, preprocessing, feature engineering, model training, evaluation, and packaging as a service.  
- **Backend & Serving:** **FastAPI** for high-performance inference API with clear request/response schemas.  
- **Data & Artifact Management:**  
  - Data and intermediate artifacts tracked using **DVC**  
  - Model artifacts stored locally and on **Hugging Face Hub** / cloud storage  
- **Cloud Integration:**  
  - **AWS S3** for dataset and artifact storage  
  - **AWS EC2** for running containerized inference services  
- **Focus Areas:**  
  - Clean, modular code architecture (configs, components, pipelines)  
  - Reproducible runs via DVC and environment management  
  - Production-ready API design and deployment workflow  

***

### 🏆 Project 02: Capstone – Sentiment Analysis & Advanced MLOps  
Path: [`Project_02_Capstone`](Project_02_Capstone)

A capstone project implementing a fully automated, production-oriented MLOps pipeline for sentiment analysis.  

- **Problem:** Text sentiment classification with end-to-end orchestration.  
- **Backend & UI:** **Flask** application serving the model and exposing user-facing endpoints.  
- **Data & Pipeline Versioning:**  
  - Strict **DVC** usage for raw data, processed data, models, and pipeline stages  
  - Reproducible experiments with defined stages and metrics  
- **Experiment Management:**  
  - **MLflow** for tracking parameters, metrics, and artifacts  
  - **MLflow Model Registry** for managing model lifecycle (e.g., *Staging* → *Production*)  
- **CI/CD:**  
  - Multi-stage **GitHub Actions** workflows (lint/test → train/evaluate → build Docker → push image)  
  - Automated checks on pull requests and main-branch changes  
- **Containerization & Deployment:**  
  - Dockerized application and inference service  
  - Images pushed to container registry (DockerHub/ECR) for deployment  
- **Monitoring & Observability:**  
  - Integration with **Prometheus** to collect application and model metrics  
  - **Grafana (Cloud)** dashboards for latency, throughput, error rates, and model-level KPIs  
- **Focus Areas:**  
  - Full MLOps lifecycle: data → model → deploy → monitor → iterate  
  - Promotion workflows from experiment to production using MLflow and CI/CD  
  - Aligning with real-world production practices from the Ultimate MLOps Course playlist.  

***

## 🧩 Features Highlight

- **End-to-End Pipelines:** From data ingestion to monitored production deployment.  
- **Reproducibility:** DVC + MLflow ensure consistent data, code, and experiment tracking across runs.  
- **Automation-First:** GitHub Actions drives automated training, testing, packaging, and delivery.  
- **Cloud-Native:** Designed to run on AWS infrastructure with containerized services.  
- **Modular Design:** Clear separation of concerns (config, components, pipelines, utilities, services).  

***

## 🚀 Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/lakshya-hidau/MLOps-Learning.git
   cd MLOps-Learning
   ```

2. **Choose a Project**
   Each project is self-contained with its own `README.md`, `requirements.txt`, and pipeline configuration.

   - [Project 01 Setup – Vehicle Insurance](Project_01_Vehicle_Insurance_Data/README.md)  
   - [Project 02 Setup – Capstone](Project_02_Capstone/README.md)  

3. **Create and Activate Virtual Environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

4. **Install Dependencies**
   Navigate into the desired project and install requirements:
   ```bash
   cd Project_01_Vehicle_Insurance_Data   # or Project_02_Capstone
   pip install -r requirements.txt
   ```

5. **Configure Environment**
   - Create a `.env` file (or export environment variables) for:  
     - AWS credentials (S3/EC2)  
     - MLflow tracking URI / Dagshub remote  
     - Hugging Face token (if needed)  
   - Refer to the project-level README for exact variable names and examples.

6. **Run Pipelines & Services**
   - Use project-specific commands (DVC stages, training scripts, and API run scripts) as documented in each sub-project README.  

***

## 🎓 Learning Source & Inspiration

This repository is built as a hands-on companion to the **Ultimate MLOps Course** YouTube playlist, translating concepts into fully working, production-aligned examples.  

- Playlist: [The Ultimate MLOPS Course](https://youtube.com/playlist?list=PLupK5DK91flV45dkPXyGViMLtHadRr6sp)  

***

<p align="center">Made with ❤️ for the MLOps Community</p>