import pickledb


def sum_values_of_2_dicts(d1, d2):
    result = {}
    for key in d1.keys():
        result[key] = d1[key] + d2[key]
    return result


class PickleDBHandler:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = pickledb.load(self.db_path, False)

    def get(self, key):
        """
        Return value of record with a specific key.
        """
        return self.db.get(key)

    def set(self, key, value):
        """
        Save value to specific key.
        """
        self.db.set(key, value)
        self.db.dump()

    def delete(self, key):
        """
        Delete record with specific key.
        """
        self.db.rem(key)
        self.db.dump()

    def get_all(self):
        """
        Return all records in db.
        """
        return list(self.db.getall())

    def add_2_dicts_in_db(self, key, d2):
        d1 = self.get(key)
        if d1 is None:
            return "Error - key not found"
        result = sum_values_of_2_dicts(d1, d2)
        self.set(key, result)
