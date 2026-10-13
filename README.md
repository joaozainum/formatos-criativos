# formatos-criativos

Skill para Claude: catálogo de 41 formatos de criativo para Reels, TikTok e anúncios de vídeo, com roteiro e direção de gravação para cada um.

## O que ela faz

Transforma um tema em roteiro gravável, escolhendo o formato pela função que a peça precisa cumprir (topo, meio ou fundo de funil) em vez de pelo gosto de quem brieffa.

Ela também responde o que o nome de um formato quer dizer, que é a dúvida mais comum do time: "tela na tela", "A ou B", "build in public", "tier list".

## Estrutura

```
index.html                      pagina de consulta do time (GitHub Pages)
formatos-criativos/
├── SKILL.md                    fluxo, tabela de escolha e regras gerais
├── references/
│   ├── catalogo.md             as 41 fichas completas
│   ├── copy.md                 ganchos, roteiro, legenda e regras anti-invencao
│   └── pesquisa.md             ferramentas de pesquisa e benchmark com fontes
└── assets/
    └── cards/                  imagem de referência de cada formato
```

O `SKILL.md` fica enxuto de propósito. Cada referência só é carregada quando a tarefa precisa dela.

## Como instalar

Copie a pasta `formatos-criativos/` para o diretório de skills do seu ambiente Claude. O nome da pasta precisa bater com o campo `name` do frontmatter.

## Como usar

Peça naturalmente, sem citar a skill:

- "Preciso de três criativos sobre dor lombar para topo de funil"
- "O que quer dizer o formato tela na tela?"
- "Esse criativo fadigou, me dá variações em outros formatos"
- "Transforma esse tema em roteiro com legenda pronta"
- "Qual formato entrega mais no Instagram hoje?"
- "Que ferramenta usar para pesquisar criativo de concorrente?"

## Consulta online

A página em `index.html` publica o catálogo com busca por nome e filtro por estágio de funil, para o time consultar sem precisar de conta no GitHub.

## Formatos cobertos

41 formatos em sete famílias: apresentador na câmera, comparação e julgamento, ensino e demonstração, edição e truque visual, prova social e bastidor, reação e conversa, e nativo de plataforma.

## Origem e uso das imagens

As descrições, roteiros e alertas foram escritos para uso próprio, a partir de um quadro de referência de formatos.

As imagens em `assets/cards/` são recortes de peças de criadores terceiros e servem apenas como referência visual interna, para o time reconhecer o formato. Não republique essas imagens. Se o repositório for público, considere remover a pasta `assets/` e manter só o texto.
