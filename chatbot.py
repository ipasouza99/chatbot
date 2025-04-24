import openai

# passando a chave da API
openai.api_key = 'SUA_CHAVE_API'
messages =[]

while True:

#obter entrada do usuário
    entrada = input('Digite sua pesquisa : ')
    if entrada == 'sair':
        exit()

# definindo o prompt
    message = {'role': 'user', 'content': entrada} 
    messages.append(message)

    
# chamando a API
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages,temperature=1,n=2,max_tokens=100)

# imprimindo a resposta
    print(response.choices[0].message.content)

    


