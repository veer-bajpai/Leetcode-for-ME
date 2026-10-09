from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
            
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:len(s1)])
        
        if s1_counts == window_counts:
            return True
            
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add the new character entering from the right
            window_counts[s2[i]] += 1
            
            # Remove the character leaving from the left
            left_char = s2[i - len(s1)]
            window_counts[left_char] -= 1
            if window_counts[left_char] == 0:
                del window_counts[left_char] # Clean up to allow direct dictionary comparison
                
            # Check if the counts match
            if s1_counts == window_counts:
                return True
                
        return False
