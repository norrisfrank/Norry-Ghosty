# NORRY_GHOSTY — Digital Intelligence Suite

A professional, modular OSINT (Open Source Intelligence) dashboard designed for structured metadata reconnaissance across network, telecom, and social identifiers.

_"Done as a fun little project to practice python and tracking."_ — **Norris Frank**

## 🚀 Overview

**NORRY_GHOSTY** is a specialized toolset that transforms technical data-gathering into a streamlined, high-performance web experience. It leverages multiple public APIs and reconnaissance techniques to extract deep metadata from digital identifiers.

## 💎 Features

### 🌍 IP Geolocation Scanner
*   **Deep Recon**: Extraction of ASN details, ISP mapping, and physical origin.
*   **Infrastructure Detection**: Identifying hosting providers, residential proxies, and potential threat indicators.
*   **Visual Mapping**: Direct links to physical coordinate mapping via Google Maps.

### 📞 Telecom Metadata Analyzer
*   **Carrier Extraction**: Identification of network operators and line types (Mobile, Fixed-line, VOIP).
*   **Regional Intelligence**: Geolocation of the numbering plan, including region codes and timezones.
*   **Standardization**: International E.164 formatting and validity verification.

### 👤 ID Linker (Social Recon)
*   **Identity Mapping**: Cross-referencing targeted usernames against dozens of social platforms.
*   **Direct Links**: Real-time extraction of profile URLs for manual reconnaissance.
*   **Fluid Status**: Immediate feedback on account existence status.

## 🛠 Tech Stack

*   **Backend**: Python / Flask
*   **Frontend**: Modern Vanilla CSS (Orange Professional Aesthetic) / JavaScript
*   **APIs**: IPWho.is, Ipify, and customized OSINT libraries.
*   **Deployment**: Fully configured for Render.com via Gunicorn.

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/NorrisFrank/NORRY_GHOSTY.git
cd NORRY_GHOSTY
pip install -r requirements.txt
```

### 2. Local Launch
Execute the Flask application:
```bash
python app.py
```
Access the dashboard at: `http://127.0.0.1:5000`

## ☁️ Deployment
The project includes a `Procfile` ready for **Render**. Simply connect your GitHub repository to Render, and it will deploy automatically using the production-grade Gunicorn server.

---
**Created & Maintained by Norris Frank**
*Educational project for practicing Python and Digital Tracking.*
