# Market Analyzer Agent – Frontend

A **Streamlit-based web interface** for the Market Analyzer Agent that allows users to generate detailed market reports on products in the Saudi Arabian market. The frontend connects to the Flask backend API and provides an interactive and user-friendly dashboard.

> 🖥️ Works together with the [Backend Repo](https://github.com/your-username/market-analyzer-backend).

---

## ✨ Features

* Simple and intuitive web interface built with **Streamlit**
* Input product details and instantly receive market analysis reports
* View competitor comparisons, market gaps, and tailored recommendations
* Downloadable reports for further analysis

---

## 📸 Demo

[*Watch from here*](https://youtu.be/SKb-t1k2A2s)

---

## ⚙️ Installation

Clone the frontend repo:

```bash
git clone https://github.com/your-username/market-analyzer-frontend.git
cd market-analyzer-frontend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the frontend:

```bash
streamlit run app.py
```

---

## 🔗 Backend Connection

Ensure the [backend](https://github.com/your-username/market-analyzer-backend) is running. Update the API endpoint in the frontend configuration if needed:

```python
BACKEND_URL = "http://127.0.0.1:5000"   # or your deployed backend URL
```

---

## 🛠 Tech Stack

* **Frontend** → Streamlit
* **Backend** → Flask (LangChain + LangGraph orchestration)
* **Language** → Python
* **Region Focus** → Saudi Arabia Market

---

## 📂 Project Structure

```
.
├── demo.py                  # Main Streamlit frontend app
├── model.py/                  # Helper model for receving the data
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

* Add authentication and user accounts
* Enhance visualizations with competitor insights and charts

---

## 📬 Contact

If you find this project useful, feel free to ⭐ star the repo and connect on [LinkedIn](www.linkedin.com/in/your-linkedin).
