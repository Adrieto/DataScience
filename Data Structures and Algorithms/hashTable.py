"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        hash_value = self.calculate_hash_value(string)

        if self.table[hash_value] == None:
            self.table[hash_value] = string
        elif isinstance(self.table[hash_value], str):  # there's one non-None element
            self.table[hash_value] = [self.table[hash_value]] # the string is put inside a bucket -a list-
            (self.table[hash_value]).append(string)
        elif isinstance(self.table[hash_value], list): 
            (self.table[hash_value]).append(string)

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)

        # Search the string in the hash table

        if (
            isinstance(self.table[hash_value], str) and self.table[hash_value] == string
        ):  # If only one element exists and is the desired string
            return hash_value

        elif (
            isinstance(self.table[hash_value], list)
            and string in self.table[hash_value]
        ):
            return hash_value

        else:
            return -1 # The string is not in the hash table

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        ascii = [ord(i) for i in string[:2]]  # The ASCII values of the first 2 letters
        hash_value = int(str(ascii[0]) + str(ascii[1]))

        return hash_value


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print("Should be 8568: ", hash_table.calculate_hash_value("UDACITY"))

# Test lookup edge case
# Should be -1
print("Should be -1: ", hash_table.lookup("UDACITY"))

# Test store
hash_table.store("UDACITY")
# Should be 8568
print("Should be 8568: ", hash_table.lookup("UDACITY"))

# Test store edge case
hash_table.store("UDACIOUS")
# Should be 8568
print("Should be 8568: ", hash_table.lookup("UDACIOUS"))

print(hash_table.table[8568])
