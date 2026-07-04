#Without module coounter
'''

words = ["apple", "banana", "apple",
"mango", "banana", "apple"]
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
'''

#with module counter 
'''from collections import Counter
words = ["apple", "banana", "apple",
"mango", "banana", "apple"]
print(Counter(words))'''


#counter
'''from collections import Counter
numbers = [1, 2, 2, 3, 3, 3, 4]
c = Counter(numbers)
print(c)
# Counter({3: 3, 2: 2, 1: 1, 4: 1})
# Count letters in a string
name = "banana"
print(Counter(name))
# Counter({'a': 3, 'n': 2, 'b': 1}v'''

#error in defaultdict
'''student = {}
student["Math"] += 1

print(student)'''

#using defaultdict
'''from collections import defaultdict
# defaultdict with int as default factory
student = defaultdict(int)
student["Math"] += 1
print(student)
# defaultdict(, {'Math': 1}'''


#deque
'''from collections import deque
d = deque([10, 20, 30])
# Add to right end
d.append(40)
print(d)  # deque([10, 20, 30, 40])
# Add to left end
d.appendleft(5)
print(d)  # deque([5, 10, 20, 30, 40])
# Remove from right
d.pop()       # returns 40
print(d)  # deque([10, 20, 30])'''

#orderdict
'''from collections import OrderedDict
d = OrderedDict()
d["A"] = 10
d["B"] = 20
d["C"] = 30
print(d)
# OrderedDict([('A', 10), ('B', 20), ('C', 30)])
# Move item to end
d.move_to_end("A")
print(d)'''
# OrderedDict([('B', 20), ('C', 30), ('A', 10)]


#Chainmap
"""from collections import ChainMap
d1 = {"name": "Kanak"}
d2 = {"age": 20}
d3 = {"course": "BCA"}
c = ChainMap(d1, d2, d3)
print(c["name"])   # Kanak
print(c["age"])    
# 20
print(c["course"]) # BCA
# First dict takes priority
d1["age"] = 25
print(c["age"])    
# 25 (from d1, not d2"""

import sys
print(sys.executable)
print(sys.version)
"""from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.responses.create(
    model="gpt-5.5",
    input="Analyze this URL: https://example.com"
)

print(response.output_text)"""