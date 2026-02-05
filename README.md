Nice project 👍 — here’s a clean, professional **README.md** you can drop straight into your repo. I’ve written it like a real-world open-source project, but still student-friendly.

---


# 🎓 LPU Smart CGPA & Percentile Estimator 
## Link- https://lpu-cgpa-calculator.streamlit.app/
A **Streamlit-based web application** that helps Lovely Professional University (LPU) students **estimate TGPA and percentile ranges** using **relative grading trends**.  
The tool works subject-wise and provides an approximate CGPA range based on marks, highest score, and credit weightage.

---

## ✨ Features

- 📘 Subject-wise input (marks, highest marks, credits)
- 📊 Automatic grade & grade-point estimation
- 🎯 TGPA range prediction (lower–upper bound)
- 📈 Percentile category insights
- 🌙 Modern dark UI with gradient styling
- ⚡ Fast, lightweight, and easy to use

---

## 🖥️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Custom CSS** for enhanced UI

---

## 📂 Project Structure

```

📁 LPU-CGPA-Estimator
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
│
├── 📁 styles
│   └── main.css           # Custom UI styling
│
└── README.md              # Project documentation

````

> ⚠️ Make sure `main.css` is placed inside a `styles/` folder as shown above.

---

## 🚀 Installation & Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/LPU-CGPA-Estimator.git
cd LPU-CGPA-Estimator
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
streamlit run app.py
```

The app will open automatically in your browser 🌐

---

## 📊 How It Works

1. Enter the **number of subjects**
2. For each subject, input:

   * Subject name
   * Your marks
   * Highest marks in class
   * Credit value
3. The app:

   * Calculates your percentage vs highest
   * Maps it to **relative grade bands**
   * Estimates **grade points**
   * Computes **TGPA range**

---

## 📌 Notes & Disclaimer

* Results are **approximate**
* Based on **common relative grading trends at LPU**
* Actual TGPA/CGPA may vary depending on:

  * Class performance
  * Faculty grading decisions
  * University normalization rules

> 💡 Top performers may receive higher grades than estimated.

---
## ❤️ Author

**Anchal Shukla**
Made with passion to help fellow LPU students 🎓

---

## ⭐ Support

If you found this project helpful:

* Give it a ⭐ on GitHub
* Share it with friends
* Fork & improve it 🚀




