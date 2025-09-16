# Sarcasm Detector Demo  

A web-based demo that shows how our sarcasm detection model works.  
The interface supports both **text input** and **audio upload**, simulating the end-to-end flow of detecting sarcasm using deep learning (LSTM model).  

---

## 🚀 Features  
- **Dual Input Modes**  
  - ✍️ Enter text directly  
  - 🎙️ Upload audio files (≤ 1MB)  
- **Interactive UI**  
  - Choice between text and audio inputs 
  - Animated **loading progress bar** with step-by-step process showing the different stages(`Pre-Processing → Analyzing → Detecting Sarcasm`)  
- **Result Display**  
  - Shows the predicted output (e.g., *Sarcastic* or *Not Sarcastic*)  
  - Displays accuracy score  for predicted result
- **Process Flow Toggle**  
  - Option to show/hide model’s working steps  

---

## 📂 Project Structure  
```bash
├── index.html          # Main UI structure
├── script.js           # Frontend logic for inputs, loading, and results
├── style.css           # Styling for the app
├── app.py              # Backend (Flask/FastAPI) integration point for ML model
├── lstm_model.keras    # Trained sarcasm detection model (large file)
└── README.md           # Documentation
```
---

## ⚡ How It Works  
1. Choose **Text** or **Audio** input.  
2. Enter your sentence or upload an audio file.  
3. Click **Submit**, and the app will walk you through the steps: Pre-processing → Analyzing → Detecting Sarcasm before showing final result.
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
2. **Run the backend**

```
python app.py
```

3. **Open the frontend**

Open index.html in your browser to launch the demo interface.

---

## 📦 Model File
⚠️ The trained LSTM model file (lstm_model.keras) is too large for GitHub’s 100MB limit. 

You may need to download it separately or use Git LFS (Large File Storage) if you want to run the full demo locally.


## Contribution
- Edit by Priyanshi Modi
