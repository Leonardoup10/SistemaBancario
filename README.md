# Sistema Bancario
Desafio de Sistema Bancário: um sistema simples desenvolvido em Python para gerenciar operações bancárias de um único usuário. O sistema oferece funcionalidades de depósito, saque (com limite diário) e consulta de extrato, com todas as transações e saldo sendo registrados. O código inclui validações de operação e limites de saque.
## Regras

1. **Sistema Simples**: O sistema é gerido para um único usuário.
2. **Operações**:
   - **Depósito**: Permite depósitos de valores positivos.
   - **Saque**: Permite até 3 saques diários, com limite de R$ 500,00 por saque. Caso o usuário não tenha saldo suficiente, uma mensagem será exibida.
   - **Extrato**: Exibe todos os depósitos e saques realizados, além do saldo atual.
3. **Validações**:
   - Depósitos não podem ser iguais ou menores que zero.
   - Saques não podem exceder o limite diário ou o saldo disponível.
