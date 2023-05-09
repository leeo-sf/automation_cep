from browser_automation import Automation


navegador = Automation("https://buscacepinter.correios.com.br/app/endereco/index.php")
ceps_pesquisar = navegador._capturaDados.ReadPlanilha()
dados_capturados = [["CEP", "Logradouro", "Bairro", "Localidade"]]
for cep in ceps_pesquisar:
    if (cep.value == "Ceps"):
        continue

    navegador._capturaDados.PesquisaCep(cep.value)
    dados = navegador._capturaDados.CapturaDados()

    dados_capturados.append(dados)

navegador._capturaDados.EscreveDados(dados_capturados)
print("Dados capturados e salvos na planilha")