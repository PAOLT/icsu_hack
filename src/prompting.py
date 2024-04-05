from typing import List

class Prompting:
    def __init__(self, system: str = None, max_tokens: int = 2064):
        self.system = system or "You are a useful bot helping people find information."
        self.max_tokens = max_tokens

    
    def _get_context(self, txts: List[str]) -> str:
        '''
            `txts`: a list of document texts
            `max_tokens`: the maximum number of tokens to return
            return: a concatenated string of document texts
        '''
        txt = '\n\n'.join(txts)
        # is txt too many tokens?
        return txt
    
    def _compile_prompt(self, query: str, context: str = None) -> str:
        '''
            `query`: the user query 
            `context`: the context of the query
            return: a compiled prompt
        '''
        prompt = self.system + '\n\n' + context + '\n\n' + query
        return prompt
    
    def _ask(self, prompt: str) -> str:
        '''
            `prompt`: the prompt to ask
            return: the response from a LLM
        '''
        # send prompt to a LLM
        return prompt
    
    def ask(self, query: str, txts: List[str]) -> str:
        '''
            `query`: the user query
            `txts`: a list of document texts
            return: the response from a LLM
        '''
        context = self._get_context(txts)
        prompt = self._compile_prompt(query, context)
        return self._ask(prompt)
    


