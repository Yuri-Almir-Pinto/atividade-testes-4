# Metodologias de Desenvolvimento

## Configurar projeto

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
