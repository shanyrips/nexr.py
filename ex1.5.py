import functools


# Q1
with open("names.txt", "r") as file:
    print(max(name for name in file))


# Q2
with open("names.txt", "r") as file:
    print(sum([len(name.strip()) for name in file]))


# Q3
with open("names.txt", "r") as file:
    names = [(name.strip()) for name in file]
    min_len = len(min(names, key=len))
    [print(name) for name in names if len(name) == min_len]


# Q4
with open("names.txt", "r") as file, open("name_length.txt", "w") as length_file:
    lengths = "\n".join([str(len(name) - 1) for name in file])
    length_file.write(lengths)


# Q5
with open("names.txt", "r") as file:
    length = int(input("Enter name length: "))
    print("\n".join([name.strip() for name in file if len(name.strip()) == length]))

