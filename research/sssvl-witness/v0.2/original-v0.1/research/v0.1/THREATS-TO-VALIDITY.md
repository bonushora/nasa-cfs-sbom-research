# Threats to validity

### T1
Casos desenhados pela equipe do comparador; oraculos pre-registrados nao garantem independencia metodologica.
Response: Pre-registration mitigates post-hoc adjustment, not shared design bias; independent replication recommended.
Residual: OPEN_LIMITATION
### T2
Mesma linhagem de build entre inventarios e referencia; nao reproducao independente de compilacao.
Response: Freeze reference before mutation; shared build lineage remains a limitation.
Residual: OPEN_LIMITATION
### T3
Repeticoes deterministicas nao sao amostra estatistica independente.
Response: Report distinct cases and paired repetitions separately; no pooled statistical rate.
Residual: OPEN_LIMITATION
### T4
W04 usa entidades e arestas sinteticas; B2-A usa arquivo e declaracao direta, nao pacote ou provedor.
Response: Distinguish W04 synthetic entities/edges from B2-A file/declaration roles.
Residual: OPEN_LIMITATION
### T5
Validade formal limitada a schema/referencias; REAL-07 preserva SHA1 e altera alegacao SHA256.
Response: Limit schema claims to Draft7 and implemented reference checks; distinguish false hash claim from changed bytes.
Residual: OPEN_LIMITATION
### T6
Configuracao autenticada pelo chamador; REAL-08 testa incompatibilidade explicita, nao descoberta autonoma.
Response: Report explicit configuration mismatch, not autonomous inference.
Residual: OPEN_LIMITATION
### T7
Sem scanner real, runtime, vulnerabilidade ou seguranca operacional demonstrada.
Response: No scanner, exploit or runtime safety conclusion; further work requires separate authorization.
Residual: OPEN_LIMITATION
### T8
Sem isolamento OS qualificado; Evidence Vault pendente.
Response: Process separation is not sandbox isolation; vault and MT06 remain blocked/unverified.
Residual: OPEN_LIMITATION
