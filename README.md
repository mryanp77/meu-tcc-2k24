# PASSOS PARA VISUALIZAR O PROJETO:
## INSTALAR PYTHON 3.7.6:
- https://www.python.org/downloads/release/python-376/

## CLONAR O PROJETO DO GITHUB DO TCC:
- git clone https://github.com/mryanp77/meu-tcc-2k24

## ABRIR O TERMINAL E EXECUTAR O COMANDO PARA INSTALAR AS DEPENDÊNCIAS:
- python -m pip install -r requirements.txt

## INSTALAR O BABEL
- pip install babel

## PARA ABRIR O SERVIDOR DO TCC, SÓ DIGITAR:
- py manage.py makemigrations
- py manage.py migrate
- py manage.py runserver

## ACESSAR A URL DO PROJETO:
http://127.0.0.1:8000/

## PARA A PÁGINA DE CONTATO FUNCIONAR:
- EMAIL_HOST_USER = 'email-do-host@gmail.com'
- EMAIL_HOST_PASSWORD = 'senha do email gerada pela google (https://myaccount.google.com/apppasswords)'
- EMAIL_RECEIVING_USER = 'email-de-quem-vai-receber-as-mensagens@gmail.com'


# RESUMO BÁSICO:
## PROFESSORES
Primeiro, o professor se candidatará ao emprego. Se ele for selecionado, suas contas serão criadas e aprovadas pelo administrador. Somente após a aprovação, o professor poderá acessar seu painel. Depois que a conta for aprovada pelo administrador, o professor poderá registrar a frequência de qualquer turma e visualizá-la posteriormente. O professor
também pode publicar/anunciar avisos aos alunos, como a entrega de tarefas.

## ESTUDANTES
Primeiro, o aluno fará a inscrição/cadastro. Quando sua conta for aprovada pelo administrador, somente então o aluno poderá acessar seu painel. Após a aprovação da conta pelo administrador, o aluno poderá visualizar seus detalhes, como a frequência. O aluno não pode visualizar a frequência de outros alunos. O aluno não pode fazer anúncios, apenas visualizá-los.

## ADMINISTRADOR
Primeiro, o administrador se registrará para criar uma conta. Após o login, ele poderá ver quantos alunos/professores desejam se inscrever ou trabalhar na escola. O administrador pode aprovar ou excluir/cancelar as solicitações. Ele também pode atualizar os detalhes de qualquer aluno ou professor. O administrador pode fazer anúncios de avisos também.

## PONTOS NEGATIVOS:
- Na página de atualização de professores/alunos, a senha deve ser atualizada.
- Qualquer pessoa pode se tornar um administrador.


# TUTORIAL GITHUB | ATUALIZAR ARQUIVOS:
## Navegue até o diretório do projeto;

## Verifique o status dos arquivos:
- git status

## Adicione os arquivos que deseja atualizar:
- git add .

## Faça um commit das suas mudanças:
- git commit -m "Sua mensagem de commit aqui"

## Atualize seu repositório remoto:
- git push origin main

## Se você tiver alterações no repositório remoto que não estão na sua máquina local, pode ser necessário fazer um pull antes:
- git pull origin main
