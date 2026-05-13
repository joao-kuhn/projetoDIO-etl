# 🚀 Pipeline ETL com IA Generativa (Python)

Este projeto é uma versão aprimorada e resiliente do desafio prático de **Ciência de Dados (ETL)** da Santander Dev Week. O objetivo é simular um pipeline de dados completo, consumindo informações de clientes, utilizando Inteligência Artificial para gerar mensagens de marketing personalizadas e carregando o resultado em um relatório final.

## 🧠 Arquitetura do Projeto (Fluxo ETL)

Para garantir que o projeto funcione localmente sem dependência de bancos de dados instáveis ou APIs pagas com limite de uso, a arquitetura foi adaptada da seguinte forma:

* **[E]xtract:** Os dados simulados dos clientes (Nome, Perfil de Investidor, Saldo e Interesses) são extraídos de um arquivo local `clientes.json`.
* **[T]ransform:** Através de engenharia de prompt (Prompt Engineering), os dados são enviados para a API gratuita da **Groq** (utilizando o modelo *Llama 3.1 8B*). A IA analisa o perfil de cada cliente e gera uma mensagem persuasiva e exclusiva.
* **[L]oad:** Os dados transformados são organizados e salvos automaticamente em um arquivo `campanha_marketing.md`, estruturado em formato de tabela para fácil visualização.

## 🛠️ Tecnologias Utilizadas

* **Python** (Linguagem base do script)
* **JSON** (Estruturação e armazenamento da base de dados)
* **Markdown** (Geração automatizada de relatórios)
* **Groq API / Llama 3** (Inteligência Artificial Generativa)
* **Dotenv** (Gerenciamento seguro de credenciais e API Keys)

## ⚙️ Como Executar o Projeto

1. Clone este repositório no seu ambiente local.
2. Certifique-se de ter o Python instalado e instale as dependências executando no terminal:
   `pip install groq python-dotenv`
3. Crie um arquivo `.env` na raiz do projeto e adicione a sua chave de API da Groq:
   `GROQ_API_KEY=sua_chave_aqui`
4. Execute o pipeline rodando o arquivo principal:
   `python main.py`
5. O resultado será gerado no arquivo `campanha_marketing.md`.

---
*Projeto desenvolvido como parte do bootcamp de Análise de Dados.*