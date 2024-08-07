from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
import argparse
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

CHROMA_PATH = 'chroma/'

def main():
    #testando forma nova de query_text
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    #carregando o bd
    embedding_function = OpenAIEmbeddings(openai_api_key=api_key)
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
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
    prompt = prompt_template.format(context = context_text, question = query_text)
    
    #llm openAI
    model = ChatOpenAI(openai_api_key=api_key)
    #perguntando pro modelo
    response_text = model.predict(prompt)
    #resposta formatada
    print(f"De acordo com os livros, a resposta para sua pergunta é: \n{response_text}")

if __name__ == "__main__":
    main() 
    

