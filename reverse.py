from __future__ import print_function
try:
    import readline
except ImportError:
    pass

def reverse_str(string):
    """Return the string with characters in reverse order."""
    lst = list(string)
    lst.reverse()
    return ''.join(lst)

if __name__ == '__main__':
    print(reverse_str(raw_input('Enter message to reverse: ')))
