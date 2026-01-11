# A Use Case Lens on Digital Cultural Heritage

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hibernator11/eccch-use-cases/HEAD)

This project shows a selection of use cases based on the [European Collaborative Cloud for Cultural Heritage](https://www.echoes-eccch.eu) (ECCCH). It provides a collection of Jupyter Notebooks describing how the use cases are created including details about the data reused, the extraction, process and integration with EU research data infrastructures.

## Use cases

The following picture shows how existing platforms and services are integrated to create the use cases in the ECCCH, to foster excellence in data and Digital Commons. Note that this figure was inspired by the ECHOES project website and tries to illustrate how our approach fits within the current research data infrastructure.

<img width="50%" src="imgs/eccch-integration.png">

**Note that the code provided is in the form of a prototype. In some cases, a local environment is required such as the case of the employment of local LLMs. This work intends to provide an approach of how it could be implemented, since the ECCCH is currently under development. The notebooks can be run in a local environment as well as using cloud services such as Binder and EOSC Interactive Notebooks.**

### Using and reusing notebooks in high-performance computing environments 

This use case shows how to reuse maps made available by the National Library of Spain following a set of steps: extraction, OCR analysis using LLMs, metadata generation and dissemination. For more information, see the [notebook](HPC.ipynb).

### Application of notebooks in digital twins
### AI preservation use case
### Open Science for notebooks
### Sustainability for notebooks

## Licence
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />Content is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International license</a>.

Please, note that the datasets used in this project have separate licences.

## Installation guide

The code can be run on cloud services such as Binder without the need to install additional software and using only the web browser by clicking on the link provided at the beginning of this documentation.

The code can be also installed in a computer by following these steps:

- download the code from GitHub
- open the folder with the code
- run the command: pip install -r requirements.txt
- open Jupyter (or Anaconda)
- open the notebooks provided

Note that these notebooks can be run in different cloud services such as [Binder](https://mybinder.org/) and [EOSC Interactive Notebooks](https://open-science-cloud.ec.europa.eu/services/interactive-notebooks).

## How to cite
- Gustavo Candela, Milena Dobreva, Henk Alkemade, Olga Holownia, Mahendra Mahey, Sarah Ames, Karen Renaud, Ines Vodopivec, Benjamin Charles Germain Lee, Thomas Padilla, Steven Claeyssens, Isto Huvila, Beth Knazook: A Use Case Lens on Digital Cultural Heritage. CoRR abs/2509.08710 (2025)
  
## References
- https://www.echoes-eccch.eu/faq/
- Gustavo Candela, Milena Dobreva, Henk Alkemade, Olga Holownia, Mahendra Mahey, Sarah Ames, Karen Renaud, Ines Vodopivec, Benjamin Charles Germain Lee, Thomas Padilla, Steven Claeyssens, Isto Huvila, Beth Knazook: A Use Case Lens on Digital Cultural Heritage. CoRR abs/2509.08710 (2025)
- https://open-science-cloud.ec.europa.eu/services/interactive-notebooks
- Gustavo Candela, Javier Pereda, Dolores Sáez, Pilar Escobar, Alexander Sánchez, Andrés Villa Torres, Albert A. Palacios, Kelly McDonough, and Patricia Murrieta-Flores. 2023. An Ontological Approach for Unlocking the Colonial Archive. J. Comput. Cult. Herit. 16, 4, Article 74 (December 2023), 18 pages. https://doi.org/10.1145/3594727
