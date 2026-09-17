def countdown(count):
    print(f"Counting down: {count}")
    # Base case missing (e.g., if count == 0: return)
    countdown(count - 1)

countdown(3)