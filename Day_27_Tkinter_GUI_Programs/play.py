def add(*args):
    sum = 0
    for n in args:
        sum += n

    print(sum)
    return  sum

add(2, 1, 7)

def calculate(**kwargs):
    print(kwargs)

calculate(add=2, multiply=5)


def f(char):
    return ord(char)

def h(s):
    p = 131
    M = 10**9 + 7
    n = len(s)
    hash_value = 0

    for i in range(n):
        hash_value = (hash_value * p + f(s[i])) % M

    return hash_value

def handle_events(events):
    current_password = ""
    current_hash = 0
    p = 131
    M = 10**9 + 7
    results = []

    for event in events:
        if event[0] == "setPassword":
            current_password = event[1]
            current_hash = h(current_password)

        elif event[0] == "authorize":
            x = event[1]

            # Check if x matches the current password hash
            if x == current_hash:
                results.append(1)
                continue

            # Check if x matches the hash of the current password with one character appended
            authorized = False
            power_p = 1
            for _ in range(len(current_password)):
                power_p = (power_p * p) % M

            for ascii_value in range(32, 127):  # Check for valid ASCII characters
                appended_hash = (current_hash * p + ascii_value) % M
                if appended_hash == x:
                    authorized = True
                    break

            results.append(1 if authorized else 0)

    return results

# Example usage:
events = [
    ("setPassword", "cAr1"),
    ("authorize", 223691457),
    ("authorize", 303580761),
    ("authorize", 100),
    ("setPassword", "d"),
    ("authorize", 100)
]

print(handle_events(events))
