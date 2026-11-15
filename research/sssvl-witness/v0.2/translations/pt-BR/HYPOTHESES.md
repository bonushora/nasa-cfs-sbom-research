# Hipóteses pré-registradas

Todas as hipóteses estão NOT_TESTED (não testadas).

## H1 — Extrapolação indevida do veredito

Um pipeline especificado que converte zero correspondências com avisos de segurança em um veredito irrestrito de segurança pode produzir uma conclusão injustificada após a omissão de um componente sintético relevante.

Controle positivo: o inventário completo deve produzir a correspondência com o aviso de segurança sintético inserido deliberadamente.

Se o controle positivo falhar, o experimento é inválido.

Se o avaliador emitir apenas uma declaração de ausência de correspondências delimitada pelo escopo, ou bloquear o veredito mais amplo, a falha proposta não estará demonstrada para esse avaliador.

Uma política de promoção deliberadamente ingênua demonstra uma falha de política, não necessariamente um defeito de scanner.

## H2 — Reconciliação

Uma testemunha com uma referência independente e delimitada detecta a ausência de uma entidade requerida, uma incompatibilidade de identidade ou a ausência de uma dependência requerida.

Previsão: a divergência é registrada e a conclusão ampla solicitada é bloqueada.

Falsificação: uma divergência relativa a um requisito ou uma identidade não resolvida é aceita como reconciliada.

## H3 — Integridade versus completude

Um SBOM válido segundo o schema, com checksums regenerados, pode omitir um componente requerido pela referência.

Previsão: schema e integridade PASS; cobertura delimitada FAIL.

Construção inválida: falha de schema/checksum ou impossibilidade de estabelecer de forma independente a identidade da referência que está ausente no inventário.

## H4 — Sensibilidade à configuração

O inventário de uma configuração não pode fundamentar conclusões sobre outra configuração sem reconciliação com o escopo de referência requerido desta última.

Previsão: a substituição controlada detecta incompatibilidades de configuração ou cobertura.

Falsificação: o universo de referência requerido é equivalente sob o escopo declarado.

Comparação inválida: mistura silenciosa dos escopos de código-fonte, compilação, instalação ou execução.

## H5 — Especificidade

Um controle válido e delimitado não deve ser bloqueado apenas porque um componente explicitamente excluído está ausente.

Falsificação: exclusões justificadas de elementos fora do escopo ou identidades duplicadas legítimas provocam um veredito incorreto de insuficiência.

## Disciplina científica

Congelar o escopo, a referência de verdade, a versão do avaliador, o snapshot de avisos de segurança e os controles esperados antes da execução.

Registrar resultados negativos e inconclusivos.

Não tratar um controle inválido como uma descoberta positiva.
