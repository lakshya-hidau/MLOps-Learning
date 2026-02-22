# End-to-End MLOps Capstone Project

[![MLflow](https://img.shields.io/badge/MLflow-Experiment--Tracking-blue?style=flat-square&logo=mlflow)](https://mlflow.org/)
[![DVC](https://img.shields.io/badge/DVC-Data--Versioning-orange?style=flat-square&logo=dvc)](https://dvc.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-blue?style=flat-square&logo=docker)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-Cloud--Services-yellow?style=flat-square&logo=amazon-aws)](https://aws.amazon.com/)
[![EKS](https://img.shields.io/badge/Kubernetes-EKS-blue?style=flat-square&logo=kubernetes)](https://aws.amazon.com/eks/)

## 🚀 Overview
This repository contains a comprehensive, production-ready MLOps project that automates the entire machine learning lifecycle—from data ingestion and experimentation to deployment and monitoring. Built as a capstone project, it demonstrates best practices in CI/CD, data versioning, and cloud-native deployments.

## ✨ Key Features
- **Data Versioning (DVC):** Tracks datasets and models with storage on AWS S3 and local remotes.
- **Experiment Tracking (MLflow):** Integrated with Dagshub to log parameters, metrics, and models.
- **Automated Pipelines:** DVC pipelines for seamless execution of data preprocessing, feature engineering, and training.
- **Containerization:** Specialized Docker images for consistent development and deployment environments.
- **Cloud Deployment:** Scalable deployment on **AWS Elastic Kubernetes Service (EKS)** using `kubectl` and `eksctl`.
- **CI/CD:** Automated testing and deployment workflows via **GitHub Actions**.
- **Monitoring:** Infrastructure and application monitoring using **Prometheus** and **Grafana**.

## 🛠️ Technology Stack
| Category | Tools |
| :--- | :--- |
| **Language** | Python 3.10 |
| **Orchestration** | DVC |
| **Tracking** | MLflow, Dagshub |
| **Backend** | Flask |
| **Containerization** | Docker |
| **Cloud Infrastructure** | AWS (S3, ECR, IAM, EC2, EKS) |
| **Monitoring** | Prometheus, Grafana |
| **Kubernetes** | kubectl, eksctl |

## 📂 Project Structure
```text
├── .dvc/               # DVC configuration
├── data/               # External, raw, and processed data (tracked by DVC)
├── flask_app/          # Flask web application and Dockerfile
├── local_storage/      # Local DVC remote storage (temporary)
├── logs/               # Application and training logs
├── mlruns/             # Local MLflow runs
├── models/             # Trained and serialized models (tracked by DVC)
├── src/                # Source code (Ingestion, Preprocessing, Training, etc.)
├── .github/workflows/  # CI/CD pipeline definitions
├── dvc.yaml            # Pipeline definition for DVC
├── params.yaml         # Project parameters
└── requirements.txt    # Python dependencies
```

## ⚙️ Getting Started

### Prerequisites
- Python 3.10+
- [Conda](https://docs.conda.io/en/latest/) (optional but recommended)
- AWS CLI configured with appropriate credentials
- Docker Desktop installed

### Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Project_02_Capstone
   ```

2. **Set up virtual environment:**
   ```bash
   conda create -n atlas python=3.10 -y
   conda activate atlas
   pip install -r requirements.txt
   ```

3. **Initialize DVC:**
   ```bash
   dvc pull
   ```

### Running the Project
- **Execute Training Pipeline:**
  ```bash
  dvc repro
  ```
- **Start Flask App:**
  ```bash
  cd flask_app
  python app.py
  ```

## 📈 Monitoring and Deployment
The project includes setup scripts and documentation for:
- Deploying to **AWS EKS** via GitHub Actions.
- Configuring **Prometheus** for metric scraping.
- Visualizing health and performance on **Grafana** dashboards.

## 📄 License
This project is licensed under the MIT License.
