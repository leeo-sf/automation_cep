from browser_automation import Automation


navegador = Automation("https://buscacepinter.correios.com.br/app/endereco/index.php")
navegador._capturaDados.PesquisaCep("06360130")