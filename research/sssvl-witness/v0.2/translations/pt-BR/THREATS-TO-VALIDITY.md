# Ameaças à validade

### T1
Casos elaborados pela equipe do comparador; oráculos pré-registrados não garantem independência metodológica.
Resposta: o pré-registro mitiga ajustes posteriores, não o viés de concepção compartilhada; recomenda-se replicação independente.
Residual: OPEN_LIMITATION (limitação em aberto).
### T2
Mesma linhagem de compilação entre inventários e referência; não constitui reprodução independente da compilação.
Resposta: congelar a referência antes da mutação; a linhagem de compilação compartilhada permanece uma limitação.
Residual: OPEN_LIMITATION (limitação em aberto).
### T3
Repetições determinísticas não constituem amostra estatística independente.
Resposta: relatar separadamente os casos distintos e as repetições pareadas; sem taxa estatística agregada.
Residual: OPEN_LIMITATION (limitação em aberto).
### T4
W04 utiliza entidades e arestas sintéticas; B2-A utiliza arquivo e declaração direta, não pacote ou provedor.
Resposta: distinguir as entidades/arestas sintéticas de W04 dos papéis de arquivo/declaração de B2-A.
Residual: OPEN_LIMITATION (limitação em aberto).
### T5
Validade formal limitada a schema/referências; REAL-07 preserva SHA1 e altera a alegação SHA256.
Resposta: limitar as alegações de schema ao Draft7 e às verificações de referências implementadas; distinguir uma alegação de hash incorreta de bytes alterados.
Residual: OPEN_LIMITATION (limitação em aberto).
### T6
Configuração autenticada pelo chamador; REAL-08 testa incompatibilidade explícita, não descoberta autônoma.
Resposta: relatar incompatibilidade explícita de configuração, não inferência autônoma.
Residual: OPEN_LIMITATION (limitação em aberto).
### T7
Sem scanner real, runtime, vulnerabilidade ou segurança operacional demonstrada.
Resposta: nenhuma conclusão sobre scanner, exploit ou segurança em runtime; trabalho adicional exige autorização separada.
Residual: OPEN_LIMITATION (limitação em aberto).
### T8
Sem isolamento qualificado pelo sistema operacional; Evidence Vault pendente.
Resposta: separação entre processos não equivale a isolamento por sandbox; o vault e MT06 permanecem bloqueados/não verificados.
Residual: OPEN_LIMITATION (limitação em aberto).
