from src import *

if __name__ == '__main__':
    search = Search()
    cache = Cache()
    preprocessor = Preprocessor()
    prompting = Prompting()

    query = input("Enter a query: ")

    doc_ids = search.dummy_search(query, num_doc=3)
    docs_in_cache = cache.check_cache(doc_ids)

    for in_cache, doc_id in zip(docs_in_cache, doc_ids):
        if in_cache:
            continue

        doc = search.get_doc(doc_id)
        docs = preprocessor.preprocess_doc(doc)
        for i, d in enumerate(docs):
            emb = get_embedding(d)
            state = cache.store_cache(doc_id, d, emb)
            print(f"Document {i}/{doc_id} stored in the cache - {state}")
    
    q_emb = get_embedding(query)
    docs = cache.search_cache(q_emb)
    answer = prompting.ask(query, docs)
    print(answer)