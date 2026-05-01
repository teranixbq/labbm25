# main.py — Runner utama Lab 1
from corpus import CORPUS, QUERIES, QRELS
from bm25 import build_index, rank
from evaluation import compute_ndcg
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator

def main():
    all_results = {}
    index = build_index(CORPUS) 
    print(f'Koleksi: {index["N"]} dokumen | avgdl = {index["avgdl"]:.2f} token\n') 
 
    for qid, query_text in QUERIES.items(): 
        print(f'=== {qid}: "{query_text}" ===') 
        results = rank(query_text, index) 
        qrels   = QRELS[qid] 
        all_results[qid] = results
 
        print(f'  {'Rank':<6} {'Doc':<5} {'BM25 Score':<14} {'Relevansi'}') 
        print(f'  {"-"*40}') 
        for i, (doc_id, score) in enumerate(results, 1): 
            rel = qrels.get(doc_id, 0) 
            print(f'  {i:<6} {doc_id:<5} {score:<14.4f} {rel}') 
 
        for k in [3, 5, 10]: 
            ndcg = compute_ndcg(results, qrels, k) 
            print(f'  NDCG@{k} = {ndcg:.4f}') 
        print() 

    matplotlib_bar_chart(all_results)


# Fungsi untuk membuat bar chart menggunakan matplotlib menggunakan tight_layout
def matplotlib_bar_chart(all_results):
    if plt is None:
        print("matplotlib tidak tersedia.")
        return

    qids = list(all_results.keys())
    if not qids: #kalau kosong gagal buat chart
        print("Tidak ada hasil untuk ditampilkan.")
        return

    fig, axes = plt.subplots(len(qids), 1, figsize=(12, 4 * len(qids)))
    if len(qids) == 1:
        axes = [axes]

    for ax, qid in zip(axes, qids):
        results = all_results[qid]
        docs = [doc_id for doc_id, _ in results]
        scores = [score for _, score in results]

        ax.bar(docs, scores)
        ax.set_title(f"{qid}\n{QUERIES[qid]}")
        ax.set_xlabel("Dokumen")
        ax.set_ylabel("BM25 Score")
        ax.yaxis.set_major_locator(MultipleLocator(0.5))
        ax.yaxis.set_major_formatter(FormatStrFormatter("%.1f"))

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()