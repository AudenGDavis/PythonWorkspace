from typing import Dict, List

def find_repeat_dict(import_str: str) -> Dict[str,int]:
    '''fuck off'''

    word_counts: Dict[str,int] = {}

    for word in import_str.split():
        word_counts[word] = word_counts.get(word,0) + 1
    
    return word_counts
            
