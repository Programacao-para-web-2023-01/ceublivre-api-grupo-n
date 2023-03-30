# CeubLivre-API

## Interações

Este microsserviço gerencia as avaliações e comentários deixados pelos usuários sobre os produtos comprados, assim como
perguntas e repostas.


### #2 - Gerenciamento de comentários (2 pontos)

Permitir que os usuários possam comentar nas avaliações de outros usuários.

---

Necessidades: identificar comentário que vai receber a resposta, identificar usuário dono da resposta, resposta em si com limite de caracteres(?), data e hora da resposta

---

```
CREATE TABLE resposta(
   numero INT AUTO_INCREMENT PRIMARY KEY,
   comentario NOT NULL, --- foreign key
   nome_usuario NOT NULL, --- foreign key, usuário da resposta
   conteudo VARCHAR(240) NOT NULL,
   data_hora TIMESTAMP);

```
