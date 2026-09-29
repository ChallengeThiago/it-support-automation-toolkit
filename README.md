# IT Support Automation Toolkit

Motor de triagem determinístico para automatizar a primeira classificação de
chamados de suporte, com prioridade, categoria e fila sugerida.

## O que demonstra

- automação de processos de atendimento;
- regras explícitas e auditáveis para incidentes críticos;
- priorização P1/P2/P3 e resumo operacional da fila;
- testes unitários para preservar o comportamento das regras.

## Executar

```powershell
python -m unittest discover -s tests -v
```

As regras são um ponto de partida. Em produção, devem ser complementadas por
integração com ITSM, autenticação, trilha de auditoria e revisão humana.
