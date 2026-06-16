# ⭐ Inverted Star Pattern using Python

A simple Python program that prints an **Inverted Right-Angled Star Pattern** using nested loops.

## 📌 Description

This project demonstrates the use of:

- 🔄 Nested Loops
- ⭐ Pattern Printing
- 🐍 Python Basics
- 🎯 Logic Building

---

## 📂 Pattern 1

### Output

```text
*
* *
* * *
* * * *
* * * * *
```

### Screenshot

(<img width="238" height="180" alt="Screenshot 2026-06-16 112248" src="https://github.com/user-attachments/assets/f92e3fc4-693e-457e-a092-b14be792f0dd" />
)

---

## 📂 Pattern 2

### Output

```text
* * * * * *
* * * * *
* * * *
* * *
* *
*
```

### Screenshot

(<img width="262" height="187" alt="Screenshot 2026-06-16 112255" src="https://github.com/user-attachments/assets/0f38f347-fa2f-4cbf-a57f-d32b90240aee" />
)

---

## 🧾 Code

```python
# Right Angle Star Pattern

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# Inverted Right Angle Star Pattern

for i in range(6, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

2. Navigate to project folder

```bash
cd your-repository
```

3. Run the program

```bash
python pattern.py
```

---

## 🛠️ Technologies Used

- 🐍 Python 3
- 💻 VS Code / PyCharm

---

## 🎯 Learning Outcomes

✅ Understanding nested loops  
✅ Pattern printing logic  
✅ Python fundamentals  
✅ Loop control and iteration

---

## 👨‍💻 Author

**Kumar Shiromani**

⭐ If you found this project helpful, don't forget to star the repository!
