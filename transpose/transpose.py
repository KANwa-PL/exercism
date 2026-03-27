from itertools import zip_longest

def transpose(text):
    lines = tuple(text.split('\n'))
    zipped_lines = [''.join(chars)for chars in zip_longest(*lines, fillvalue='$')]
    return '\n'.join(line.rstrip('$').replace('$',' ') for line in zipped_lines)