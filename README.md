# CeubLivre-API

## Interações

Este microsserviço gerencia as avaliações e comentários deixados pelos usuários sobre os produtos comprados, assim como
perguntas e repostas.


### #2 - Gerenciamento de comentários (2 pontos)

Permitir que os usuários possam comentar nas avaliações de outros usuários.

---
```
CREATE TABLE comentarios(
   numero INT AUTO_INCREMENT PRIMARY KEY,
   nome_usuario VARCHAR(50) NOT NULL, --- foreign key
   comentario NOT NULL, --- foreign key
   conteudo VARCHAR (240) NOT NULL,
   estrelas DECIMAL (6,1) NOT NULL)
   data_hora timestamp;
   
   ```
