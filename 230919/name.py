def sort_key(dictionary):
    return dictionary['name']

people = [
    {'name': 'Homer', 'age': 39},
    {'name': 'Bart', 'age': 10},
    {'name': 'Lisa', 'age': 8}
]

# Sort the list by the 'name' key in ascending order
sorted_people = sorted(people, key=sort_key)
print(sorted_people)
# Output: [{'name': 'Bart', 'age': 10}, {'name': 'Homer', 'age': 39}, {'name': 'Lisa', 'age': 8}]

# Sort the list by the 'age' key in descending order
people.sort(key=sort_key, reverse=True)
print(people)
# Output: [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}, {'name': 'Lisa', 'age': 8}]