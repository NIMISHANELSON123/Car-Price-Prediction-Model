# 🚗 Car Price Prediction Mini Project

A Machine Learning web application built using **Flask** and **Python** to predict used car prices based on various features.

---

## 📋 Table of Contents
- [About The Project](#about-the-project)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Running](#installation--running)
- [Screenshots](#screenshots)

---

## 🎯 About The Project
This mini-project provides a simple and user-friendly web interface where users can input car details (such as year, kilometers driven, fuel type, etc.) to get an estimated market price predicted by a trained machine learning model (`model.pkl`).

---

## 📂 Project Structure
```text
CarPriceApp/
│
├── templates/           # HTML files
│   └── index.html       # Main UI interface
├── screenshots/         # Application screenshots
├── app.py               # Main Flask application
├── model.pkl            # Trained Machine Learning model
└── requirements.txt     # Required Python libraries

⚙️ Prerequisites
Make sure you have Python installed on your system. You will also need the following libraries:
 * Flask
 * pandas
 * scikit-learn
 * numpy
🚀 Installation & Running
 * Clone the repository:
   git clone [https://github.com/your-username/CarPriceApp.git](https://github.com/your-username/CarPriceApp.git)
cd CarPriceApp

 * Install dependencies:
   pip install -r requirements.txt

 * Run the application:
   python app.py

 * Open in browser:
   Open your web browser and go to: http://127.0.0.1:5000/
