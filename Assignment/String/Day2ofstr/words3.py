"""
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
"""
"""complaint = input("Enter complaint: ")
count=0
words = complaint.split()
for word in words:
    count=count+1
print("Total words ",count)
"""

complaint = input("Enter complaint: ")
count=1
for word in complaint:
    if word==' ':
        count=count+1
print(count)