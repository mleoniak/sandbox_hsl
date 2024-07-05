class Helpers:

    @staticmethod
    def has_common_substring(str1, str2):
        # Convert both strings to sets of words
        set1 = set(str1.split())
        set2 = set(str2.split())

        # Find intersection of sets (common words)
        common_words = set1.intersection(set2)

        # Check if there's at least one common word
        return len(common_words) > 0
