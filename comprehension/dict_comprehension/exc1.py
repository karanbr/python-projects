sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
# words = sentence.split()
# print(words)
result = {
    word: len(word) for word in sentence.split()
}

print(result)
