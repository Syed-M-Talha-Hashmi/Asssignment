#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
person = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore",
    "hobbies": ["reading", "cricket", "gaming"]
}

print(person)


# In[7]:


#Q2
text = "this is a test this is simple"

words = text.split()
freq = {}

for word in words:
    freq[word] = words.count(word)

print(freq)


# In[8]:


#Q3
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

#adding inventory 
inventory["banana"] += 3

print(inventory)


# In[12]:


#Q4
orders = [
    {"category": "FMCGs"},
    {"category": "clothing"},
    {"category": "electronics"},
    {"category": "books"},
    {"category": "electronics"},
    {"category": "books"}
]

count = {}

for order in orders:
    cat = order["category"]
    if cat in count:
        count[cat] += 1
    else:
        count[cat] = 1

most_popular = max(count, key=count.get)

print("Most popular:", most_popular)


# In[13]:


#Q5
grades = {
    "Ali": [80, 90, 85],
    "Sara": [70, 75, 80],
    "Ahmed": [90, 95, 92]
}

for student in grades:
    avg = sum(grades[student]) / len(grades[student])
    print(student, "average:", avg)


# In[14]:


inventory = {}

def add_product(name, qty, price):
    inventory[name] = {"quantity": qty, "price": price}

def update_quantity(name, qty):
    if name in inventory:
        inventory[name]["quantity"] = qty

def total_value():
    total = 0
    for item in inventory:
        total += inventory[item]["quantity"] * inventory[item]["price"]
    return total

def low_stock(threshold=5):
    for item in inventory:
        if inventory[item]["quantity"] < threshold:
            print("Low stock:", item)

# Example usage
add_product("apple", 10, 50)
add_product("banana", 3, 30)

update_quantity("banana", 2)

print("Total value:", total_value())
low_stock()


# In[15]:


students = {
    "Ali": {"math": 80, "english": 70},
    "Sara": {"math": 90, "english": 85},
    "Ahmed": {"math": 60, "english": 75}
}

# average grade
averages = {}
for name in students:
    scores = students[name].values()
    avg = sum(scores) / len(scores)
    averages[name] = avg
    print(name, "average:", avg)

# highest & lowest in math
math_scores = {name: students[name]["math"] for name in students}

highest = max(math_scores, key=math_scores.get)
lowest = min(math_scores, key=math_scores.get)

print("Highest in math:", highest)
print("Lowest in math:", lowest)

# sort by average
sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)
print("Sorted:", sorted_students)


# In[ ]:


store = {
    "apple": {"price": 50, "quantity": 10},
    "banana": {"price": 30, "quantity": 20}
}

cart = {}

def add_to_cart(item, qty):
    if item in store and store[item]["quantity"] >= qty:
        cart[item] = cart.get(item, 0) + qty
        store[item]["quantity"] -= qty

def remove_from_cart(item):
    if item in cart:
        store[item]["quantity"] += cart[item]
        del cart[item]

def total_cost():
    total = 0
    for item in cart:
        total += cart[item] * store[item]["price"]
    return total

def apply_discount_tax(total, discount=0.1, tax=0.05):
    total -= total * discount
    total += total * tax
    return total

# Example
add_to_cart("apple", 2)
add_to_cart("banana", 3)

total = total_cost()
final = apply_discount_tax(total)

print("Cart:", cart)
print("Total:", total)
print("Final with discount & tax:", final)

