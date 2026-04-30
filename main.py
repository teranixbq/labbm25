# main.py — Runner utama Lab 1
from corpus import CORPUS, QUERIES, QRELS
from bm25 import build_index, rank
from evaluation import compute_ndcg

def main():
    index = build_index(CORPUS)
    print(f'Koleksi: {index["N"]} dokumen | avgdl = {index["avgdl"]:.2f}token\n')

    for qid, query_text in QUERIES.items():
        print(f'=== {qid}: "{query_text}" ===')
        results = rank(query_text, index) 
        qrels = QRELS[qid]
        print(f' {'Rank':<6} {'Doc':<5} {'BM25 Score':<14} {'Relevansi'}')
        print(f' {"-"*40}')
        for i, (doc_id, score) in enumerate(results, 1):
            rel = qrels.get(doc_id, 0)
            print(f' {i:<6} {doc_id:<5} {score:<14.4f} {rel}')
            for k in [3, 5, 10]:
                ndcg = compute_ndcg(results, qrels, k)
                print(f' NDCG@{k} = {ndcg:.4f}')
                print()

if __name__ == '__main__':
    main()