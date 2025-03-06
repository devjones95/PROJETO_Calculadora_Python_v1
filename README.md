Como funciona o esqueleto da nossa calculadora, lembrando que foi usado apenas Python para a parte lógica, pois o projeto está em fase de criação.

1. **Início do loop while**:  
   O while True: cria um loop infinito, ou seja, o programa ficará em execução até que o usuário decida sair, usando um comando de saída.

2. **Coleta de dados**:  
   O programa solicita ao usuário que insira dois números e um operador. Ele utiliza a função `input()` para capturar essas entradas:
   - numero_1 e numero_2 são os números que o usuário deseja usar na operação.
   - operador é o operador matemático que o usuário escolhe (como soma, subtração, etc.).

3. **Conversão de entrada para número**:  
   Dentro do try-except o código tenta converter os valores inseridos pelo usuário (numero_1 e numero_2) de strings para float. Isso é feito com float(numero_1) e float(numero_2). Caso o usuário insira algo que não possa ser convertido para número (como letras ou símbolos), o programa entra no bloco except, onde a variável numeros_validos é setada como False.

4. **Validação dos números**:  
   O código verifica se os números são válidos, com a condição if not numeros_validos:. Se os números não forem válidos, o código imprime a mensagem `'Um ou ambos os números digitados são inválidos. e o loop reinicia com continue.

5. **Validação do operador**:  
   O código valida o operador inserido pelo usuário, comparando-o com os operadores permitidos (+-/*). Caso o operador inserido não seja um desses, o programa imprime Operador inválido; e reinicia o loop. Além disso, há uma verificação para garantir que o usuário não digite mais de um operador. Se o comprimento do operador for maior que 1, o código avisa o usuário e reinicia o loop.

6. **Execução da operação matemática**:  
   Se todas as validações forem passadas, o programa executa a operação solicitada:
   - Se o operador for +, realiza a soma.
   - Se for '-', realiza a subtração.
   - Se for '*', realiza a multiplicação.
   - Se for '/', realiza a divisão.
   O resultado é exibido ao usuário de forma formatada com a mensagem 'O resultado da operação é: '.

7. **Validação de erro**:  
   Caso o código falhe em algum ponto da validação, um `else` está preparado para capturar esse erro e imprimir 'Algum erro conseguiu passar nas validações. Revise seu código.'. Isso ajuda a identificar falhas caso o código deixe passar algum valor não válido.

8. **Solicitação de saída**:  
   Após exibir o resultado, o programa pergunta ao usuário se ele deseja sair da calculadora. A função input() é usada para capturar a resposta. Se a resposta começar com a letra 's' (independente de ser maiúscula ou minúscula), o programa interrompe o loop com o break. Isso é feito utilizando o método .lower() para tornar a resposta em minúsculas e .startswith('s') para verificar se a resposta começa com a letra 's' (permitindo respostas como "s", "S", "sim", "SIM", "Sair").

9. **Saída do loop**:  
   Se o usuário digitar uma resposta que indica que deseja sair (como 's' ou 'sim'), o loop é interrompido e o programa termina.

Esse fluxo é repetido até que o usuário escolha sair da calculadora.
