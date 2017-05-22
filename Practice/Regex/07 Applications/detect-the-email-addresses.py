import re

EMAIL_RE = re.compile(r'\w+(?:\.\w+)*@\w+(?:\.\w+)+')

def get_emails(text):
    return set(EMAIL_RE.findall(text))

if __name__ == '__main__':
    n = int(input())
    text = '\n'.join(input() for _ in range(n))
    
    emails = get_emails(text)
    print(';'.join(sorted(emails)))
