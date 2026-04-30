# evaluation.py — Metrik evaluasi NDCG
# Nama : Hanief Fathul Bahri Ahmad
# NIM : ___________________________

import math

def compute_dcg(ranked_list: list, qrels: dict, k: int) -> float:
    """
    Hitung DCG@k.
    Input : ranked_list = [(doc_id, score), ...] terurut descending
    qrels = {doc_id: relevance_score} untuk query ini
    k = cut-off depth
    Output: float, nilai DCG@k
    """
    # TODO: implementasi Anda di sini
    dcg = 0.0
    ranked_selected = ranked_list[:k]
    for i, (doc_id, _) in enumerate(ranked_selected, start = 1):
        rel = qrels.get(doc_id, 0)
        dcg_sum = rel / math.log2(i + 1)
        dcg += dcg_sum
    return dcg
    

def compute_idcg(qrels: dict, k: int) -> float:
    """
    Hitung IDCG@k (DCG ideal / perfect ranking).
    Input : qrels = {doc_id: relevance_score}
    k = cut-off depth
    Output: float, nilai IDCG@k
    """
    # TODO: implementasi Anda di sini
    idcg = 0.0

    sorted_rels = sorted(qrels.items(), key=lambda x: x[1], reverse=True)
    sorted_selected = sorted_rels[:k]

    for index, (_,rel_value) in  enumerate(sorted_selected,start=1):
        idcg_sum = rel_value / math.log2(index + 1)
        idcg += idcg_sum
    return idcg


def compute_ndcg(ranked_list: list, qrels: dict, k: int) -> float:
    """
    Hitung NDCG@k = DCG@k / IDCG@k.
    Kembalikan 0.0 jika IDCG = 0.
    """
    # TODO: implementasi Anda di sini
    ndcg = 0.0
    dcg = compute_dcg(ranked_list,qrels, k)
    idcg = compute_idcg(qrels, k)

    if idcg == 0 or idcg == 0.0:
        return 0.0
    else:
        ndcg = dcg / idcg
        return ndcg