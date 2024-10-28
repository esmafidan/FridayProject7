# Prompt the player for input
large_object = input("Enter a large object: ")
large_objects = input("Enter large objects (plural): ")
adjective = input("Enter an adjective: ")
body_part = input("Enter a body part: ")
restaurant = input("Enter a restaurant name: ")
food1 = input("Enter a food: ")
food2 = input("Enter another food: ")

# Combine the player's inputs into the story template
story = f"I’ve had a very {adjective} day.\n" \
        f"This morning, I dropped a box of {large_objects} on my {body_part}.\n" \
        f"Then, at lunch, I went to {restaurant} for their delicious {food1},\n" \
        f"But the waiter brought me {food2}, which I was not hungry for.\n" \
        f"Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."

# Print the completed story
print(story)