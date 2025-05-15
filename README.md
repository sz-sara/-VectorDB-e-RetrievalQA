<h1>Sistema de Recuperação de Informações usando VectorDB e RetrievalQA</h1>
<p>Repositório de como fazer um sistema de perguntas e respostas utilizando Langchain, FAISS como banco vetorial e Ollama para embeddings e geração de respostas com LLM. 
  <br>Utiliza-se um arquivo pdf como fonte de treinamento, a partir dele os chunks gerados são armazenados no banco vetorial a fim de que o usuário seja respondido no contexto do arquivo. </p>

  <h2>Requisitos</h2>
  <p>
    Python 3.10 acima (Versões estáveis são melhores) https://www.python.org/downloads/ <br>
    Ollama rodando localmente: https://ollama.com
  </p>

  ```bash
#Em um ambiente de desenvolvimento com terminal, colocar:
ollama run llama3.2
ollama run mxbai-embed-large
pip install langchain
pip install faiss-cpu
pip install langchain-community
pip install langchain-ollama
#Colocar o seu arquivo para análise no lugar do caminho:
file_path = "C:/Users/saraa/geral/TSI/GIT/Conteúdo 1 _ Projetos.pdf"

#Execute o script, exemplo de perguntas e respostas de acordo com meu arquivo sobre git:
Qual a sua pergunta? (Para interromper, digite: sair): Qual é o ciclo de vida de um arquivo no Git?
Resposta gerada pelo modelo:
 O ciclo de vida de um arquivo no Git é o seguinte:

1. Untracked (não rastreado): o arquivo existe no diretório do projeto, mas ainda não é gerenciado pelo Git.
2. Tracked / Unmodified (rastreado / não modificado): o arquivo é conhecido pelo Git e não sofreu alterações desde o último commit.
3. Modified (modificado): o arquivo foi alterado desde o último commit, mas ainda não foi preparado para o próximo commit.
4. Staged (preparado): o arquivo foi adicionado à "staging area" e está pronto para ser incluído no próximo commit.

Esses estão os estados possíveis de um arquivo no Git, conforme mencionado na seção 5 do texto fornecido.
```


  
