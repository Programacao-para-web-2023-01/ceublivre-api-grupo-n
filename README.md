# CeubLivre-API

## Interações

Este microsserviço gerencia as avaliações e comentários deixados pelos usuários sobre os produtos comprados, assim como
perguntas e repostas.

### #1 - Gerenciamento de avaliações (2 pontos)

Permitir que os usuários possam avaliar os produtos comprados e deixar uma nota ou estrela e um comentário sobre sua
experiência.

* Permitir avaliações com foto (1 ponto)

---

Necessidades: nome do usuário, limite de caracteres (?), número do comentário, data e hora nos quais o comentário foi realizado, estrelas (de 0 à 5) dos produtos, upvote/downvote(?).

---
```
CREATE DATABASE teste;

USE teste;

CREATE TABLE comentarios(
   numero INT AUTO_INCREMENT PRIMARY KEY,
   nome_usuario VARCHAR(50) NOT NULL, --- foreign key
   nome_produto VARCHAR(250) NOT NULL, --- foreign key
   conteudo VARCHAR(240),
   estrelas DECIMAL(6,1) NOT NULL,
   data_hora timestamp);

INSERT INTO comentarios(conteudo, estrelas) VALUES
(`insira comentário aqui`, `5.0`);
   
SELECT * FROM comentarios;
```
