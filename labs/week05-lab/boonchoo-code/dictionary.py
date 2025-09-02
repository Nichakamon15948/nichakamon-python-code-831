# Empty dictionary
empty_dict = {}
another_empty_dict = dict()

# Dictionary with initial  #เก็บข้อมูลนักเรียนหรือคน
student = {
    "name": "Alice Smith", #ข้างซ้ายคือคี("name") ขวาคือข้อมูล
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Different data types as values
mixed_dict = {
    "string": "hello", # ฝั่งขวาคือเดต้าจากฝั่งซ้าย
    "number": 42,
    "list": [1, 2, 3], #วงเล็บ
    "nested_dict": {"key": "value"},
    "boolean": True
}

# Using dict() constructor
person = dict(name="Bob", age=25, city="Bangkok") #กำหนดคีมวาลู่เป็นอะไร

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)

dict_from_pairs = {
    "a": 1,
    "b": 2,
    "c": 3,
}
print(f"Student: {student}")
print(f"Mixed: {mixed_dict}")
print(f"Person: {person}")
print(f"From pairs: {dict_from_pairs}")