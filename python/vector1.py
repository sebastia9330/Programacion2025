from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-l6-v2")
texto = "Sebastian Carrero"
vector = model.encode(texto)
print(vector[:10])

frase2 = "sebastian nacio en 1993"
v2 = model.encode(frase2)
sim = model.similarity(vector, v2).item()
print(f"Similitud coseno: {sim:.3f}")   # 0.7-0.9 = muy parecidas
print(vector[:10])