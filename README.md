# Blue-Green Deployment CI/CD Pipeline on AWS

## Project Overview

This project demonstrates a **zero-downtime deployment pipeline** using DevOps tools.
The pipeline automatically deploys new versions of an application using **Blue-Green deployment strategy**.

It includes:

* CI/CD pipeline using Jenkins
* Containerization using Docker
* Infrastructure automation using Ansible
* AWS EC2 servers
* Nginx load balancer
* Health checks before traffic switching

This ensures **safe deployments without downtime**.

---

# Architecture

Developer Push (GitHub)
↓
GitHub Webhook
↓
Jenkins Pipeline
↓
Docker Build & Push
↓
Ansible Deployment
↓
Blue Server / Green Server
↓
Health Check
↓
Nginx Traffic Switch

---

# Tools Used

| Tool       | Purpose                      |
| ---------- | ---------------------------- |
| AWS EC2    | Infrastructure hosting       |
| Jenkins    | CI/CD pipeline automation    |
| Docker     | Application containerization |
| Docker Hub | Image registry               |
| Ansible    | Configuration management     |
| Nginx      | Load balancer                |
| GitHub     | Source code repository       |
| Flask      | Demo web application         |

---

# Blue-Green Deployment Flow

1. User pushes code to GitHub
2. GitHub webhook triggers Jenkins pipeline
3. Jenkins builds Docker image
4. Image pushed to Docker Hub
5. Ansible deploys container to inactive server
6. Health check is performed
7. If healthy → traffic switched in Nginx
8. If unhealthy → deployment stops

---

# Features

✔ Zero-downtime deployment
✔ Automated CI/CD pipeline
✔ Health-check validation
✔ Automatic Blue/Green environment detection
✔ Traffic switching through Nginx

---

# Deployment Cycle

Deployment 1

Traffic → BLUE
Deploy → GREEN
Switch → GREEN

Deployment 2

Traffic → GREEN
Deploy → BLUE
Switch → BLUE

---

# Application Endpoints

```
/
Main application page

/health
Health check endpoint
```

---

# Project Outcome

This project demonstrates a **production-style CI/CD pipeline** with automated deployment and traffic switching.

It shows practical experience with **DevOps tools and deployment strategies used in modern cloud infrastructure.**

---


