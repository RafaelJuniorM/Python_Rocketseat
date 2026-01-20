
## Métodos de requisição HTTP 

Métodos HTTP são comandos (verbos) que definem a ação que um cliente (navegador) deseja realizar em um servidor.

| Metodos         |  Função                                                   |
|:-----           |:--------:                                                 |
| GET             | Solicita dados de um recurso.                             |
| POST            | Envia dados para o servidor para criar um novo recurso ou processar informações (ex: envio de                               formulário). |  
| PUT             | Atualiza ou substitui um recurso existente por completo.  |
| DELETE          | Remove um recurso específico do servidor.                 |  
| PATCH           | Aplica modificações parciais a um recurso.                |


## Codigo de Status re respostas HTTP 

- Respostas Informativas ( 100 - 199 )
- Respostas bem sucedidas ( 200 - 299 )
- Mensagens de redirecionamento ( 300 - 399 )
- Respostas de erro do cliente ( 400 - 499 )
- Respostas de erro do servidor ( 500 - 599 )


## Exemplo de como funciona 

1. O cliente envia requisição: Um navegador ou aplicativo envia uma requisição HTTP para um servidor
2. Servidor Processa:  O servidor identifica o metodo (GET) e o recurso (/produtos/123) e executa a ação.
3. Servidor retorna resposta: O servidor envia uma resposta HTTP, incluindo um codigo de status e opciionalmente os dados solicitados (json, xml, html)

## Documentação da API - Swagger

