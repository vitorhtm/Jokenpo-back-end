import random


class Jogo:
    def jogar(self, jogada):

        ganha_de = {
            "tesoura": ["papel", "lagarto"],
            "papel": ["pedra", "spock"],
            "pedra": ["tesoura", "lagarto"],
            "lagarto": ["spock", "papel"],
            "spock": ["tesoura", "pedra"],
        }

        computador = random.choice(["tesoura", "papel", "pedra", "spock", "lagarto"])

        resposta = {
            "jogada": f"VC {jogada} | PC {computador}",
            "mensagem": None,
            "vencedor": None,
            "pc": computador,
        }

        if computador == jogada:
            resposta["mensagem"] = f"Jogo empatou"

        elif jogada in ganha_de[computador]:
            resposta["mensagem"] = self.mensagens(computador, jogada)
            resposta["vencedor"] = "PC"
        else:
            resposta["mensagem"] = self.mensagens(jogada, computador)
            resposta["vencedor"] = "VC"

        return resposta

    def mensagens(self, jogada1, jogada2):
        lista_mensagens = {
            "tesoura": {
                "papel": "Tesoura corta papel",
                "lagarto": "Tesoura decapita lagarto",
            },
            "papel": {
                "pedra": "Papel cobre pedra",
                "spock": "Papel refuta Spock",
            },
            "pedra": {
                "lagarto": "Pedra esmaga lagarto",
                "tesoura": "Pedra amassa tesoura",
            },
            "lagarto": {
                "spock": "Lagarto envenena Spock",
                "papel": "Lagarto come papel",
            },
            "spock": {
                "tesoura": "Spock derrete Tesoura ",
                "pedra": "Spock vaporiza pedra",
            },
        }
        return lista_mensagens[jogada1][jogada2]
