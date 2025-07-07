# ProyectoSisRec IIC3633-1 2025-1

## Integrantes del grupo
- Lucas Vidal
- Vicente Steidle
- Nicolás Herrera

Este repositorio agrupa la implementación y evaluación de distintos sistemas de recomendación aplicados a datos de Goodreads (interacciones implícitas entre usuarios y libros) y features de contenido (texto e imágenes).

## 📁 Estructura de archivos

```
ProyectoSisRec/
├── .gitignore
├── README.md                ← Este archivo
├── Analisis_de_datos/       ← Análisis exploratorio de datos
│   ├── Analisis_de_datos.ipynb   ← Notebook principal de EDA
│   └── image_downloader.py       ← Script para descargar portadas
├── Modelos/                 ← Notebooks de implementación de modelos
│   ├── baselines.ipynb            ← ALS, BPR, IBCF, Random, Most Popular
│   ├── book_covers.ipynb         ← Recomendación basada en portadas
│   ├── book_embeddings.ipynb     ← BERT embeddings como recomendador
│   ├── Content_based/            ← Modelos de filtrado basado en contenido
│   │   ├── image_embeddings_BERT_large.ipynb    
│   │   └── text_embeddings_ResNet50.ipynb      
│   ├── cornac.ipynb             ← Experimentos con libreria Cornac para VBPR (no usado en informe)
│   ├── matrix_factorization_books.ipynb         ← MF con LightFM (no usado en informe)
│   ├── matrix_factorization_books_pca.ipynb     ← LightFM + PCA
│   ├── NCF.ipynb                ← Neural Collaborative Filtering y variantes (usado para resultados tabla)
│   ├── NCF_with_examples.ipynb  ← NCF con ejemplos de recomendación
│   ├── user_features.ipynb      ← Filtrado basado en features de usuario
│   └── vbpr.ipynb               ← Implementación de VBPR
└── data/                    ← (Opcional) Carpeta de datos 
    └── resnet_book_embeddings.npy
```

> **Nota:** en este repo los archivos de datos (`.json`, `.csv`, `.npy`) se cargan directamente en los notebooks bajo `Modelos/` y `Analisis_de_datos/`.

## 📦 Runtime Environment

Todos los notebooks fueron corridos en Google Colab.

## 🚀 Reproducción de Experimentos

1. **Análisis exploratorio**
   Ejecutar `Analisis_de_datos/Analisis_de_datos.ipynb` para ver la distribución de interacciones, popularidad de libros, etc.

2. **Modelos de baseline**
   Abrir y ejecutar `Modelos/baselines.ipynb` para comparar ALS, BPR, IBCF, Most Popular y recomendación aleatoria.

3. **Embeddings de libros**

   * Texto: `book_embeddings.ipynb` usa BERT.
   * Portadas: `book_covers.ipynb` usa VGG16/ResNet.

4. **Filtrado basado en contenido**
   Revisar `Modelos/Content_based/*.ipynb` para ver distintos enfoques de similitud.

5. **Factorization Machines (FM)**

   * `matrix_factorization_books.ipynb`: LightFM sin PCA (muy lento y no utilizado en informe final).
   * `matrix_factorization_books_pca.ipynb`: LightFM + PCA sobre embeddings.

6. **Neural Collaborative Filtering (NCF)**

   * Resultados: `NCF.ipynb`.
   * Resultados + ejemplos de recomendación: `NCF_with_examples.ipynb`.

7. **User Features (UF)**
   `user_features.ipynb`: construcción de vectores de usuario y recomendación.

8. **VBPR**
   `vbpr.ipynb`: Visual BPR, combinando imágenes y colaborativo.

9. **Evaluación completa**

   * Métricas de ranking: Precision\@K, NDCG\@K, MAP\@K.
   * Métricas de diversidad: ILD\@K.
   * Métricas de novedad: Novelty\@K.
   * Ejemplos de recomendaciones y perfiles.

## 📝 Notas

* Notebooks descargan los datos automáticamente a excepción de `resnet_book_embeddings.npy/`, ese archivo cargarlo al runtime environment de Colab.



