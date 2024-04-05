from typing import List
import numpy as np 

class Cache:

    def __init__(self) -> None:
        pass

    def check_cache(self, docs: List[int]) -> List[bool]:
        '''
            `docs`: a list of document IDs
            return: a list of boolean values indicating whether the document is in the cache or not
        '''
        return [False for _ in docs]
    
    def store_cache(self, id: int, text: str, embedding: np.ndarray) -> bool:
        '''
            `id`: the document ID   
            `text`: the document text
            `embedding`: the document embeddings
            return: a boolean value indicating whether the document was stored in the cache or not
        '''
        return True

    def search_cache(self, q_embedding: np.ndarray, k: int = 3) -> List[str]:
        '''
            `q_embedding`: the query embedding
            `k`: the number of documents to return
            return: a list of document texts
        ''' 
        return ["Hello document!"] * k