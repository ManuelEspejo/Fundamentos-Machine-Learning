# 🌟🤖​🧠​ Introducción a Machine Learning para Profesionales 🧠🤖​​​🌟

¡Bienvenidos al repositorio de recursos de **Introducción a Machine Learning**! Este repositorio está diseñado para **profesionales de cualquier área** que quieran aprender las bases de Machine Learning de una manera **clara, accesible y práctica**. No necesitas experiencia técnica previa, solo curiosidad y ganas de aprender.

## 📚 Índice de Contenidos

- [🌟🤖​🧠​ Introducción a Machine Learning para Profesionales 🧠🤖​​​🌟](#-introducción-a-machine-learning-para-profesionales-)
  - [📚 Índice de Contenidos](#-índice-de-contenidos)
  - [🎯 Objetivo](#-objetivo)
  - [📚 Contenido](#-contenido)
  - [🤷🏻‍♂️ ¿Para quién es este repositorio?](#️-para-quién-es-este-repositorio)
  - [🛠️ ¿Qué aprenderás?](#️-qué-aprenderás)
  - [🚧 ¿Qué necesitas?](#-qué-necesitas)
  - [🔥 ¿Cómo empiezo?](#-cómo-empiezo)
    - [📁 Estructura del repositorio](#-estructura-del-repositorio)
      - [📄 Descripción de la Organización](#-descripción-de-la-organización)
    - [🚀 Ejecución de Notebooks](#-ejecución-de-notebooks)
      - [🌐 En Google Colab (ideal para principiantes)](#-en-google-colab-ideal-para-principiantes)
      - [💻 En Local (opción avanzada)](#-en-local-opción-avanzada)
  - [🔗 Recursos externos](#-recursos-externos)
    - [Google Colab](#google-colab)
  - [💬 Guía de contribución](#-guía-de-contribución)

## 🎯 Objetivo

Con la creciente **explosión de la IA generativa**, muchos profesionales están descubriendo el poder transformador de la inteligencia artificial. Este repositorio tiene como objetivo **extender el Machine Learning** a quienes, desde distintas áreas, deseen profundizar en los fundamentos, **sin tecnicismos ni complejidades innecesarias**.

## 📚 Contenido

En este repositorio encontrarás:

- **Notebooks Introductorios:** Material paso a paso que te guiará en la creación de tus primeros modelos de Machine Learning, desde la adquisición de datos hasta la evaluación de los resultados.
- **Recursos adicionales:** Mis lecturas recomendadas, cursos y vídeos favoritos para seguir aprendiendo.
- **Conceptos clave:** Explicaciones claras y concisas de los términos más importantes en Machine Learning, como la diferencia entre IA, Machine Learning y Deep Learning, tipos de aprendizaje, y más.
- **Ejemplos prácticos:** Aplicaciones de Machine Learning en sectores variados (marketing, finanzas, personalización de recomendaciones, etc.).
- **Glosario:** Explicaciones claras y concisas de los términos clave que aparecen en los notebooks.

## 🤷🏻‍♂️ ¿Para quién es este repositorio?

Este repositorio es perfecto para:

- **Profesionales no técnicos** que ya utilizan herramientas de IA generativa pero quieren entender cómo funcionan sus bases.
- **Curiosos de la tecnología** que desean aplicar Machine Learning en su trabajo o proyectos personales.
- **Cualquier persona** con interés en aprender cómo los modelos de Machine Learning pueden transformar industrias.

## 🛠️ ¿Qué aprenderás?

1. **Fundamentos de Machine Learning**: Qué es, cómo funciona y cómo aplicarlo.
2. **Creación de tu primer modelo**: Cómo entrenar un modelo básico con datos reales usando Python.
3. **Aplicación práctica**: Ejemplos sencillos aplicables a problemas reales.

## 🚧 ¿Qué necesitas?

Para aprovechar este repositorio necesitarás lo siguiente:

- **Curiosidad y ganas de aprender**. No necesitas conocimientos previos ni instalar nada en tu ordenador.
- **Acceso a internet y una cuenta de Google**: Los notebooks se pueden ejecutar directamente en Google Colab, por lo que solo necesitarás un navegador web.
- **Tu LLM de confianza**: ChatGPT, Claude o el que más uses, para profundizar en los conceptos que más te interesen, generar código y hacer tus propios experimentos.
- **Opcional**: Conocimientos básicos de programación en Python (aunque no es obligatorio, si tienes dudas tu LLM te lo explica).

## 🔥 ¿Cómo empiezo?

Realmente puedes empezar por donde te apetezca, símplemente sigue tu curiosidad y revisa el tema que más te llame la atención. En la carpeta [notebooks](notebooks) encontrarás los notebooks que hemos creado hasta el momento. Cualquier notebook está hecho para ser entendido y ejecutado individualmente.

Sin embargo, te recomiendo encarecidamente que te leas el notebook [00_Empieza-aquí.ipynb](notebooks/00_Empieza-aquí.ipynb), porque ahí te doy una introducción a todo el proyecto, te explico cómo puedes contribuir y cómo sacarle todo el partido a todos .los recursos que encontrarás en este repositorio.

### 📁 Estructura del repositorio

Esta es la estructura del repositorio, para que te hagas una idea de cómo está organizado:

├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── imgs/
├── notebooks/
│   ├── 00_Empieza-aquí.ipynb
│   ├── 01_Intro-to-Supervised-Learning.ipynb
│   ├── 02_Intro-to-Unsupervised-Learning.ipynb
│   └── ...
└── utils/
    ├── helper_functions.py
    └── README.md

#### 📄 Descripción de la Organización

- **README.md**: Guía completa de este proyecto.
- **notebooks/**: Los notebooks organizados y nombrados de manera consistente, comenzando por "00_" para el introductorio, luego "01_", "02_", etc., para temas específicos. Facilitando la exploración por temas.
- **requirements.txt**: Lista de librerías necesarias para ejecutar los notebooks (para usar en local).
- **data/**: Carpeta para alojar los datasets (para usar en local).
  - **raw/**: Datos sin procesar.
  - **processed/**: Datos procesados.
- **docs/**: Para información adicional y recursos visuales, como imágenes, gráficos y otros elementos que aparecen en los notebooks.
- **utils/**: Funciones auxiliares para los notebooks. He intentado abstraer lo máximo posible el código que no sea específico de los temas tratados en los notebooks, para que puedas concentrarte aprender los conceptos clave.
  - **utils/README.md**: Explicación de cada script auxiliar y cómo pueden usarse en los notebooks. Esto ayuda a los colaboradores a entender cómo utilizar funciones específicas sin que se dupliquen en cada notebook.

### 🚀 Ejecución de Notebooks

#### 🌐 En Google Colab (ideal para principiantes)

Al comienzo de cada notebook, encontrarás un botón para abrirlo directamente en Google Colab. Solo tienes que hacer clic en el botón **Abrir en Google Colab** y el notebook se cargará en un entorno en línea, listo para ejecutarse sin necesidad de instalar nada en tu ordenador. Puedes hacer una copia del notebook en tu Google Drive para poder editarlo.

**Ventajas**:

- En el plan gratuíto puedes ejecutar todo este contenido sin ningún problema.
- No requiere configuración ni instalación previa, ya viene con gran parte de las librerías que necesitarás instaladas por defecto.
- Está integrado con Gemini de Google.

Si necesitas más información sobre cómo funciona Google Colab, puedes consultar la sección de [Recursos externos](#google-colab) para encontrar enlaces a tutoriales y recursos adicionales.

#### 💻 En Local (opción avanzada)

Esta opción es para quienes quieran tener más control sobre su entorno de trabajo y ejecución, y si estás empezando y no te interesa demasiado el apartado técnico, te recomiendo la opción anterior.

Si usas esta opción, asumo que ya tienes ciertos conocimientos de Github, por lo que no me voy a extender demasiado:

1. Descarga este repositorio en tu ordenador.

```bash
git clone https://github.com/ManuelEspejo/Machine-Learning-Bases.git
```

2. Navega hasta la carpeta del repositorio.

```bash
cd Machine-Learning-Bases
```

3. Crea un entorno virtual (recomendado) y ejecuta en tu terminal el fichero `requirements.txt` para instalar las librerías necesarias.

```bash
pip install -r requirements.txt
```

4. Inicia Jupyter Notebook o tu editor de código favorito con soporte para notebooks.

## 🔗 Recursos externos

(En proceso...)

### Google Colab

- [Tutorial de Introducción a Google Colab](https://www.youtube.com/watch?v=8VFYs3Ot_aA&ab_channel=DATACLOUDER)
- [Documentación oficial de Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)

## 💬 Guía de contribución

Si tienes preguntas o te gustaría compartir tus avances, no dudes en **abrir un issue** en este repositorio. También puedes contactarme a mi correo:[manuelesph@gmail.com](mailto:manuelesph@gmail.com), ​.

Si tienes ideas para mejorar este proyecto, ¡nos encantaría escuchar tus sugerencias! Sigue estos pasos para contribuir:

1. **Crear un Issue**: Si tienes una sugerencia o encuentras un problema, abre un issue en el repositorio describiendo tu propuesta.

   [![Crear un Issue](https://img.shields.io/badge/-Crear%20Issue-4a4a4a?style=for-the-badge&logo=github)](https://github.com/ManuelEspejo/Machine-Learning-Bases/issues/new)

2. **Fork y Pull Request**: Si quieres hacer una contribución directa, haz un fork del repositorio, realiza tus cambios y envía un pull request.

   [![Fork Repo](https://img.shields.io/badge/-Hacer%20Fork-4a4a4a?style=for-the-badge&logo=github)](https://github.com/ManuelEspejo/Machine-Learning-Bases/fork)

   [![Crear Pull Request](https://img.shields.io/badge/-Enviar%20Pull%20Request-4a4a4a?style=for-the-badge&logo=github)](https://github.com/ManuelEspejo/Machine-Learning-Bases/pulls)

3. **Revisión de Cambios**: Nuestro equipo revisará tus cambios y te dará feedback. 

   - Si estás buscando alguna respuesta en GitHub o necesitas ver las notificaciones de tu contribución:

   [![Ver Notificaciones](https://img.shields.io/badge/-Notificaciones-4a4a4a?style=for-the-badge&logo=github)](https://github.com/notifications)

4. **Checklist de Contribución**:
   - ✅​ Si modificas el código, asegúrate de que esté comentado y sea fácil de entender.
   - ✅​ Incluye una breve descripción de tu cambio en el pull request.
   - ✅​ Si creaste un notebook nuevo, añade una breve introducción explicando su propósito.

5. **Otras sugerencias**:
   - Si tienes cualquier otra sugerencia, o quieres contactar conmigo para cualquier cosa, puedes hacerlo a través de mi correo: [manuelesph@gmail.com](mailto:manuelesph@gmail.com). Estaré encantado de resolver tus dudas 😊

---
¡AH! Lo más importante... ¡Explora, aprende y empieza a aplicar Machine Learning en tu área de interés! 🔥 🔥
