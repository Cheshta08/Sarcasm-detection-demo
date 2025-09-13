# Sarcasm Detector Demo  

A web-based demo that showcases how our sarcasm detection model works.  
The interface supports both **text input** and **audio upload**, simulating the end-to-end flow of detecting sarcasm using machine learning.  

---

## 🚀 Features  
- **Dual Input Modes**  
  - ✍️ Enter text directly  
  - 🎙️ Upload audio files (≤ 1MB)  
- **Interactive UI**  
  - Choice between text and audio  
  - Animated **loading progress bar** with step-by-step process (`Pre-Processing → Analyzing → Detecting Sarcasm`)  
- **Result Display**  
  - Shows predicted output (e.g., *Sarcastic* or *Not Sarcastic*)  
  - Displays accuracy score  
- **Process Flow Toggle**  
  - Option to show/hide model’s working steps  

---

## 📂 Project Structure  
├── index.html # Main UI structure
├── script.js # Frontend logic for inputs, loading, and results
├── style.css # Styling for the app
├── app.py # Backend (Flask/FastAPI) integration point for ML model
├── lstm_model.keras # Trained sarcasm detection model (large file)
└── README.md # Documentation

---

## ⚡ How It Works  
1. Choose **Text** or **Audio** input.  
2. Enter your sentence or upload an audio file.  
3. Click **Submit** → the app simulates pre-processing, analysis, and sarcasm detection.  
4. Results are displayed with prediction and accuracy.  

---

## 🖼️ Demo Preview  
<img width="1907" height="937" alt="image" src="https://github.com/user-attachments/assets/e3c1a883-a106-45cd-b15e-7d9e5e8f9cd1" />
  

---

## 🛠️ Installation & Usage  

1. **Clone the repo**  
   ```
   git clone https://github.com/Cheshta08/Sarcasm-detection-demo.git

   ```
   ```
   cd Sarcasm-detection-demo
   ```
Run the backend

```
python app.py
```

Open the frontend

Open index.html in your browser.

📦 Model File
The trained LSTM model (lstm_model.keras) is large in size.

GitHub has a 100MB per file limit.
