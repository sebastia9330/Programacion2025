from pypdf import PdfReader, PdfWriter
from sentence_transformers import SentenceTransformer
import numpy as np


#limpiar pdf
""" reader = PdfReader("Decreto_1082_de_2015_Sector_Administrativo_de_Planeación_Nacional.pdf", strict=False)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

with open("output_clean.pdf", "wb") as f:
    writer.write(f)
 """

#modelo local para vectores
modelo = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def embed(text):
    return modelo.encode(text).tolist()


#leer el pdf
reader1 = PdfReader("output_clean.pdf")
texto = ""

for pagina in reader1.pages:
    texto += pagina.extract_text()
    

#crear el chunk
def chunk_text(text, max_chars=800):
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

chunks = chunk_text(texto)

embeddingds = []

print("\n=== GENERANDO VECTORES ===\n")

for chunk_id, chunk_texto in enumerate(chunks):
    vector = embed(chunk_texto)
    embeddingds.append(vector)
    #print(f"\n--- VECTOR DEL CHUNK {chunk_id} ) ---\n")
    #print(vector[:10], "...")  

print(len(embeddingds))



pregunta = "¿Que dice el decreto sobre contratacion?"
vectorPregunta = np.array(embed(pregunta))
print(vectorPregunta[:10])