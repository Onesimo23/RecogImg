José Onésimo Abel Nuvunga

**Contextualização**
A aprendizagem de línguas locais em Moçambique, como a Changana, tem tido problemas sérios devido à limitada presença de materiais pedagógicos que integrem métodos interativos e tecnológicos. Ao mesmo tempo, o avanço da visão computacional abre novas possibilidades para desenvolver ferramentas educacionais inovadoras que contribuem para a preservação e o ensino de línguas minoritárias. Este projeto busca unir tecnologia e educação ao desenvolver um agente inteligente que detecte objetos e traduza seus nomes para o Changana. Utilizando técnicas de visão computacional com o modelo YOLO para reconhecimento de objetos, o sistema proposto permitirá que estudantes e usuários interajam com o mundo ao seu redor em sua língua materna, facilitando o aprendizado e a valorização cultural.

**Problemas **

•	Falta de materiais didáticos em Changana: A ausência de materiais educativos em Changana dificulta o acesso ao aprendizado formal da língua.
•	Desafios no ensino de vocabulário contextualizado: Os métodos tradicionais de ensino de línguas nem sempre facilitam o aprendizado contextualizado, onde o aluno associa palavras diretamente aos objetos ao seu redor.
•	Baixa integração tecnológica no ensino de línguas locais: Embora a tecnologia de visão computacional esteja avançada, seu uso no ensino de línguas locais ainda é limitado em Moçambique. Este projeto visa preencher essa lacuna ao criar uma ferramenta educativa acessível e prática.


**Objetivos**
Objetivo Geral
	Desenvolver um agente inteligente que detecta objetos e traduz seus nomes para a língua Changana, usando visão computacional para facilitar o aprendizado interativo.
Objetivos Específicos
	Implementar um modelo de detecção de objetos com YOLO que identifique objetos comuns em tempo real.
	Traduzir automaticamente os nomes dos objetos detectados para o Changana, promovendo a aprendizagem da língua.
	Criar uma interface visual para exibir as traduções sobre os objetos detectados, facilitando a compreensão e o aprendizado.
	Integrar um sistema interativo de captura e tradução que permita o uso em dispositivos com câmeras, promovendo a acessibilidade do aprendizado.

**Bibliotecas**
Ultralytics YOLO (You Only Look Once): Utilizada para a detecção de objetos em tempo real. A YOLO é uma das redes neurais mais eficientes para reconhecimento de objetos, permitindo a identificação rápida e precisa de itens no ambiente.
OpenCV: Essencial para capturar imagens da câmera e manipular as imagens processadas. Fornece suporte para a exibição e anotação das imagens com retângulos e legendas, facilitando a visualização dos objetos e suas traduções.
Numpy (opcional, dependendo da necessidade de manipulação adicional de dados numéricos): Biblioteca para processamento e operações numéricas em arrays, podendo ser usada para otimizar a manipulação de dados de imagem.
