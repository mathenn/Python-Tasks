
import numpy as np

participantes = [
    {
        "nome": "Alice",
        "localizacao": "EUA",
        "afiliacao": "Universidade A",
        "interesses": ["Física", "Astronomia"]
        },

        {
            "nome": "Matheus",
            "localizacao": "Brasil",
            "afiliacao": "Universidade B",
            "interesses": ["Eng software", "CS"]
        },

        {
            "nome": "Joao",
            "localizacao": "Brasil",
            "afiliacao": "Universidade B",
            "interesse": ["Física"]
        },

        {
            "nome": "Pierre",
            "localizacao": "Italy",
            "afiliacao": "Universidade C",
            "interesses": ["Astronomia", "Eng software"]
        }
    ]

afiliacoes = {}
for participante in participantes:
    afiliacao = participante["afiliacao"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
        afiliacoes[afiliacao].append(participante["nome"])














