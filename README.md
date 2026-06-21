# 🎬 Movie Recommendation System (Content-Based Filtering)

## 📌 Overview

This project is a **Movie Recommendation System** built using **Python** and **Machine Learning techniques**.
It recommends movies based on similarity in genres using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🚀 Features

* Recommends movies based on genre similarity
* Uses TF-IDF for text feature extraction
* Computes similarity using cosine similarity
* Simple command-line interface
* Fast and efficient for small datasets

---

## 🧠 How It Works

1. Dataset containing movie titles and genres is loaded
2. Missing values are handled
3. Genres are converted into numerical vectors using TF-IDF
4. Cosine similarity is computed between all movies
5. User inputs a movie name
6. System returns top 5 similar movies

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas
* Scikit-learn

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── movie.csv          # Dataset
├── main.py            # Main Python script
├── README.md          # Project documentation
└── requirements.txt   # Dependencies
```

---

## ▶️ How to Run

### Step 1: Clone the repository

```
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Run the program

```
python main.py
```

---

## 💻 Example Usage

```
Enter movie name: Avatar

Recommended Movies:
👉 Guardians of the Galaxy
👉 Star Wars
👉 Avengers
👉 Interstellar
👉 The Martian
```

---

## ⚠️ Limitations

* Only uses genres for recommendation
* Not personalized (same result for all users)
* Works best with clean dataset

---

## 🔮 Future Improvements

* Add user-based recommendations
* Build web app using Flask/Django
* Add ratings and reviews
* Use advanced ML models

---

## 👨‍💻 Author

Diya Krishna

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
