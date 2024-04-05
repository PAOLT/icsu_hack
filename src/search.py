from typing import List
from pathlib import Path
from glob import glob
from random import sample
import os

class Search:
    def __init__(self, root_dir: str = './documents', pattern: str = '*.pdf') -> None:
        if not Path(root_dir).is_dir():
            raise ValueError(f"Directory {root_dir} does not exist.")
        
        self.documents = list(glob(f"{root_dir}/{pattern}"))
        self.max_docs = len(self.documents)
        

    def get_doc(self, ids: int) -> str:
        '''
            `ids`: the number of documents to return        
            return: a document path
        ''' 
        if ids < 0 or ids > len(self.documents):
            raise ValueError(f"Document ID {ids} is out of range.")
        
        return self.documents[ids]

    def dummy_search(self, query: str, num_doc: int = 3) -> List[int]:
        '''
            `query`: the user query

            `root_dir`: the root directory of the documents
            `num_doc`: the number of documents to return        
            return: a list of document IDs.
        '''
        num_doc = min(num_doc, self.max_docs)
        doc_ids = sample(list(range(self.max_docs)), num_doc)
        return doc_ids
