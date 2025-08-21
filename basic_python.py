# basic_python.py

# Problem: Given a list of integer fragments and a target integer message, count how many ways you can concatenate (not add) some of the fragments (in any order and using each at most once) to form the message as an integer. Do not implement the solution yet.

def equal_start(fragment, message):
    """
    Check if the fragment starts with the same digits as the message.
    """
    return str(message).startswith(str(fragment))

def count_fragment_combinations(fragments, message):
    """
    Given a list of integer fragments and a target integer message, count how many ways you can concatenate some of the fragments (in any order, using each at most once) to form the message.
    For example, fragments = [1, 23, 4], message = 1234
    Possible combinations: [1, 23, 4] => 1|23|4 = 1234
    Return the count of such combinations.
    """
    occurences = 0

    for f in fragments:
        if equal_start(f, message):
            if f == message:
                occurences += 1
            else:
                new_fragments = fragments.copy()
                new_fragments.remove(f)
                occurences += count_fragment_combinations(new_fragments, int(str(message)[len(str(f)):]))

    return occurences

# The tests have been moved to test_basic_python.py for better structure and maintainability.





