# 🏗️ Industry Inventory Manager — Arvind Stone Crusher ERP

![Python](https://img.shields.io/badge/Backend-Python%20Flask-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Firebase](https://img.shields.io/badge/Database-Firebase%20RTDB-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)
![Twilio](https://img.shields.io/badge/Alerts-Twilio%20WhatsApp-F22F46?style=for-the-badge&logo=twilio&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployment-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

A full-stack, cloud-based industrial inventory and operations management platform built for **Arvind Stone Crusher**. It replaces manual paper registers with real-time stock synchronization, mobile QR/barcode scanning, financial analytics, and automated Twilio WhatsApp low-stock alerts.

🌐 **Live Application:** [industry-inventory-manager.vercel.app](https://industry-inventory-manager.vercel.app)

---

## ✨ Key Features

- **🔐 Role-Based Access Control (RBAC):** Dedicated **Staff Workspace** for daily floor logging and an **Administrator Portal** with full system governance, financial analytics, and user management.
- **📷 Instant QR & Barcode Scanning:** Integrated mobile camera scanner (`html5-qrcode`) that recognizes registered item codes to auto-fill product names, units, and standard prices—or links new codes on the spot.
- **🚨 Automated WhatsApp Low-Stock Alerts:** Automatically monitors inventory levels on every transaction and dispatches instant WhatsApp warnings via the **Twilio API** whenever any item drops below **50 units**.
- **📊 Financial & Consumption Analytics:** Interactive `Chart.js` visualizations tracking inflow vs. outflow, spend distribution by category, sector-wise consumption, and active stock valuation with one-click **CSV report exports**.
- **📡 Cloud Sync & Offline Resilience:** Powered by **Firebase Realtime Database** for live multi-device updates across the quarry floor and office, backed by browser `localStorage` support for uninterrupted field operations.
- **🛡️ Production Hardening & UX Safeguards:**
  - Three-layer negative-value blocking (HTML input constraints, JavaScript checks, and Flask server validation).
  - Protected root `admin` account and self-deletion safeguards in user management.
  - Frosted-glass UI with Light/Dark mode toggle, Enter-key login flow, mobile slide-out drawer, and a logout confirmation modal.

---

## 🛠️ Tech Stack & Storage Architecture

| Layer | Technologies Used | Purpose |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3 (Glassmorphism UI), JavaScript, Chart.js, `html5-qrcode`, Toastify.js | Responsive dashboard, camera barcode scanning, and real-time analytics |
| **Backend** | Python 3, Flask (19 REST API endpoints) | Authentication, role verification, stock calculation, and validation |
| **Database** | Firebase Realtime Database + Browser `localStorage` | Live cloud persistence evolved from local JSON prototyping |
| **Notifications** | Twilio WhatsApp Sandbox API | Automated threshold alerts (`< 50` units) to management |
| **Hosting & Security** | Vercel Serverless Functions + Environment Variables | Continuous GitHub deployment with encrypted API credentials |

---

## 📂 Project Structure

```text
Industry-inventory-manager_2/
├── api/
│   └── index.py            # Python Flask backend & REST API routes
├── public/
│   └── index.html          # Single-page frosted-glass frontend & client logic
├── requirements.txt        # Python dependencies (Flask, twilio)
├── vercel.json             # Vercel serverless routing configuration
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/Industry-inventory-manager_2.git
cd Industry-inventory-manager_2
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
For local testing, create a `.env` file in the root directory (do **not** commit this file to GitHub). For production, add these keys inside **Vercel Dashboard → Settings → Environment Variables**:

```env
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
```

### 4. Activate Twilio WhatsApp Sandbox
1. Open the **Twilio Console** → **Messaging** → **Try it out** → **Send a WhatsApp message**.
2. Send the sandbox join code (e.g., `join <sandbox-keyword>`) from your WhatsApp number to `+1 415 523 8886`.
3. Log into the app's **Suppliers & Settings** tab as an Admin and save your recipient number in the format:
   ```text
   whatsapp:+919876543210
   ```

### 5. Run Locally
```bash
python api/index.py
```

---

## 🔌 Core API Endpoints

| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/login` | Public | Authenticates Staff or Admin portal credentials |
| `POST` | `/api/register` | Public | Registers a new staff operator account |
| `POST` | `/api/purchase` | Staff / Admin | Logs inbound stock purchases (blocks negative values) |
| `POST` | `/api/usage` | Staff / Admin | Records material usage and triggers low-stock check |
| `GET` | `/api/stock` | Staff / Admin | Calculates live remaining inventory and stock status |
| `GET` | `/api/resolve_barcode` | Staff / Admin | Resolves scanned QR/barcode to product name, unit, and price |
| `POST` | `/api/create_admin` | Admin Only | Provisions a new administrator account |
| `POST` | `/api/delete_user` | Admin Only | Deletes non-root users while preventing self-deletion |
| `POST` | `/api/activity_log` | Admin Only | Returns full audit trail tagged by username and date |

---

## 👥 Project Team

Developed as a B.Tech CSE (AI & Data Science) project at **MIT World Peace University (MIT-WPU)**:

- **Anant Jaiswal**
- **Pranay Suman**
- **Aditya Renjit**
- **Abhyuday Tripathi**
