import time
def only_vowels(s):
    return ''.join([c for c in s if c.lower() in 'aeiou'])

start_time = time.time()
print("\n".join(c for c in "01234")+ "\n\n"+ "\n".join(str(c) for c in range(5)))
print(time.time()-start_time)

#countdown
for i in range(10,0,-1):
    print(i)
print()
#even numbers
for i in range(0, 10, 2):
    print(i)
print()
#get index and value
for index, char in enumerate("abcde"):
    print(f"At position {index} we have character {char}")
    
def count_vowels(string):
    return len(only_vowels(string))

