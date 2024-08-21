# Pacote de Processamento de Imagens

Este repositório contém um pacote de processamento de imagens em Python, criado para o desafio "Criando um Pacote de Processamento de Imagens com Python". O objetivo é demonstrar a criação e publicação de um pacote Python, incluindo as etapas para configurar, distribuir e publicar o pacote.

## Descrição

O pacote `pacote-modelo` oferece funcionalidades para o processamento de imagens. Abaixo estão os principais componentes e instruções para instalação e uso.

## Estrutura do Projeto

- **`setup.py`**: Arquivo usado para especificar como o pacote deve ser construído. Documentação: [Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
- **`requirements.txt`**: Lista de dependências que devem ser instaladas com o pacote.

### Exemplo do Arquivo `setup.py`

```python
from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    page_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="pacote-modelo",
    version="0.0.1",
    author="AllianceTechSolutions/Thiago",
    description="Descrição curta do pacote",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AllianceTechSolutions",
    packages=find_namespace_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)
```

## Instalação

Para instalar o pacote, use o gerenciador de pacotes pip:

```
pip install pacote-modelo
```
## Uso

Após a instalação, você pode usar o pacote em seus scripts Python. Aqui está um exemplo de como importar e usar uma função do pacote:

```
from pacote_modelo.module1_name import file1_name
file1_name.my_function()
```
## Comandos para Configuração e Publicação

1. Atualizar pip e instalar dependências:

``` 
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools
```

2. Criar distribuições:

```
python setup.py sdist bdist_wheel
```

3. Publicar o pacote:


- Criar conta no Test PyPI: [TestPyPI]
- Publicar no Test PyPI:

```
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

- Criar conta no Test PyPI: [PyPI]
- Publicar no Test PyPI:

```
python -m twine upload dist/*
```

## Autor

Thiago Arantes Borges Candido - AllianceTechSolutions

## Licença

[MIT]

```

Este código está formatado para que você possa copiá-lo e colá-lo diretamente no arquivo `README.md` do seu repositório. Se precisar de ajustes adicionais ou mais detalhes, você pode modificar conforme necessário.
```