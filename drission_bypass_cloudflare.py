from DrissionPage import ChromiumPage, ChromiumOptions
from bs4 import BeautifulSoup
from time import sleep

browser_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

options = ChromiumOptions()
options.set_paths(browser_path=browser_path)

arguments = [
    "-no-first-run",
    "-force-color-profile=srgb",
    "-metrics-recording-only",
    "-password-store=basic",
    "-use-mock-keychain",
    "-export-tagged-pdf",
    "-no-default-browser-check",
    "-disable-background-mode",
    "-enable-features=NetworkService,NetworkServiceInProcess,LoadCryptoTokenExtension,PermuteTLSExtensions",
    "-disable-features=FlashDeprecationWarning,EnablePasswordsAccountStorage",
    "-deny-permission-prompts",
    "-disable-gpu"
    # "-headless=new"
    # "-incognito"
    # "-user-data-dir=D:\\System\\Desktop\\Undetected\\Drission_Dennis\\tmp\\"
]

for argument in arguments:
    options.set_argument(argument)

driver = ChromiumPage(options)
driver.get('https://forum.cfcybernews.eu/')

# Aguardar um pouco para garantir que a página e os elementos sejam carregados
sleep(5)

# Abre o shadow-root
script_open_shadow = """
    Element.prototype._as = Element.prototype.attachShadow;
    Element.prototype.attachShadow = function (params) {
        return this._as({mode: "open"});
    };
"""

driver.run_js(script_open_shadow)

# Encontre o shadow host
shadow_host = driver.ele('x://*[@id="MDjtu6"]/div/div/div')

# Verifique se o shadow host foi encontrado
if shadow_host:
    sr = shadow_host.shadow_root
    
    # Aguarde um pouco para garantir que o shadow-root esteja completamente carregado
    sleep(2)

    sr_html = sr.html
    soup_sr = BeautifulSoup(sr_html, 'html.parser')
    formatted_html_sr = soup_sr.prettify()
    print("HTML do shadow-root:")
    print(formatted_html_sr)

    # Encontre o iframe dentro do shadow-root
    iframe = sr.child()
    iframe.run_js(script_open_shadow)

    if iframe:
        print("Iframe encontrado:")
        iframe.run_js(script_open_shadow)
    else:
        print("Iframe não encontrado dentro do shadow-root.")
else:
    print("Shadow host não encontrado.")

sleep(10)
