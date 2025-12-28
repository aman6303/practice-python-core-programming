file = open('youtube.txt', 'w')

# two basic way of openning file
# Example 1

try:
    file.write("hello from youtube manager")
finally:
    file.close()
    
# Example 2
with open('youtube.txt', 'w') as file:
    file.write("chai aur python")