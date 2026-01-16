# 🛒 SmartPOS: AI-Integrated Retail Billing System

![Python](https://img.shields.io/badge/Backend-Flask-green?style=for-the-badge&logo=python)
![Database](https://img.shields.io/badge/Database-SQLite-blue?style=for-the-badge&logo=sqlite)
![Frontend](https://img.shields.io/badge/Frontend-HTML5%20%2F%20JS-orange?style=for-the-badge&logo=html5)
![Status](https://img.shields.io/badge/Status-Expo%20Ready-red?style=for-the-badge)

**SmartPOS** is a web-based Point of Sale (POS) application designed to modernize supermarket billing. Unlike traditional systems that rely on expensive hardware, SmartPOS utilizes **Computer Vision** and **Cloud-Native Architecture** to turn any laptop or tablet into a fully functional billing counter.

It features a unique **Consumer Safety Engine** that automatically detects and blocks the sale of expired products during checkout.

---

## 🚀 Key Features

### 1. Zero-Hardware Scanning (Vision Input)
* Replaces expensive laser scanners with standard webcams.
* Uses **Optical Recognition** to identify product labels/barcodes from the video stream.
* Ideal for mobile kiosks and pop-up stores.

### 2. 🛡️ Active Safety Protocols (Expiry Lock)
* **The Problem:** Cashiers often accidentally sell expired goods.
* **The Solution:** The system checks the manufacturing/expiry date in real-time against the database.
* **Outcome:** If a product is expired, the system **blocks the transaction** and flashes a red alert.

### 3. Professional Data Persistence
* Powered by **SQLite** and **SQLAlchemy ORM**.
* Data persists across restarts (ACID Compliance).
* Includes an **Audit Log** (`SalesLog`) that records every transaction for security and analytics.

### 4. Enterprise-Grade Security
* Secure Login Gate for authorized personnel only.
* Role-based access simulation.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Python (Flask) | Handles business logic, DB queries, and API routing. |
| **Database** | SQLite | Serverless, self-contained SQL database engine. |
| **ORM** | SQLAlchemy | Object-Relational Mapping for professional DB management. |
| **Frontend** | HTML5 / CSS3 | Responsive design using the 'Inter' font family. |
| **Scripting** | JavaScript (ES6) | Handles webcam streaming and Fetch API calls. |

---

| **Login Interface** | **Billing Dashboard** |
| :---: | :---: |
|                  |                  |

---

## ⚙️ Installation & Setup

Follow these steps to deploy the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR-USERNAME/smart-pos.git](https://github.com/YOUR-USERNAME/smart-pos.git)
cd smart-pos# Smart-Scan-Web
"Enterprise-grade retail POS solution utilizing Optical Character Recognition (OCR) for hardware-free checkout. Built with Python, Flask, SQLAlchemy, and JavaScript."
