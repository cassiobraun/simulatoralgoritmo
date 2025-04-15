# Sorting & Searching Algorithm Simulator  
#### 🎥 Video Demo: [https://youtu.be/mvFkVRoqD80](https://youtu.be/mvFkVRoqD80)

## 📌 Descrição

Este projeto é um simulador visual de algoritmos de ordenação e busca. O objetivo é ajudar estudantes a entender, de forma gráfica e interativa, como funcionam algoritmos clássicos como:

- **Bubble Sort**
- **Quick Sort**
- **Merge Sort**
- **Insertion Sort**
- **Selection Sort**
- **Binary Search**
- **Linear Search**

A interface é web, desenvolvida com:

- **HTML** para a estrutura da página  
- **CSS** para estilização  
- **JavaScript + D3.js** para manipulação visual dos dados e interatividade  
- **Python (Flask)** para geração dos dados e integração com o backend

---

## ⚙️ Como funciona

O usuário acessa o site, escolhe a quantidade de elementos e o tipo de algoritmo a ser simulado. Ao clicar em "gerar" e depois em "ordenar", o gráfico é desenhado e o algoritmo escolhido começa a executar passo a passo, atualizando a tela em tempo real.

---

## 📁 Estrutura dos Arquivos

- `app.py` – Código Python que gerencia as rotas do Flask, gera os dados aleatórios e serve os arquivos HTML.
- `templates/index.html` – Tela inicial do site.
- `templates/layout.html` – Página que contém o header e o footer.
- `templates/quick.html`, `bubblesort.html`, `merge.html`, `insertion.html`, `selection.html`, `binary.html`, `linear.html` – Páginas com os algoritmos e visualização com D3.js.
- `static/layout.css`, `index.css` – Estilo visual do site.
- `README.md` – Este arquivo com a descrição completa do projeto.

---

## 💡 Motivo da Escolha do Projeto

Pensei em realizar algo que integrasse a maior parte do conteúdo que aprendi no curso CS50 e, ao mesmo tempo, ajudasse outros estudantes a entender melhor esses conceitos. Escolhi este tema porque me interesso bastante pela lógica por trás dos algoritmos, e gostei muito da aula que abordava esse assunto.

---

## 🧠 Decisões de Design

Escolhi usar o **D3.js** por ser uma biblioteca poderosa para visualização de dados no navegador. A integração com **Flask** facilita a geração dinâmica dos dados. O projeto foi idealizado para ser simples, intuitivo e funcional.

---

## 🧗 Principais Desafios Enfrentados

A maior dificuldade foi implementar os algoritmos em conjunto com a interação gráfica em tempo real. Esse tipo de atualização exigiu muita atenção com timers e controle de fluxo no JavaScript usando `async/await`.

Outro desafio foi aprender a sintaxe da biblioteca **D3.js**, que era totalmente nova para mim. Entender como gerar e atualizar visualmente os dados com ela foi um processo de tentativa e erro – mas muito enriquecedor!

---

## 👨‍💻 Minha Jornada na Implementação

Comecei planejando o funcionamento do site com foco na experiência do usuário, usando botões interativos e um design simples.

Em seguida, implementei o backend com Flask, criando as rotas e a geração dos dados aleatórios com base na entrada do usuário. Tive mais dificuldade com os algoritmos recursivos, como o **Quick Sort**, devido à sua lógica de chamadas de função e controle de estado.

Depois, parti para os gráficos. Inicialmente, tentei integrar os dados do Flask com o D3.js diretamente, mas tive muitos problemas. Como solução, decidi implementar os algoritmos em JavaScript dentro dos próprios arquivos HTML, o que facilitou bastante a integração e o comportamento dinâmico.

---

## 📈 Como foi a Implementação dos Algoritmos

Para entender e codar os algoritmos, assisti a vídeos explicativos e interativos sobre cada um deles. Após isso, implementei manualmente em JavaScript e criei a interação com os botões no site. Quando o usuário digita a quantidade desejada e clica em "gerar", o vetor é gerado e visualizado passo a passo com o algoritmo escolhido.

---

## 📚 O que Aprendi

- Implementação prática de algoritmos de ordenação e busca
- Desenvolvimento frontend com HTML, CSS e JavaScript
- Uso da biblioteca D3.js para visualizações dinâmicas
- Integração backend/frontend com Flask

---

## 🔧 O que Poderia Ser Melhorado

- Adicionar opções de controle de velocidade na visualização  
- Permitir pausar e continuar a execução dos algoritmos  
- Tornar o site responsivo para dispositivos móveis  
- Incluir mais algoritmos para enriquecer a experiência do usuário

---

## ✅ Conclusão

Gostei muito de ter realizado esse projeto! Agradeço à equipe do CS50 por todo o conteúdo incrível. Esse projeto me motivou ainda mais a seguir aprendendo programação e espero que ele possa também ajudar e incentivar outros estudantes a explorarem mais o mundo dos algoritmos e da computação.

**Obrigado!**
