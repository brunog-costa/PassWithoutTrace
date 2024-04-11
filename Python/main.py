'''
Put your super important code implementation here
'''

def roll_dice(num_faces, num_rolls):
    total = 0
    print(f"Rolling {num_rolls} dice with {num_faces} faces:")
    for i in range(num_rolls):
        roll_result = random.randint(1, num_faces)
        total += roll_result
        print(f"Roll {i+1}: {roll_result}")
    print(f"Total: {total}")

# Example usage:
num_faces = int(input("Enter the number of faces on the dice: "))
num_rolls = int(input("Enter the number of rolls: "))
roll_dice(num_faces, num_rolls)
