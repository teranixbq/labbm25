# evaluation.py — Metrik evaluasi NDCG
# Nama : Hanief Fathul Bahri Ahmad
# NIM : ___________________________

import math

def compute_dcg(ranked_list: list, qrels: dict, k: int) -> float:
    """
    Hitung DCG@k.
    Input : ranked_list = [(doc_id, score), ...] terurut descending
    qrels
    = {doc_id: relevance_score} untuk query ini
    k
    = cut-off depth
    Output: float, nilai DCG@k
    """
    # TODO: implementasi Anda di sini
    pass

def compute_idcg(qrels: dict, k: int) -> float:
    """
    Hitung IDCG@k (DCG ideal / perfect ranking).
    Input : qrels = {doc_id: relevance_score}
    k
    = cut-off depth
    Output: float, nilai IDCG@k
    """
    # TODO: implementasi Anda di sini
    pass

def compute_ndcg(ranked_list: list, qrels: dict, k: int) -> float:
    """
    Hitung NDCG@k = DCG@k / IDCG@k.
    Kembalikan 0.0 jika IDCG = 0.
    """
    # TODO: implementasi Anda di sini
    pass