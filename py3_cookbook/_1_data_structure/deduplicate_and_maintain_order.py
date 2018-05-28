""" Sample for removing duplicated elements in list and maintain original order """
import types

names = ['tom', 'ken', 'tim', 'mary', 'ken', 'ben', 'berry', 'mary']

# Use `set()` for easy deduplicate, but changes the order
print(set(names))


# Another approach: use loop with a customized hash function
def dedupe(items, hash_func=None):
    deduped_items = []
    seen_keys = set()
    for e in items:
        if hash_func is not None and isinstance(hash_func, types.FunctionType):
            key = hash_func(e)
        else:
            key = e

        if key not in seen_keys:
            seen_keys.add(key)
            deduped_items.append(e)
    return deduped_items


print(dedupe(names))  # No customized hash function, use the elements' default hash function directly

print(dedupe(names, lambda e: e[0]))  # Think them as duplicated if the 1st char is the same

print(dedupe(names, lambda e: e[-2:-1]))  # Think them as duplicated if the last 2 chars are the same
