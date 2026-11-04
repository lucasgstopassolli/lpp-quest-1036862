"""NÍVEL 1 — Vila do Boletim (Python)

Você é o(a) novo(a) monitor(a) da turma e vai montar o boletim usando funções PURAS.
Siga as missões na ordem e rode  python quest.py 1  a cada passo (veja o LEIAME.md).

Regra de ouro: uma função pura só usa o que recebe e só devolve um valor.
Não altere as listas recebidas e não use print dentro destas funções.
"""


# ============================================================ MISSÃO 1.1 — Funções puras
def media(notas):
    return round(sum(notas) / len(notas), 2) if notas else 0.0


def situacao(media_final):
    if media_final >= 7:
        return "aprovado"
    elif media_final >= 5:
        return "recuperacao"
    else:
        return "reprovado"


# ============================================================ MISSÃO 1.2 — map: o boletim da turma
def boletim(alunos):
    return [
        {
            "nome": a["nome"],
            "media": media(a["notas"]),
            "situacao": situacao(media(a["notas"])),
        }
        for a in alunos
    ]


# ============================================================ MISSÃO 1.3 — filter e reduce: aprovados e ranking
def aprovados(boletins):
    return [b["nome"] for b in boletins if b["situacao"] == "aprovado"]


def media_da_turma(boletins):
    if not boletins:
        return 0.0
    soma = sum(b["media"] for b in boletins)
    return round(soma / len(boletins), 2)


def ranking(boletins):
    ordenados = sorted(boletins, key=lambda b: (-b["media"], b["nome"]))
    return [b["nome"] for b in ordenados]