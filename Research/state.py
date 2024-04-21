states = [
    {'name': 'Texas', 'population': 29087070, 'age':3},
    {'name': 'California', 'population': 39512223, 'age': 2},
    {'name': 'Florida', 'population': 21477737, 'age':1}
]

print(states)
print("#####")
# Sort states by population
sorted_states = sorted(states, key=lambda x: x['age'])
print(sorted_states)
