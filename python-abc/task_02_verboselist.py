#!/usr/bin/python3


class VerboseList(list):
    def append(self, obj):
        super().append(obj)
        print(f"Added [{obj}] to the list.")

    def extend(self, nb):
        super().extend(nb)
        print(f"Extended the list with [{len(nb)}] items.")

    def remove(self, obj):
        print(f"Removed [{obj}] from the list.")
        super().remove(obj)

    def pop(self, idx=None):
        if idx is None:
            idx = -1
        try:
            value = self[idx]
        except IndexError:
                raise
        print(f"Popped [{self[idx]}] from the list.")
        return super().pop(idx)
