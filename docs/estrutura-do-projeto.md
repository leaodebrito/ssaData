# Estrutura do Projeto

```
ssaData/
│
├── app.py                          # Ponto de entrada da aplicação
├── pagina_inicial.py               # Página de apresentação
├── dados_sociodemograficos.py      # Página de dados sócio-demográficos
├── equip_urbanos.py                # Página de equipamentos urbanos
│
├── funcoes_elementos_interface/
│   └── graficos.py                 # Funções de visualização (gráficos)
│
├── dados/
│   ├── dataset_salvador.csv                        # Dados sócio-demográficos dos bairros
│   ├── dataset_equip_urb_salvador.csv              # Dataset consolidado de equipamentos urbanos
│   ├── juntar_dataset.py                           # Script para consolidar os CSVs de equipamentos
│   ├── Equipamentos urbanos salvador- *.csv        # Arquivos-fonte por tipo de equipamento
│
├── assets/
│   └── farol_salvador.png          # Imagem exibida na sidebar
│
├── docs/                           # Documentação do projeto
│   ├── visao-geral.md
│   ├── estrutura-do-projeto.md
│   ├── dados.md
│   └── modulos.md
│
├── requirements.txt                # Dependências Python
├── LICENSE                         # Licença CC BY 4.0
└── readme.md                       # Documentação principal
```

## Fluxo da Aplicação

```
app.py
  └── sidebar (menu de navegação)
        ├── Página Inicial       → pagina_inicial.py
        ├── Dados Sócio-Demog.   → dados_sociodemograficos.py
        │       └── graficos.py (funções de visualização)
        └── Equipamentos Urbanos → equip_urbanos.py
```

## Geração dos Dados de Equipamentos

Os arquivos-fonte (`Equipamentos urbanos salvador- *.csv`) são CSVs individuais por tipo de equipamento. O script `dados/juntar_dataset.py` os consolida em um único arquivo (`dataset_equip_urb_salvador.csv`), adicionando as colunas `Tipo`, `cor`, `latitude` e `longitude`.

Para regerar o dataset consolidado:

```bash
cd ssaData
python dados/juntar_dataset.py
```
