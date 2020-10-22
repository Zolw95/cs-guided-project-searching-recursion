"""
You are a new author that is working on your first book. You are working on a
series of drafts. Each draft is based on the previous draft. The latest draft
of your book has a serious typo. Since each newer draft is based on the
previous draft, all the drafts after the draft containing the typo also include
the typo.

Suppose you have `n` drafts `[1, 2, 3, ..., n]` and you need to find out the
first one containing the typo (which causes all the following drafts to have
the typo as well).

You are given access to an API tool `containsTypo(draft)` that will return
`True` if the draft contains a typo and `False` if it does not.

You need to implement a function that will find the *first draft that contains
a typo*. Also, you have to pay a fee for every call to `containsTypo()`, so
make sure that your solution minimizes the number of API calls.

Example:

Given `n = 5`, and `draft = 4` is the first draft containing a typo.

containsTypo(3) -> False
containsTypo(5) -> True
containsTypo(4) -> True
"""
def firstDraftWithTypo(n):
    # Your code here
    #[draft1, draft2, draft3, ... draftn-1, draft n]

    # If we find a draft with the typo, the first draft with the typo (target) is before the current draft
    # If current draft does not have the typo, the first drag w/ the typo is after the current draft
    min = 0
    max = n

    while not max <= min:  
        guess = min + max // 2
        contains_typo = contains_typo(guess)

        if contains_typo:
            # The first draft w/ the typo is before our guess
            # look left
            # we could check if its the first one by calling containsTypo (guess - 1)
            # move max to the guess value
            max = guess
        else:
            # look right
            # move min to guess + 1
            min = guess + 1
        # repeat
    return min


