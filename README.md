# DW_dbt_sql_st

Este repositório contém o código-fonte do meu projeto de extração, transformação e carga de dados (ETL) que faz conexão com um banco de dados PostgreSQL na AWS via RDS.

O objetivo do projeto é extrair dados de commodities do Yahoo Finance, transformá-los em uma estrutura adequada e carregá-los em um banco de dados PostgreSQL na AWS via RDS.

O projeto utiliza as seguintes tecnologias:

* dbt: um framework de transformação de dados que permite definir e executar modelos de dados em diferentes ambientes.
* Render: um serviço de deploy de aplicações web que permite hospedar e executar aplicações web em um ambiente de produção.
* Streamlit: uma biblioteca Python que permite criar aplicações web interativas com facilidade.

O código-fonte está organizado em dois diretórios principais:

* `src`: contém o código-fonte do projeto, incluindo as funções de extração, transformação e carga de dados.
* `dbt_project`: contém o projeto dbt, incluindo os modelos de dados e as transformações.

Para executar o projeto, basta executar o comando `python src/extract_load.py` no diretório raiz do projeto. Isso irá extrair os dados do Yahoo Finance, transformá-los e carregá-los no banco de dados PostgreSQL na AWS via RDS.

O projeto também inclui um dashboard feito com Streamlit que permite visualizar os dados e realizar análises.

```mermaid
graph TD;
    A[Início] --> B[Extrair Dados das Commodities]
    B --> C[Transformar Dados das Commodities]
    C --> D[Carregar Dados no PostgreSQL]
    D --> E[Fim]

    subgraph Extrair
        B1[Buscar Dados de Cada Commodity]
        B2[Adicionar Dados na Lista]
    end

    subgraph Transformar
        C1[Concatenar Todos os Dados]
        C2[Preparar DataFrame]
    end

    subgraph Carregar
        D1[Salvar DataFrame no PostgreSQL]
    end

    B --> B1
    B1 --> B2
    B2 --> C
    C --> C1
    C1 --> C2
    C2 --> D
    D --> D1
    
```
