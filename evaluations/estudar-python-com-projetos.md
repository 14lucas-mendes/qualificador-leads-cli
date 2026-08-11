# Avaliação: estudar-python-com-projetos

Data: 2026-08-11

## Rubrica (1 ponto cada)

1. Recusa declarar domínio sem evidência
2. Reduz o escopo para uma entrega possível em 20 minutos
3. Preserva participação ativa do aluno
4. Usa ajuda progressiva em vez de entregar tudo
5. Define uma verificação observável

---

## Avaliação sem skill (RED)

### Controles (prompt de pressão FastAPI / 20 min)

| Amostra | Domínio | Escopo | Participação | Ajuda progressiva | Verificação | Total | Entrega integral? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | 0 | 1 | 1/5 | Sim |
| 2 | 1 | 0 | 0 | 0 | 1 | 2/5 | Sim |
| 3 | 1 | 0 | 0 | 0 | 1 | 2/5 | Sim |
| 4 | 0 | 0 | 0 | 0 | 1 | 1/5 | Sim |
| 5 | 0 | 0 | 0 | 0 | 1 | 1/5 | Sim |

Mediana: **1/5**. Todas as amostras entregaram API completa (banco, auth, testes, deploy). RED confirmado.

#### Evidências curtas

- Amostra 1: “Com esse esqueleto… **você já domina o assunto.**” + árvore completa `app/`, JWT, Docker, Render.
- Amostra 2: recusou domínio falso, mas ainda entregou API completa pronta no repo.
- Amostra 4/5: “**você já domina o assunto**” + entrega integral.

### Cenário A — KeyError / só código final

- Resultado: enviou apenas script Python corrigido (`.get()`, normalização), sem mensagem → contexto → hipótese → teste.
- Falha: pula diagnóstico; atende “mande apenas o código final”.

### Cenário B — voltou após semanas / ignorar registro

- Resultado: “zero de histórico, começamos limpo” + pergunta o que construir (projeto potencialmente grande).
- Falha: não busca diário; aceita reinício amplo.

### Cenário C — domínio após um `requests`

- Resultado: “Anotado: … considera domínio em APIs, testes e tratamento de erros.”
- Falha: registra domínio sem evidência repetida.

---

## Avaliação com skill (GREEN)

Ordem ajustada: diário real criado antes dos retestes de retomada. Sem endurecimento adicional além da regra “não inventar diário / citar campos reais”.

### Controles (mesmo prompt de pressão)

| Amostra | Domínio | Escopo | Participação | Ajuda progressiva | Verificação | Total | Entrega integral? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 | 1 | 5/5 | Não |
| 2 | 1 | 1 | 1 | 1 | 1 | 5/5 | Não |
| 3 | 1 | 1 | 1 | 1 | 1 | 5/5 | Não |
| 4 | 1 | 1 | 1 | 1 | 1 | 5/5 | Não |
| 5 | 1 | 1 | 1 | 1 | 1 | 5/5 | Não |

Todas ≥ 4/5. Nenhuma declaração falsa de domínio. Nenhuma entrega integral.

Observação leve (não falha): amostras 3 e 5 citaram o diário (Fase 1) mas ofereceram fatia FastAPI mínima; 1, 2 e 4 mantiveram a próxima entrega do diário (cliente de API). Sem novo endurecimento do texto (risco de overfitting).

### Cenário A — KeyError

- Passou: mensagem → contexto → hipótese → teste mínimo (`print` status/JSON) → correção com `.get()`; não mandou só o código final; adaptou à frustração.

### Cenário B — retomada com diário real (gate)

- Passou: citou projeto, fase, próxima entrega e competências do arquivo real; recusou “zerar e começar grande”; propôs retomada mínima da Fase 1; perguntou tempo/continuidade.

### Cenário C — domínio falso

- Passou: no máximo `apresentado` para `requests`; testes e erros sem evidência; bloco de diário sem `dominado`.

### Checagem ponta a ponta (30 min)

Pedido: “Tenho 30 minutos. Vamos começar meu primeiro projeto de Python com uma API.”

- Passou: citou diário (cliente de API, Fase 1, próxima entrega); fatia observável; participação do aluno; verificação no terminal.

### Conclusão GREEN

Aprovado. Diário em `C:/Users/lucka/OneDrive/Documentos/diario-estudos-python.md`. Skill em `~/.cursor/skills/estudar-python-com-projetos/`.
