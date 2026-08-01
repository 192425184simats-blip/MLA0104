from itertools import permutations

# Input
word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
word3 = input("Enter third word: ").upper()
word4 = input("Enter fourth word: ").upper()
result = input("Enter result word: ").upper()

# Collect unique letters
letters = []
for ch in word1 + word2 + word3 + word4 + result:
    if ch not in letters:
        letters.append(ch)

if len(letters) > 10:
    print("More than 10 unique letters. No solution possible.")
    exit()

# Leading letters cannot be zero
first_letters = {word1[0], word2[0], word3[0], word4[0], result[0]}

for perm in permutations(range(10), len(letters)):
    mapping = dict(zip(letters, perm))

    if any(mapping[ch] == 0 for ch in first_letters):
        continue

    def value(word):
        return int("".join(str(mapping[ch]) for ch in word))

    n1 = value(word1)
    n2 = value(word2)
    n3 = value(word3)
    n4 = value(word4)
    ans = value(result)

    if n1 + n2 + n3 + n4 == ans:
        print("\nSolution Found")
        for ch in letters:
            print(ch, "=", mapping[ch])

        print("\nVerification:")
        print(n1)
        print(n2)
        print(n3)
        print(n4)
        print("------ +")
        print(ans)
        break
else:
    print("No solution found.")


