# Set relationships
all_animals = {"dog", "cat", "bird", "fish", "rabbit", "hamster"}
pets = {"dog", "cat", "rabbit"}
mammals = {"dog", "cat", "rabbit", "hamster"}
small_pets = {"cat", "rabbit", "hamster"}

print(f"All animals: {all_animals}")
print(f"Pets: {pets}")
print(f"Mammals: {mammals}")
print(f"Small pets: {small_pets}")

# Subset and superset 
print(f"Are pets subset of all animals? {pets.issubset(all_animals)}")#ทุกตัวของ pets เป็นสมาชิก(มีอยู่)ใน all_animals
print(f"Are all animals superset of pets? {all_animals.issuperset(pets)}")

# Disjoint sets (no common elements)
birds = {"eagle", "sparrow", "parrot"}
print(f"Birds: {birds}")
print(f"Are mammals and birds disjoint? {mammals.isdisjoint(birds)}") #mammalsกับbirds ไม่มีสมาชิกซ้ำกันใช่ไหม
print(f"Are pets and small_pets disjoint? {pets.isdisjoint(small_pets)}") 

# Set equality
pets_copy = {"dog", "cat", "rabbit"}
print(f"Are pets equal to pets_copy? {pets == pets_copy}")

# Length and membership
print(f"Number of mammals: {len(mammals)}")
print(f"Is 'dog' in mammals? {'dog' in mammals}")#ถ้าเราไม่รู้จักการใช้คำสั่งนี้ก็loopไปเลย
print(f"Is 'fish' in mammals? {'fish' in mammals}")