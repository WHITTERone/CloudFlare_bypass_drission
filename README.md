# CloudFlare_bypass_drission
Estou tentando criar um codigo pra passar o desafio de turnstile do cloudflare

Atualmente o turnstile do cloudflare consiste em um checkbox que esta dentro de um shadow-root (closed) que esta dentro de um iframe que esta dentro de um shadow-root (closed)

Eu consegui deixar o primeiro shadow-root como open, porem, n estou conseguindo deixar o shadow-root que esta dentro de iframe como open mas estou com ideias, como por exemplo estou usando a biblioteca drissio para tentar injetar um codigo javascript para forcar o shadow-root a ser open
