"""
Personal Finance Calculator
Student: Nichakamon Tapaohirun
Date: 27 July 2025
Purpose: Calculate monthly budget and savings
"""
monthly_income = float(input("Enter you monthly income in THB: ")) #รับค่าที่ผู้ใช้พิมพ์เข้ามา
rent_cost = float(input("Enter You Monthly rent/housing cost: ")) #รับค่าที่พักของผู้ใช
food_budget = int(input("Enter you Monthly food budget in THB  : ")) #รับค่ากินต่อเดือนของผู้ใช้
transportation_cost = float(input("Enter You  Monthly transportation expenses : ")) #รับค่าเดินทางต่อเดือนของผู้ใช้
entertainment_budget = int(input("Enter your Monthly entertainment budget: ")) #รับค่าพักผ่อนต่อเดือนของผู้ใช้
emergency_fund_percent = float(input("Enter Percentage to save for emergency: ")) #รับค่าปอร์เซ็นต์ที่ต้องการเก็บสำรองฉุกเฉิน
investment_percent = float(input("Enter Percentage to invest: "))#รับค่าเปอร์เซ็นต์ที่ต้องการลงทุน

#คำนวณค่าใช้จ่าย
total_fixed_expenses = rent_cost + transportation_cost #ค่าใช้จ่าย คงที่ = ค่าที่พัก + ค่าเดินทาง
total_variable_expenses = food_budget + entertainment_budget #ค่าใช้จ่าย ไม่คงที่ = ค่าอาหาร + ค่าพักผ่อนต่อเดือน
total_expenses = total_fixed_expenses + total_variable_expenses #ค่าใช้จ่าย ทั้งหมด = คงที่ + ไม่คงที่
remaining_income = monthly_income - total_expenses


#คำนวณเงินออมและการลงทุน
emergency_fund = monthly_income * (emergency_fund_percent / 100) #คำนวณเงินสำรองฉุกเฉินจากเปอร์เซ็นต์ที่ผู้ใช้กำหนด
investment_amount = monthly_income * (investment_percent / 100) #คำนวณเงินลงทุนจากเปอร์เซ็นต์
available_for_savings = remaining_income - emergency_fund - investment_amount #เงินที่เหลือ - เงินฉุกเฉิน - เงินลงทุน

#คำนวณสัดส่วนค่าใช้จ่ายเทียบกับรายได้ทั้งหมดเป็นเปอร์เซ็นต์
expense_ratio = (total_expenses / monthly_income) * 100

#แสดงผลลัพธ์
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

#แสดงเงินที่แบ่งเก็บเป็นฉุกเฉิน ลงทุน  ออมเพิ่ม
print(f"=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund({emergency_fund_percent:.0f}%): {emergency_fund_percent:.2f} THB")
print(f"Investment({investment_percent:.0f}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB\n")

#วิเคราะห์ว่าใช้เงินไปกี่เปอร์เซ็นต์จากรายได้ทั้งหมด
print(f"=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%\n")