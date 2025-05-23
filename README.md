# Plataforma Digital Segura

Sistema de ensino com autenticação, níveis de acesso (aluno, professor, admin), atividades, envio de projeto final e geração de relatórios de desempenho.

---

## Requisitos

- **Python 3** instalado no computador.
  - Baixe em: [https://www.python.org/downloads/](https://www.python.org/downloads/)
  - Durante a instalação, marque a opção **"Add Python to PATH"**.

---

## Como executar

1. Abra o terminal (Prompt de Comando ou PowerShell no Windows).
2. Navegue até a pasta do projeto.
3. Execute o comando:
   ```bash
   python main.py
   ```
4. **Registre um usuário** ou faça login.
5. O menu será exibido conforme o nível de acesso:
   - **Aluno:** ver conteúdos, fazer atividades, acessar e baixar relatório de desempenho.
   - **Professor:** consultar relatórios dos alunos.
   - **Admin:** gerenciar usuários e professores.

---

## Cadastro de Usuários e Níveis de Acesso

- Para se cadastrar como **professor**, utilize o código:
  ```
  prof123
  ```
- Para se cadastrar como **admin**, utilize o código:
  ```
  admin123
  ```
- Se não informar nenhum código, o usuário será cadastrado como **aluno**.

---

## Estrutura do Projeto

- `main.py`: ponto de entrada do sistema.
- `autenticacao/`: login, registro e alteração de senha.
- `aluno/`: conteúdos, atividades e relatórios dos alunos.
- `relatorios/`: respostas e relatórios gerados.
- `atividades/`: questões das atividades (arquivos `.json`).
- `util/`: funções utilitárias (ex: segurança, limpeza de tela).

---

## Funcionalidades

- **Cadastro e login** com senha protegida por hash.
- **Níveis de acesso**: aluno, professor e admin.
- **Atividades** para alunos, com correção automática.
- **Relatórios detalhados** de desempenho dos alunos.
- **Download de relatório** em `.txt` para a pasta Downloads.
- **Professores** podem consultar relatórios de qualquer aluno.
- **Admins** podem visualizar e gerenciar usuários.

---

## Observações

- Os relatórios dos alunos são salvos em `relatorios/relatorios_txt`.
- O sistema é multiplataforma, mas os caminhos de arquivos estão configurados para Windows.
- Para rodar, é necessário ter o Python 3 instalado.

---

## Instalação de Dependências

Este projeto não utiliza bibliotecas externas além da biblioteca padrão do Python.

---

Se precisar de exemplos de uso, instruções para rodar em outros sistemas ou mais detalhes, é só pedir!