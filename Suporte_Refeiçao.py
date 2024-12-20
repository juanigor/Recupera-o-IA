import google.generativeai as genai

from google.colab import userdata

GOOGLE_GEMINI_API_KEY = userdata.get("Googleapi")

genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

chat = model.start_chat(history=[])

prompt = input("Esperando prompt: ")

prompt = f"""
    
    Você é um chatbot especializado em auxiliar na organização das refeições diárias. Sua função é: 

- **Horários:** Sugerir os melhores horários para cada refeição, ajudando o usuário a manter uma rotina alimentar equilibrada.  
- **Sugestões de refeições:** Indicar opções saudáveis e apropriadas para cada horário do dia, considerando os benefícios nutricionais e as preferências do usuário. 

Seu objetivo é promover uma alimentação balanceada e auxiliar na construção de hábitos saudáveis.
     {input}
    """


while prompt != "sair":
    response = chat.send_message(prompt)
    print(response.text)
    prompt = input("Esperando prompt: ")