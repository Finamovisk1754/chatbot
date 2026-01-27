# 🤖 Chatbot de Atendimento Virtual

**Autores:** 🧑‍💻 Matheus Finamor & Tiago Ferreira  

Este projeto consiste em um **chatbot de atendimento virtual** desenvolvido em Python.  
Ele simula um atendimento automatizado para suporte de internet, Wi-Fi, consulta de planos e encaminhamento para um atendente humano.

---

## 📋 Funcionalidades do Chatbot

O chatbot oferece as seguintes funcionalidades:

1. **Problemas com a Internet** – Sugere soluções como verificação de cabo de rede, reinício de modem/roteador e checagem do provedor.  
2. **Problemas com o Wi-Fi** – Orienta sobre ativação do Wi-Fi, conexão correta e reinício do roteador.  
3. **Falar com um atendente** – Simula a transferência para um atendente humano.  
4. **Consultar planos** – Mostra os planos disponíveis e seus preços.  
5. **Encerrar atendimento** – Finaliza o atendimento de forma amigável.

---

## ⚙️ Estrutura do Código

O código é organizado em **funções separadas**, facilitando manutenção e expansão:

- `exibir_menu()` – Mostra o menu principal.  
- `problemas_internet()` – Exibe soluções para problemas de internet.  
- `problemas_wifi()` – Exibe soluções para problemas de Wi-Fi.  
- `falar_com_atendente()` – Simula transferência para atendente humano.  
- `consultar_planos()` – Lista os planos disponíveis.  
- `encerrar_atendimento()` – Finaliza o chatbot.  
- `chatbot()` – Função principal que executa o loop de interação com o usuário.

---

## 💻 Como Executar

1. Certifique-se de ter o **Python 3** instalado no seu computador.  
2. Clone o repositório ou baixe o código `.py`.  
3. Abra o terminal e navegue até a pasta do projeto.  
4. Execute o arquivo:

```bash
python chatbot.py
