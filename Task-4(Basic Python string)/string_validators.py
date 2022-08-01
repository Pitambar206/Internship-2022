# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.


if __name__ == '__main__':
    S =input()
    print(any(char.isalnum() for char in S))
    print(any(char.isalpha() for char in S))
    print(any(char.isdigit() for char in S))
    print(any(char.islower() for char in S))
    print(any(char.isupper() for char in S))