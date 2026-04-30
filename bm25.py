# bm25.py — Implementasi BM25 dari prinsip pertama
# Nama : Hanief Fathul Bahri Ahmad
# NIM : ___________________________
import math
import re
from collections import defaultdict

def tokenize(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = text.split()
    return tokens


def build_index(corpus: dict) -> dict:
    """
    Bangun inverted index dan hitung statistik koleksi.
    Input : corpus = {doc_id: teks_dokumen}
    Output: dict berisi:
    index['tf']
     : {doc_id: {term: frekuensi}}
    index['df']
     : {term: jumlah_dokumen_yang_mengandung_term}
    index['dl']
     : {doc_id: panjang_dokumen}
    index['avgdl'] : float, rata-rata panjang dokumen
    index['N']
     : int, total jumlah dokumen
    index['docs'] : list of all doc_ids
    """
    # TODO: implementasi Anda di sini
    tf = {}  
    df = defaultdict(int)  
    dl = {}  
    docs = list(corpus.keys())  

    for doc_id, text in corpus.items():
        terms = tokenize(text)
        dl[doc_id] = len(terms)

        # temporary term frequency untuk dokumen ini
        term_freq = defaultdict(int)
        for term in terms:
            term_freq[term] += 1

        # term frekuensi 
        tf[doc_id] = dict(term_freq)

        # document frequency
        for term in term_freq:
            df[term] += 1

    # Hitung statistik
    N = len(docs)  
    avgdl = sum(dl.values()) / N if N > 0 else 0.0  

    return {
        "tf": tf,
        "df": dict(df),
        "dl": dl,
        "avgdl": avgdl,
        "N": N,
        "docs": docs,
    }



def compute_idf(term: str, N: int, df: dict) -> float:
    """
    Hitung IDF menggunakan formula Robertson-Jones.
    Formula: ln((N - df[term] + 0.5) / (df[term] + 0.5) + 1)
    Jika term tidak ada dalam df, kembalikan 0.
    """
    # TODO: implementasi Anda di sini
    if term not in df:
        return 0.0
    
    df_term = df[term]
    idf = math.log((N - df_term + 0.5) / (df_term + 0.5) + 1)
    return idf


def compute_bm25_score(query_terms: list, doc_id: str, index: dict, k1: float, b: float) -> float:
    """
    Hitung BM25 score untuk satu pasang (query, dokumen).
    Input : query_terms = list of tokens query
    doc_id = id dokumen target
    index = inverted index dari build_index()
    k1, b = parameter BM25
    Output: float, skor BM25
    """
    # TODO: implementasi Anda di sini
    score = 0.0
    doc_tf = index['tf'].get(doc_id, {})
    doc_len = index['dl'].get(doc_id, 0)
    
    for term in query_terms:
        idf = compute_idf(term, index['N'], index['df'])
        tf = doc_tf.get(term, 0)
        norm = 1 - b + b * (doc_len / index['avgdl']) if index['avgdl'] > 0 else 1
        score += idf * (tf * (k1 + 1)) / (tf + k1 * norm)
    
    return score

def rank(query: str, index: dict, k1: float = 1.5, b: float = 0.75) -> list:
    """
    Ranking seluruh dokumen untuk query tertentu.
    Input : query = string query
    index = inverted index
    Output: list of (doc_id, score) terurut descending by score
    """
    # TODO: implementasi Anda di sini
    query_terms = tokenize(query)

    scores = []
    for doc_id in index["docs"]:
        score = compute_bm25_score(query_terms, doc_id, index, k1, b)
        scores.append((doc_id, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores