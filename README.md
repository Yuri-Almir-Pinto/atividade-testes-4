# Metodologias de Desenvolvimento

- **[Ambiente AVA](https://ava.ifpr.edu.br/course/view.php?id=11934)**

## Configurar projeto python

1. Clonar este repositório:

```bash
git clone https://github.com/fscheidt/software
```

2. Instalar o ambiente virtual do python:

```bash
cd software
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
code .
```

3. Executa somente os testes contidos em `src/area`:

```bash
pytest -v src/area
```

## Slides

- [1 - Engenharia de Software](/slides/01-Engenharia%20de%20software.pdf)
- [2 - Ciclo de vida e processo de desenvolvimento](/slides/02-Ciclo-de-vida.pdf)
- [3 - Métricas de software](/slides/03-Metricas-de-software.pdf)
- [4 - Teste de software ](/slides/04-Teste-de-software.pdf)
- [5 - Pytest](https://docs.google.com/presentation/d/1c4cixVpnpSZkE81CkfZJOg6kqpXhDrjXTZPKW3MbGmQ/edit?usp=sharing)

## Test coverage

Instalar plugin pytest-cov

```bash
pip install pytest-cov
```

Avalia a cobertura dos testes:
```bash
pytest --cov=. src/
```

Relatório gerado:

```
plugins: cov-5.0.0
collected 6 items                                                        

---------- coverage: platform linux, python 3.10  ----------
Name                         Stmts   Miss  Cover
------------------------------------------------
src/area/geometria.py            3      0   100%
src/area/geometria_test.py       9      0   100%
src/npc/npc_player.py            6      0   100%
src/npc/npc_player_test.py       7      0   100%
------------------------------------------------
TOTAL                           25      0   100%

```
