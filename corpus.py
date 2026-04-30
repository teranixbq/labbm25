CORPUS = {
"D1": "mesin pencari menggunakan algoritma untuk merangking dokumen berdasarkan relevansi query pengguna",
"D2": "BM25 adalah algoritma ranking probabilistik yang digunakan dalam sistem information retrieval modern",
"D3": "Google dan Bing menggunakan berbagai teknik ranking termasuk machine learning dan neural network",
"D4": "inverted index adalah struktur data utama dalam sistem information retrieval untuk pencarian cepat",
"D5": "TF-IDF mengukur pentingnya sebuah term dalam dokumen relatif terhadap seluruh koleksi dokumen",
"D6": "BERT dan transformer digunakan dalam neural information retrieval untuk memahami semantik query",
"D7": "evaluasi sistem retrieval menggunakan metrik seperti precision recall MAP dan NDCG",
"D8": "query expansion meningkatkan recall dengan menambahkan term sinonim ke dalam query original",
}

QUERIES = {
"Q1": "algoritma ranking dokumen",
"Q2": "evaluasi information retrieval",
"Q3": "neural network search engine",
}

# Relevance judgments: {query_id: {doc_id: relevance_score}}
# Skala: 0=tidak relevan, 1=relevan, 2=sangat relevan

QRELS = {
"Q1": {"D1": 1, "D2": 2, "D3": 0, "D4": 1, "D5": 1, "D6": 0, "D7": 0, "D8": 0},
"Q2": {"D1": 0, "D2": 0, "D3": 0, "D4": 0, "D5": 1, "D6": 0, "D7": 2, "D8": 1},
"Q3": {"D1": 0, "D2": 0, "D3": 2, "D4": 0, "D5": 0, "D6": 2, "D7": 0, "D8": 0},
}