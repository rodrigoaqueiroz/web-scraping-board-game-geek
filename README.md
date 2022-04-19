# BoardGameGeek (BGG) Web Scraping.

---

# Sumário

- [Habilidades](#habilidades)
- [Desenvolvido](#o-que-foi-desenvolvido)
- [Estrutura](#estrutura-de-arquivos-e-pastas)
  - [arquivos](#os-arquivos)
  - [pastas](#as-pastas)
- [Ambiente Virtual](#como-desenvolver)
- [Raspagem](#raspagem)
- [Contatos](#contatos)
---

# Habilidades

- Utilizar o terminal interativo do Python;
- Escrever seus próprios módulos e importá-los em outros códigos;
- Aplicar técnicas de raspagem de dados;
- Extrair dados de conteúdo HTML;
- Armazenar os dados obtidos em um banco de dados. (MySQL)
- Fazer análises usando o pandas.
- Exportar gráficos
- Exportar os dados obtidos para o excel

---

## O que foi desenvolvido

O projeto foi feito para exercitar minha habilidade de raspagem de dados e matar a minha curiosidade de saber quais eram os jogos de tabuleiro mais bem rankeados, mais populares e mais pesados do top 1000. Além de detalhes como ano, popularidade e com quantas pessoas é o mais recomendado para jogar. 
Eu amo jogar BG mas nunca tinha feito um estudo sobre os mais bem ranqueados, comecei a estudar o assunto de raspagem de dados e notei que eu poderia matar a curiosidade e exerciar ao mesmo tempo.

A lista com o rank dos jogos pode ser obtido no [BoardGame Rank](https://boardgamegeek.com/browse/boardgame).

---

# Estrutura de Arquivos e Pastas

### Os Arquivos:

- `requirements.txt` e `dev-equirements.txt` para adicionar as dependências que foram utilizadas no projeto.

- `database.py` é responsável pela conexão com o banco de dados;

- `query.py` por adicionar as informações coletadas no banco de dados

### As Pastas:

__Importer__: Funções responsáveis pela raspagem de dados.

__Exporter__: Funções responsável por transformar os dados salvos no Banco de Dados `MySQL` em `csv`

__Analyzer__: Análises e gráficos das informações coletadas da lista de jogos, foi usado o pandas e o seaborn.

---

# Como desenvolver


1. **criar o ambiente virtual**

```bash
$ python3 -m venv .venv
```

2. **ativar o ambiente virtual**

```bash
$ source .venv/bin/activate
```

3. **instalar as dependências no ambiente virtual**

```bash
$ python3 -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todas as dependências que foram utilizadas no projeto.

---

## Raspagem

A lista de jogos a ser raspadas está disponível na aba Browse/All BoardGames no _BGG_: https://boardgamegeek.com/browse/boardgame.
Os jogos foram salvos no banco de dados MySQL, usando as funções python implementadas no módulo `query.py`, a conexão com o DB está no módulo `database.py`

---

# Contatos:

<div style="display: flex; align-items: center; justify-content: space-between;">
  <div>
    <h4> Rodrigo de A. Queiroz </h4>
  <div style="display: flex; align-items: center;">
    <img src="./assets/images/linkedin-logo.png" alt="linkedin-logo" style="width:20px; padding: 5px"/>  https://www.linkedin.com/in/rodrigoandradequeiroz/
  </div>
  <br/>
  <div style="display: flex;align-items: center;">
    <img src="./assets/images/github-logo.png" alt="github-logo" style="width:20px; padding: 5px"/> https://github.com/rodrigoaqueiroz
  </div>
  <br/>
  <div style="display: flex;align-items: center;">
    <img src="./assets/images/email-logo.png" alt="email-logo" style= 'width:20px; padding: 5px'/></img>
    <a href="mailto:rodrigoandradequeiroz@gmail.com">rodrigoandradequeiroz@gmail.com</a>
  </div>
<br/>

---

