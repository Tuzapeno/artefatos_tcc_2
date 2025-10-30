# Artefatos do projeto

## Google Drive:
### Nesse link está contido todos os artefatos usados para realizar o experimento assim como os pesos e resultados.

https://drive.google.com/drive/folders/1-6LHC79H50vr8jsI7T9FVaM9TH1j0clV?usp=sharing

## Fonte dos datasets

- http://cnrpark.it/
- https://web.inf.ufpr.br/vri/databases/parking-lot-database/

## Estrutura dos diretórios

```
DATASETS_EXP
├── Augments
│   ├── LightPole
│   │   └── ...
│   └── Tree
│       └── ...
├── Data
│   ├── Tests
│   │   ├── CAMERA{1-9}.zip
│   │   ├── PUC.zip
│   │   └── UFPR0{4-5}.zip
│   ├── CNRPark-EXT.zip
│   ├── PKLot_small.zip
├── Models
│   ├── cnr_[baseline/copypaste].weights.h5
│   └── pk_[baseline/copypaste].weights.h5
└── Results
    └── CNRPark/PKLot
        ├── Baseline
        │   └── [cnr/pk]_baseline_[set].txt
        └── CopyPaste
            └── [cnr/pk]_copypaste_[set].txt
```

| Artefato | Descrição |
| :--- | :--- |
| **TCC_2.ipynb** | Arquivo Jupyter Notebook usado para realizar os experimentos. |
| **sorter.py** | Script escrito em Python para ler os arquivos de `label` do *dataset* CNRPark-EXT e organizar os arquivos em novos diretórios (`Train`) e (`Test`). |
| **fractor.py** | Script escrito em Python para realizar um random subsampling de 5% do dataset PKLot já organizado em (`Train`) e (`Test`). |
| **DATASETS_EXP/** | Diretório principal do projeto, contendo todos os dados de entrada, modelos treinados e resultados experimentais. |
| **./Augments/** | Diretório destinado a armazenar amostras de oclusões coletadas. |
| **./Augments/LightPole/** | Subdiretório contendo imagens de postes de luz (`LightPole`). |
| **./Augments/Tree/** | Subdiretório contendo imagens relacionadas à árvores e vegetações (`Tree`). |
| **./Data/** | Diretório que armazena os *datasets* pré-processados e compactados, divididos em conjuntos de treinamento e teste. |
| **./Data/Tests/** | Subdiretório que agrupa os subconjuntos compactados dos *datasets* utilizados especificamente para a etapa de testes do modelo. |
| **CAMERA{1-9}.zip, PUC.zip, UFPR0{4-5}.zip** | Arquivos compactados dos subconjuntos de dados de teste provenientes do PKLot e do CNRPark-EXT |
| **CNRPark-EXT.zip, PKLot_small.zip** | Arquivos compactados com os principais *datasets* utilizados, a versão reduzida do PKLot para treino (`PKLot_small`) e o conjunto de treinamento do CNRPark (`CNRPark-EXT`). |
| **./Models/** | Diretório que armazena os pesos dos modelos após o treinamento. |
| **cnr_[baseline/copypaste].weights.h5** | Arquivo de pesos no formato HDF5 (`.h5`) para o modelo treinado no *dataset* CNRPark, utilizando a estratégia de treinamento **`baseline`** ou **`copypaste`**. |
| **pk_[baseline/copypaste].weights.h5** | Arquivo de pesos no formato HDF5 (`.h5`) para o modelo treinado no *dataset* PKLot, utilizando a estratégia de treinamento **`baseline`** ou **`copypaste`**. |
| **./Results/** | Diretório principal que armazena os resultados dos experimentos, organizados por *dataset* (CNRPark/PKLot). |
| **./Results/.../Baseline/** | Subdiretório para resultados de testes usando o modelo treinado com a abordagem **`Baseline`**. |
| **./Results/.../CopyPaste/** | Subdiretório para resultados de testes usando o modelo treinado com a abordagem **`CopyPaste`**. |
| **[cnr/pk]_baseline_[set].txt, [cnr/pk]_copypaste_[set].txt** | Arquivos de texto contendo logs de métricas para o respectivo *dataset* (`cnr` ou `pk`), abordagem (`baseline` ou `copypaste`), e o subconjunto de dados específico (`set`) utilizado no teste, (UFPR04, CAMERA1, ...). |
