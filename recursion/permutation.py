string = "abc"  # abc, acb, bac, bca, cab, cba


def permutation(s):
    out = []

    # base case
    if len(s) == 1:
        out = [s]
    else:
        for i, e in enumerate(s):
            for perm in permutation(s[:i] + s[i+1:]):
                out += [e + perm]
    return out


print(permutation(string))
