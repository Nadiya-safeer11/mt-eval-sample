# Machine Translation Evaluation Sample

This is a simple project to evaluate the quality of a machine-translated text using the BLEU score.

---

## 📂 Project Structure
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Nadiya-safeer11/mt-eval-sample/blob/main/run.ipynb)


```
mt-eval-sample/
├── data/
│   ├── reference.txt
│   └── hypothesis.txt
├── evaluate.py
├── run.py
├── requirements.txt
└── README.md
```

---

## 📋 Description

This script uses [SacreBLEU](https://github.com/mjpost/sacrebleu) to evaluate a machine translation output (`hypothesis.txt`) against a reference translation (`reference.txt`).

---

## ⚙️ Requirements

Install the required package:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python run.py
```

### ✅ Expected Output

```
BLEU Score: 72.50
```

---

## 📘 Example

- `reference.txt`:
  ```
  This is a test sentence.
  The quick brown fox jumps over the lazy dog.
  ```

- `hypothesis.txt`:
  ```
  This is a test sentence.
  The quick brown fox jumped over a lazy dog.
  ```

---

## 🔗 License

This project is free to use and modify for educational purposes.
