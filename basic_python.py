# basic_python.py

# Problem: Given a list of integer fragments and a target integer message, count how many ways you can concatenate (not add) some of the fragments (in any order and using each at most once) to form the message as an integer. Do not implement the solution yet.

def count_fragment_combinations(fragments, message):
    """
    Given a list of integer fragments and a target integer message, count how many ways you can concatenate some of the fragments (in any order, using each at most once) to form the message.
    For example, fragments = [1, 23, 4], message = 1234
    Possible combinations: [1, 23, 4] => 1|23|4 = 1234
    Return the count of such combinations.
    """
    pass  # TODO: Implement the solution

def test_count_fragment_combinations():
    # Test 1: Example from docstring
    fragments = [1, 23, 4]
    message = 1234
    assert count_fragment_combinations(fragments, message) == 1

    # Test 2: Multiple ways
    fragments = [12, 3, 4, 123, 34]
    message = 1234
    # Possible: [12, 34], [123, 4], [1, 23, 4]
    # But [1, 23, 4] not possible since 1 not in fragments
    assert count_fragment_combinations(fragments, message) == 2

    # Test 3: No possible combinations
    fragments = [5, 6, 7]
    message = 123
    assert count_fragment_combinations(fragments, message) == 0

    # Test 4: Fragments can only be used once
    fragments = [1, 1, 2]
    message = 112
    assert count_fragment_combinations(fragments, message) == 2  # [1,1,2] (two ways to pick the 1s)

    # Test 5: Empty fragments
    fragments = []
    message = 1
    assert count_fragment_combinations(fragments, message) == 0

if __name__ == "__main__":
    test_count_fragment_combinations()
    print("All tests passed.")

print("Hello, Coding Dojo!")
for i in range(5):
    print(f"Number {i}")



