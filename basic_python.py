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
    """
    message_str = str(message)
    if not message_str:
        return 1  # Successfully formed the message
    if not fragments:
        return 0
    occurrences = 0
    for i, f in enumerate(fragments):
        frag_str = str(f)
        if message_str.startswith(frag_str):
            new_fragments = fragments[:i] + fragments[i+1:]
            remainder = message_str[len(frag_str):]
            if remainder == '':
                occurrences += 1
            else:
                occurrences += count_fragment_combinations(new_fragments, int(remainder))
    return occurrences

# The tests have been moved to test_basic_python.py for better structure and maintainability.





