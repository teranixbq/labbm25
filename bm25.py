# bm25.py — Implementasi BM25 dari prinsip pertama
# Nama : Hanief Fathul Bahri Ahmad
# NIM : ___________________________
import math
import re
from collections import defaultdict

from corpus import CORPUS

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
    tf = {}  # term frequency per dokumen
    df = defaultdict(int)  # document frequency per term
    dl = {}  # panjang dokumen
    docs = list(corpus.keys())  # list semua doc_id

    # Loop setiap dokumen di corpus
    for doc_id, text in corpus.items():
        # Tokenisasi teks dokumen
        terms = tokenize(text)
        # Simpan panjang dokumen
        dl[doc_id] = len(terms)

        # Hitung term frequency di dokumen ini
        term_freq = defaultdict(int)
        for term in terms:
            term_freq[term] += 1

        # Simpan tf untuk dokumen ini
        tf[doc_id] = dict(term_freq)

        # Update df: catat term mana saja yang ada di dokumen ini
        for term in term_freq:
            df[term] += 1

    # Hitung statistik koleksi
    N = len(docs)  # total dokumen
    avgdl = sum(dl.values()) / N if N > 0 else 0.0  # rata-rata panjang

    return {
        "tf": tf,
        "df": dict(df),
        "dl": dl,
        "avgdl": avgdl,
        "N": N,
        "docs": docs,
    }

print(build_index(CORPUS))



def compute_idf(term: str, N: int, df: dict) -> float:
    # Hitung IDF menggunakan formula Robertson-Jones.
    # Formula: ln((N - df[term] + 0.5) / (df[term] + 0.5) + 1)
    # Jika term tidak ada dalam df, kembalikan 0.
    # TODO: implementasi Anda di sini
    if term not in df:
        return 0.0
    
    df_term = df[term]
    idf = math.log((N - df_term + 0.5) / (df_term + 0.5) + 1)
    return idf

def compute_bm25_score(query_terms: list, doc_id: str,
    index: dict, k1: float, b: float) -> float:
    """
    Hitung BM25 score untuk satu pasang (query, dokumen).
    Input : query_terms = list of tokens query
    doc_id
    = id dokumen target
    index
    = inverted index dari build_index()
    k1, b
    = parameter BM25
    Output: float, skor BM25
    """
    # TODO: implementasi Anda di sini
    pass

def rank(query: str, index: dict,
    k1: float = 1.5, b: float = 0.75) -> list:
    """
    Ranking seluruh dokumen untuk query tertentu.
    Input : query = string query
    index = inverted index
    Output: list of (doc_id, score) terurut descending by score
    """
    # TODO: implementasi Anda di sini
    pass