import requests

def get_proxies_from_url(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Erro ao obter proxies: {e}")
        return []

def test_proxy(proxy):
    test_url = "https://httpbin.org/ip"
    proxies = {
        "http": f"socks5://{proxy}",
        "https": f"socks5://{proxy}",
    }
    try:
        response = requests.get(test_url, proxies=proxies, timeout=5)
        response.raise_for_status()
        print(f"Proxy SOCKS5 funcionando: {proxy}\nResposta: {response.json()}")
        return True
    except requests.RequestException as e:
        print(f"Proxy SOCKS5 falhou: {proxy}\nErro: {e}")
        return False

if __name__ == "__main__":
    proxy_url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
    proxy_list = get_proxies_from_url(proxy_url)
    
    i = 0
    success = 0
    size = len(proxy_list)
    for proxy in proxy_list:  # Testa apenas os 10 primeiros proxies para evitar excesso de requisições
        if test_proxy(proxy):
            success += 1
            with open("proxy.txt", "a") as file:
                file.write(proxy)
        i += 1
        print(f"Testados: {i}/{size}, Sucesso: {success}")
