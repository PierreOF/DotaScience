# DotaScience

A API utilizada para ingestões de dados é a www.opendota.com.

Importante: Todos comandos executados apresentados neste arquivo são executados a partir da pasta raiz do projeto.

# Instalação

```bash
git clone https://github.com/TeoCalvo/DotaScience.git <nome_da_pasta>
```

```bash
cd <nome_da_pasta>
```

## Uso

### Preparação do ambiente

0. Subindo nosso banco de dados com docker
```bash
docker-compose up -d
```

1. Criando novo ambiente Python

```sh
conda create --name dota-env python=3.
```

2. Ativando ambiente python

```sh
conda activate dota-env
```

3. Instalando dependências

```sh
pip install -r requirements.txt
```
