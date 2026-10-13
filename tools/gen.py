import json, html, sys, os
sys.path.insert(0, "/home/claude/v2")
from meta import META

F = json.load(open("/home/claude/v2/base.json"))
cards = json.load(open("/home/claude/cards/manifest.json"))

FAMS = ["Apresentador","Comparação","Ensino","Edição","Prova social","Reação","Nativo"]
TITULO = {
 "Apresentador":"Apresentador na câmera","Comparação":"Comparação e julgamento",
 "Ensino":"Ensino e demonstração","Edição":"Edição e truque visual",
 "Prova social":"Prova social e bastidor","Reação":"Reação e conversa",
 "Nativo":"Nativo de plataforma",
}
DESC = {
 "Apresentador":"O rosto carrega a peça. Depende inteiramente da fala.",
 "Comparação":"Coloca coisas lado a lado. Decidir comparando é mais rápido que avaliar no vácuo.",
 "Ensino":"Entrega método. Constrói autoridade.",
 "Edição":"A edição é o diferencial. Retém pelo estímulo visual.",
 "Prova social":"Mostra a operação real. Vence objeção de confiança.",
 "Reação":"Pega carona no que já existe. Rápido de produzir.",
 "Nativo":"Imita o conteúdo orgânico da plataforma onde roda.",
}
ESF = {"baixo":"Esforço baixo","medio":"Esforço médio","alto":"Esforço alto"}

def esc(s): return html.escape(str(s))

data = []
for slug,nome,fam,oque,gravar,roteiro,funil,erro in F:
    m = META[slug]
    data.append({
      "slug":slug,"nome":nome,"fam":fam,"oque":oque,"gravar":gravar,
      "roteiro":roteiro,"funil":funil.lower(),"erro":erro,
      "esforco":m[0],"camera":m[1],"dupla":m[2],"edicao":m[3],"saida":m[4],
      "img":("cards/%s.jpg"%slug) if slug in cards else None,
    })

secoes = []
for fam in FAMS:
    itens = [d for d in data if d["fam"]==fam]
    arts = []
    for d in itens:
        img = ('<img src="formatos-criativos/assets/%s" alt="Exemplo do formato %s" loading="lazy" decoding="async">' % (d["img"], esc(d["nome"]))) if d["img"] else '<div class="noimg">sem exemplo</div>'
        chips = ['<span class="chip chip-%s">%s</span>' % (d["esforco"], ESF[d["esforco"]])]
        if d["camera"]=="nao": chips.append('<span class="chip">Sem aparecer</span>')
        if d["dupla"]=="sim": chips.append('<span class="chip">Precisa de dupla</span>')
        if d["edicao"]=="alta": chips.append('<span class="chip">Edição pesada</span>')
        if d["saida"]!="video": chips.append('<span class="chip">%s</span>' % esc(d["saida"].capitalize()))
        arts.append(f'''<article class="card" id="{esc(d["slug"])}" data-slug="{esc(d["slug"])}" data-funil="{esc(d["funil"])}" data-esforco="{esc(d["esforco"])}" data-camera="{esc(d["camera"])}" data-dupla="{esc(d["dupla"])}" data-edicao="{esc(d["edicao"])}" data-busca="{esc((d["nome"]+' '+d["oque"]+' '+d["gravar"]+' '+d["roteiro"]).lower())}">
  <div class="shot">{img}</div>
  <div class="body">
    <div class="card-top">
      <h3>{esc(d["nome"])}</h3>
      <button class="usado" type="button" data-slug="{esc(d["slug"])}" aria-pressed="false">Marcar como usado</button>
    </div>
    <p class="oque">{esc(d["oque"])}</p>
    <div class="chips"><span class="chip chip-funil">{esc(d["funil"].capitalize())}</span>{''.join(chips)}</div>
    <dl>
      <dt>Como gravar</dt><dd>{esc(d["gravar"])}</dd>
      <dt>Roteiro</dt><dd>{esc(d["roteiro"])}</dd>
      <dt>Erro comum</dt><dd>{esc(d["erro"])}</dd>
    </dl>
    <div class="acoes">
      <button class="btn-brief" type="button" data-slug="{esc(d["slug"])}">Copiar briefing</button>
      <button class="btn-link" type="button" data-slug="{esc(d["slug"])}">Copiar link</button>
    </div>
  </div>
</article>''')
    secoes.append(f'''<section class="fam" data-fam="{esc(fam)}">
  <header class="fam-head"><h2>{esc(TITULO[fam])}</h2><p>{esc(DESC[fam])}</p><span class="n">{len(itens)}</span></header>
  <div class="grid">{''.join(arts)}</div>
</section>''')

briefs = {d["slug"]: {"nome":d["nome"],"funil":d["funil"],"gravar":d["gravar"],"roteiro":d["roteiro"],"erro":d["erro"],"oque":d["oque"]} for d in data}

tpl = open("/home/claude/v2/template.html", encoding="utf-8").read()
out = tpl.replace("<!--SECOES-->", "\n".join(secoes)).replace("/*DADOS*/", json.dumps(briefs, ensure_ascii=False))
open("/home/claude/formatos-criativos/index.html","w",encoding="utf-8").write(out)
print("gerado:", len(data), "formatos")
