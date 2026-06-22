class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        hashtable to keep track of character frequencies
        sliding window
        lbound rbound start as 0 and 1 where s[lbound:rbound] is just the first character
        insert that first character with frequency 1 into hashtable

        increase bound2 and add the new character or if its the same character update hashtable
        make sure that the hashtable is only two keys in length at any time
        once a third character is found via bound2, increase bound1 until two characters in substring

        all the while keeping track of a longest int which is then returned.
        update longest when he has
        """

        """
        hashtable stores frequencies of characters in current window

        expand rbound

        keep track of the frequency of the most common character in the window

        window size = rbound - lbound + 1

        replacements needed =
        window size - max_frequency

        if replacements needed > k:
            shrink from the left

        otherwise:
            update longest
        """

        hashtable = {}
        n = len(s)

        lbound, rbound = 0, 1
        max_freq = 0
        longest = 0

        while rbound <= n:
            window_size = rbound - lbound

            if s[rbound - 1] not in hashtable:
                hashtable[s[rbound - 1]] = 1
            else:
                hashtable[s[rbound - 1]] += 1

            max_freq = max(max_freq, hashtable[s[rbound - 1]])

            num_replacements = window_size - max_freq

            if num_replacements > k:
                lbound += 1
            else:
                longest = window_size
            
            rbound += 1

        return longest
            
            

