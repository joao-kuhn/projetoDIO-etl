import json
import os
from dotenv import load_dotenv
from groq import Groq 

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_JSON = os.path.join(DIRETORIO_ATUAL, 'clientes.json')
CAMINHO_MARKDOWN = os.path.join(DIRETORIO_ATUAL, 'campanha_marketing.md')

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract():
    with open(CAMINHO_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def transform(cliente):
    prompt = f"""
    Você é um especialista em marketing bancário. 
    Crie uma mensagem curta e persuasiva para o cliente {cliente['nome']}.
    Perfil: {cliente['perfil']}
    Interesses: {', '.join(cliente['interesses'])}
    
    A mensagem deve ser curta e incentivar o cliente a aumentar seu saldo atual de R$ {cliente['saldo_investido']:.2f}.
    Seja profissional e use o perfil dele para personalizar o tom.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Você é um assistente de marketing que fala português do Brasil fluente."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def load(resultados):
    with open(CAMINHO_MARKDOWN, 'w', encoding='utf-8') as f:
        f.write("# Relatório de Campanha Personalizada\n\n")
        f.write("| ID | Cliente | Mensagem Gerada |\n")
        f.write("|----|---------|-----------------|\n")
        for res in resultados:
            msg_limpa = res['mensagem'].replace('\n', ' ') 
            f.write(f"| {res['id']} | {res['nome']} | {msg_limpa} |\n")
    print(f"✅ Arquivo gerado com sucesso em: {CAMINHO_MARKDOWN}")

if __name__ == "__main__":
    print("🚀 Iniciando Pipeline com Llama 3 via Groq...")
    dados = extract()
    
    final_data = []
    for cliente in dados:
        print(f"Transformando dados de: {cliente['nome']}...")
        mensagem = transform(cliente)
        final_data.append({
            "id": cliente['id'],
            "nome": cliente['nome'],
            "mensagem": mensagem
        })
    
    load(final_data)