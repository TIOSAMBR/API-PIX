# API-PIX

# Descrição do Código: Página de Pagamento via Pix
Este código implementa uma página de pagamento via Pix, proporcionando uma interface gráfica moderna e intuitiva para efetuar transações com QR Code. Ele faz uso de integração com a API de pagamentos para gerar o código Pix e processar o pagamento em tempo real.

# Componentes da Interface Gráfica:
**Campo de QR Code (Imagem):**
Responsável por exibir o código Pix gerado para o usuário, facilitando o pagamento por meio de aplicativos bancários ou de carteiras digitais.

**Campo de Status do Pagamento (Div):**
Exibe o status da transação em tempo real (pendente, concluído, falhado), fornecendo feedback visual para o usuário.

**Botão de Atualizar Status:**
Permite que o usuário consulte manualmente o status do pagamento, caso seja necessário, garantindo que a atualização seja feita sem precisar sair da página.

**Variáveis e Estruturas de Dados:**
qrCodeUrl (String):
Armazena a URL gerada pela API Pix para o QR Code. Utilizado para exibir a imagem correspondente no frontend.

statusPagamento (String):
Armazena o status da transação em tempo real, garantindo que o feedback sobre o sucesso ou falha da operação seja atualizado para o usuário.

transacaoId (String):
ID único associado à transação Pix, usado para consultar o status do pagamento de forma precisa junto à API de pagamentos.

# Métodos Principais:
gerarQRCode():
Faz a requisição para a API Pix, recebendo a URL do QR Code gerado e exibindo-o na tela. Este método é crucial para iniciar o processo de pagamento.

consultarStatus():
Consulta o status do pagamento através da API usando o transacaoId. Ele atualiza a interface do usuário com o status atual (ex: pagamento aprovado ou pendente).

voltarPaginaInicial():
Redireciona o usuário para a página inicial quando o pagamento é aprovado, proporcionando uma experiência de fluxo contínuo ao concluir o processo.

exibirMensagemErro():
Exibe uma mensagem de erro amigável ao usuário caso algum problema ocorra durante a geração do QR Code ou a consulta do status, como falha de conexão ou erro de servidor.

# Lógica de Pagamento e Interatividade:
A lógica principal de interação com o usuário ocorre nos métodos gerarQRCode() e consultarStatus(). Esses métodos fazem a conexão com a API de pagamentos, geram o QR Code e monitoram o status da transação, tudo em tempo real. A experiência do usuário é otimizada com atualizações automáticas e mensagens visuais claras sobre o progresso da transação.

Os métodos estão vinculados aos componentes HTML por meio de eventos de clique (onClick) que desencadeiam as funções relevantes para cada ação, garantindo que a interação com a página seja responsiva e fluida.

# Ferramentas Utilizadas:
Linguagem Backend: Python

Integração de Pagamento: API Pix (Mercado Pago / Gerencianet)

Frontend: HTML, CSS e JavaScript

Ambiente de Desenvolvimento: VSCode

# Conclusão:
Este código implementa uma solução de pagamento eficiente e moderna com Pix, permitindo uma experiência fluida e integrada para os usuários. A modularidade dos métodos e a clareza da interface garantem facilidade de manutenção e futuras melhorias. A estrutura está pronta para evoluções como a adição de novos métodos de pagamento ou melhorias na usabilidade.
