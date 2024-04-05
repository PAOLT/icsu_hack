from typing import List

class Preprocessor:

    def __init__(self) -> None:
        pass

    def _to_md(self, path:str) -> str:
        '''
            `path`: the local path to a document
            return: the markdown representation of the document
        ''' 
        # HINT: look into the Azure Document Intelligence API, using the layout model
        
        return "Hello World!"
    
    def _clean(self, text: str) -> str:
        '''
            `path`: the local path to a document
            return: the cleaned text of the document
        '''
        return "Hello World!"
    
    def _split(self, text: str) -> List[str]:
        '''
            `text`: the text to split
            return: a list of chunks
        '''
        return ["Chunk1", "Chunk2", "Chunk3"]
    
    def preprocess_doc(self, path:str) -> List[str]:
        '''
            `path`: the local path to a document
            return: a list of chunks
        '''
        txt = self._to_md(path)
        txt = self._clean(txt)
        txts = self._split(txt)
        return txts
