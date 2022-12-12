# Bem vindo a Pilar API
[![Pilar CI](https://github.com/rvaccari/pilar/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/rvaccari/pilar/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10-green)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Stack**
- Linguagem: Python 3.10
- Frameworks: Flask
- Infra: Docker, docker-compose

**Instalação**
1. Clone o repositório
2. Execute a instalação
3. Execute os testes

```
git clone https://github.com/rvaccari/pilar.git && cd pilar
make install
make test
```

**Executando via docker-compose**
1. Clone o repositório
2. Execute o build
3. Rode o projeto
4. Pare a execução do projeto
```
git clone https://github.com/rvaccari/pilar.git && cd pilar
make docker-build
make docker-up
make docker-stop
```

**Links do projeto**
*Teste local*
| Page        | Address                                                                        | Use                                                                                                                                           |
|:------------|:-------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| vowel_count | [http://127.0.0.1:5000/api/vowel_count](http://127.0.0.1:5000/api/vowel_count) | ```curl -d '{"words": ["batman", "robin", "coringa"]}' -H "Content-Type: application/json" -X POST 127.0.0.1:5000/api/vowel_count```          |
| sort        | [http://127.0.0.1:5000/api/sort](http://127.0.0.1:5000/api/sort)               | ```curl -d '{"words": ["batman", "robin", "coringa"], "order": "asc"}' -H "Content-Type: application/json" -X POST 127.0.0.1:5000/api/sort``` |

*Teste em produção*
| Page        | Address                                                                                  | Use                                                                                                                                                       |
|:------------|:-----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| vowel_count | [https://pilar.onrender.com/api/vowel_count](https://pilar.onrender.com/api/vowel_count) | ```curl -d '{"words": ["batman", "robin", "coringa"]}' -H "Content-Type: application/json" -X POST https://pilar.onrender.com/api/vowel_count```          |
| sort        | [https://pilar.onrender.com/api/sort](https://pilar.onrender.com/api/sort)               | ```curl -d '{"words": ["batman", "robin", "coringa"], "order": "asc"}' -H "Content-Type: application/json" -X POST https://pilar.onrender.com/api/sort``` |
