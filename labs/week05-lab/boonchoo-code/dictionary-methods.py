# Sample data
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96, "Eve": 89}

# Length and membership
print(f"Number of students: {len(scores)}")
print(f"Is Alice in scores? {'Alice' in scores}")
print(f"Is 'Frank' in scores? {'Frank' in scores}")

# Getting keys, values, items
print(f"Students: {list(scores.keys())}")
print(f"Scores: {list(scores.values())}")
print(f"All data: {list(scores.items())}")

# Iterating through dictionary
print("\nAll students and scores:")
for name, score in scores.items():
    print(f"{name}: {score}")

print("\nJust the names:") #รายการของคีย์ทั้งหมด
for name in scores.keys():
    print(name)

print("\nJust the scores:")
for score in scores.values():
    print(score)

# Dictionary comprehension for filtering
high_scores = {name: score for name, score in scores.items() if score >= 90} #ตั้งตัวแปลมาใหม่ชื่อscore ฝั่งซ้ายมีคีเป็น name ฝั่งขวาเป็นscore 
print(f"High scores (>=90): {high_scores}") #มีแค่2คน 

# Finding min/max #ฟังก์ชันหยิบไอเท็มที่มีประเด็นของคะแนน ฝั่งขวาของscores หยิบเฉพาะคนที่คะแนนสูงสุดออกมา,ต่ำสุด 
best_student = max(scores, key=scores.get)
worst_student = min(scores, key=scores.get)
print(f"Best student: {best_student} with {scores[best_student]}") #เข้าถึงข้อมูล
print(f"Lowest score: {worst_student} with {scores[worst_student]}")

# fromkeys() method
subjects = ["Math", "Science", "English"]
default_scores = dict.fromkeys(subjects, 0)
print(f"Default scores: {default_scores}")

# setdefault() method
student_grades = {} 
student_grades.setdefault("Alice", []).append(85) #สร้างคี Aliceขึ้นมา ทำให้เราสามารถยัดใส่เข้าไปได้
student_grades.setdefault("Alice", []).append(92)
student_grades.setdefault("Bob", []).append(78)
print(f"Student grades: {student_grades}")

