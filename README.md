<h1 align="center">IA_disciplina</h1>
<p align="center">
Repositório para desenvolvimento em equipe das atividades de Inteligência Artificial, disciplina do 6º Sem na Fatec Cruzeiro.<br>
<i>Status do Projeto: <b>Finalizado</b> :heavy_check_mark:</i><br>
<b>Acesse ao programa: </b>https://share.streamlit.io/guilhermedonizetti/ia_disciplina/index.py
</p>

<b>Objetivo: </b>desenvolver um programa para gerar a melhor rota entre cidades. Em um cenário de catástrofe (independente do motivo), a ação da Ajuda Humanitária precisa do caminho mais curto para atender em menor tempo, também o caminho entre a cidade que sofre um desastre até um ponto de atendimento hospitalar precisa ser otimizado. Esse projeto visa a resolução desse problema!

<b>Cenário: </b>o cenário é usado para validar os algoritmos desenvolvidos, portanto se baseia num ambiente real que é o <a href="https://pt.wikipedia.org/wiki/Regi%C3%A3o_Metropolitana_do_Vale_do_Para%C3%ADba_e_Litoral_Norte">Vale do Paraíba (São Paulo - Brasil)</a>, uma mesorregião paulista no interior do estado mais o litoral norte, formado por 39 municípios. O objetivo do projeto será testado com rotas entre essas cidades.

<p align="center">
<img src="https://www.desenvolvevale.com.br/wp-content/uploads/2019/08/mapa_RMVPLN.jpg" width="510" height="395"></img>
</p>

<b>Etapas desenvolvidas: </b><br>
<ul>
<li>Encontra a rota entre o ponto de Ajuda Humanitária mais próximo e uma cidade X</li>
<li>Encontra a rota entre a cidade X e o ponto de Atendimento Hospitalar mais próximo</li>
<li>Implementa 8 métodos de busca diferentes em grafos:</li>
  <ul>
    <li>Amplitude</li>
    <li>Profundidade</li>
    <li>Profundidade Limitada</li>
    <li>Aprofundamento Iterativo</li>
    <li>Bidirecional</li>
    <li>A-estrela</li>
    <li>Greedy</li>
    <li>Custo Uniforme</li>
  </ul>
<li>Geração de mapas</li>
</ul>

<br>

<b>Demonstração: </b>a imagem abaixo mostra a rota gerada na tentativa de atender a uma demanda no município de Queluz - SP. Porém, é possível verificar a rota utilizando qualquer cidade do Vale do Paraíba (paulista) acessando (https://share.streamlit.io/guilhermedonizetti/ia_disciplina/index.py) e também escolher qual método de busca será usado. Para exibir a imagem do mapa, selecione "Buscar rota".<br>
<p align="center">
<img src="https://github.com/guilhermedonizetti/IA_disciplina/blob/master/images/resultado.png" width="770" height="455"></img>
</p>

<br>

<b>Modelagem: </b>O projeto é modelado em cima de um cenário real, que é o mapa do Vale do Paraíba, mas os pontos de Ajuda Humanirária (AH) e Atendimento Hospitalar usados no projeto não necessariamente correspondem à situação real da região, pois são usados apenas para validação dos algoritmos. Porém foram estrategicamente escolhidos como:

<ul>
  <li>Pontos de Ajuda Humanitária: Caraguatatuba, Cruzeiro, Guaratinguetá, São José dos Campos e Taubaté.</li>
  <li>Pontos de Atendimento: Aparecida, Caçapava, Cruzeiro, Guaratinguetá, Lorena, Pindamonhangaba, Queluz, São José dos Campos, São Sebastião e Taubaté.</li>
</ul>

Foi considerado o tamanho do território da região, a distribuição da população e os agrupamentos de cidades (sub-regiões) dentro do Vale. Com essa distribuição, cada ponto de atendimento hospitalar atende a 4 cidades e de ajuda humanitária atende a 8 cidades.

<br>

<b>Uso: </b>o projeto pode ser acessado no link apresentado acima. Mas se executar localmente, lembre-se que existe requirements e certifique-se de ter o ambiente preparado, execute:

```python
streamlit run index.py
```

<p align="center"><b>Devs: </b></p>
<table align="center">
  <tr>
    <td align="center"><a href="https://br.linkedin.com/in/guilhermedonizetti-ads"><img src="https://avatars.githubusercontent.com/u/47000945?v=4" width="100px;" alt=""/><br /><sub><b>Guilherme Donizetti</b></sub></a><br /><a href="https://github.com/guilhermedonizetti/IA_disciplina/commits?author=guilhermedonizetti" title="Desenvolvedor">💻</a></td>
    <td align="center"><a href="https://github.com/SACRIER"><img src="https://avatars.githubusercontent.com/u/61637378?v=4" width="100px;" alt=""/><br /><sub><b>Luiz Fernando Rodrigues</b></sub></a><br /><a href="https://github.com/guilhermedonizetti/IA_disciplina/commits?author=SACRIER" title="Desenvolvedor">💻</a></td>
    <td align="center"><a href="https://github.com/Ricardo-Braga1"><img src="https://avatars.githubusercontent.com/u/89203941?v=4" width="100px;" alt=""/><br /><sub><b>Ricardo Braga</b></sub></a><br /><a href="https://github.com/guilhermedonizetti/IA_disciplina/commits?author=Ricardo-Braga1" title="Desenvolvedor">💻</a></td>
  </tr>
</table>
</center>

<br>

<p align="center">
<b>Análise e Desenvolvimento de Sistemas - Fatec Cruzeiro</b><br>
Python, Inteligência Artificial.
</p>
