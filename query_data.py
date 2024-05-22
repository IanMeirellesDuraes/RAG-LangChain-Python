from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os


PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    #testando forma nova de query_text
    query_text = input("Ask your question: ")
    #carregando o bd
    db = Chroma.load('chroma')
    #procurando as respostas
    results = db.similarity_search_with_relevance_scores(query_text, k = 4)
    if results[0][1] < 0.7 and len(results) == 0:
        print("Sorry, I don't know the answer to that question.")
        return
    
    #formando os contextos para o prompt
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    #fazendo o prompt template
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    #fazendo o prompt para perguntar ao modelo, juntando o template e a pergunta
    prompt = format.prompt_template(context = context_text, question = query_text)
    
    #llm openAI
    model = ChatOpenAI()
    #perguntando pro modelo
    response_text = model.predict(prompt)

    #resposta formatada
    print(f"De acordo com os livros, a resposta para sua pergunta é: \n{response_text}")

if __name__ == "__main__":
    main() 
    

