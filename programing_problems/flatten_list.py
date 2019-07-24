def flatten(lst):
    result = []
    for elem in lst:
         if not isinstance(elem, list):
            result.append(elem)
         else:
            result.extend(flatten(elem))
    return result


def iter_flatten(iterable):
  it = iter(iterable)
  for e in it:
    if isinstance(e, (list, tuple)):
      for f in iter_flatten(e):
        yield f
    else:
      yield e

test_case = ['a', [], ['a', 'b', 'c', []], ['a', 'b', 'c', ['a','b','c', 'd', 'e', 'f']]]

print(flatten(test_case))
results = [i for i in iter_flatten(test_case)]
print(results)
