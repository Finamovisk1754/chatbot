import time

#Matheus Finamor --- Tiago Ferreira

def exibir_menu():
    print("Bom dia! Bem-vindo ao nosso atendimento virtual.")
    print("Por favor, selecione uma das opções abaixo:")
    print("1. Problemas com a Internet")
    print("2. Problemas com o Wi-Fi")
    print("3. Falar com um atendente")
    print("4. Consultar planos")
    print("5. Encerrar atendimento")

def problemas_internet():
    print("Vejo que você está com problemas na internet. Vamos tentar algumas soluções:")
    print("1. Verifique se o cabo de rede está conectado corretamente.")
    print("2. Reinicie o modem e o roteador.")
    print("3. Verifique se há algum problema com o seu provedor de internet.")

def problemas_wifi():
    print("Problemas com o Wi-Fi? Tente as seguintes etapas:")
    print("1. Verifique se o Wi-Fi está ativado no seu dispositivo.")
    print("2. Certifique-se de que está conectado à rede Wi-Fi correta.")
    print("3. Reinicie o roteador.")

def falar_com_atendente():
    print("Aguarde um momento. Estamos transferindo você para um atendente humano...")
    print("Conectando com o atendente...")

def consultar_planos():
    print("Aqui estão as informações dos seus planos:")
    print("1. Plano Básico: 100 Mbps - R$ 79,90/mês")
    print("2. Plano Avançado: 300 Mbps - R$ 129,90/mês")
    print("3. Plano Premium: 600 Mbps - R$ 199,90/mês")
    print("Para mais informações, entre em contato com o nosso atendimento.")

def encerrar_atendimento():
    print("Obrigado por utilizar nosso atendimento. Até logo!")
    return True

def chatbot():
    while True:
        exibir_menu()
        escolha = input("Digite o número correspondente à sua escolha ou descreva o problema: ").lower()

        if "1" in escolha or "internet" in escolha or "rede" in escolha:
            problemas_internet()
        
        elif "2" in escolha or "wifi" in escolha or "conexão" in escolha:
            problemas_wifi()
        
        elif "3" in escolha or "falar com atendente" in escolha:
            falar_com_atendente()

        elif "4" in escolha or "consultar planos" in escolha or "planos" in escolha:
            consultar_planos()

        elif "5" in escolha or "sair" in escolha or "encerrar" in escolha or "exit" in escolha:
            if encerrar_atendimento():
                break  

        else:
            print("Desculpe, não entendi sua solicitação. Por favor, tente novamente.")
        
        time.sleep(3)
        print("\n--- Conexão encerrada ---\n")

# Executar o chatbot
chatbot()
