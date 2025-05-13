### services/compatibilidade.py

def calcular_compatibilidade(pet: dict, adotante: dict) -> int:
    pontos = 0

    desejado = adotante.get("caracteristicas_desejadas", {})
    necessidades = pet.get("necessidades", {})
    social = pet.get("social", {})

    # Espécie
    if pet.get("especie") == desejado.get("especie"):
        pontos += 20
    else:
        pontos -= 20

    # Porte
    if pet.get("porte") == desejado.get("porte"):
        pontos += 10
    else:
        pontos -= 10

    # Sexo
    if pet.get("sexo") == desejado.get("sexo"):
        pontos += 5
    else:
        pontos -= 5

    # Tratamento contínuo ou necessidades especiais
    if necessidades.get("tratamento_continuo") or necessidades.get("necessidades_especiais"):
        if desejado.get("aceita_necessidades"):
            pontos += 10
    else:
        if desejado.get("aceita_necessidades"):
            pontos += 5
        else:
            pontos += 10

    # Doença crônica
    if not necessidades.get("doenca_cronica", False):
        if not desejado.get("aceita_doenca_cronica", True):
            pontos += 5
    else:
        if desejado.get("aceita_doenca_cronica", False):
            pontos += 10

    # Social - fatores impeditivos
    if social.get("com_outros_animais") is False and desejado.get("possui_outros_animais"):
        return -9999
    if social.get("exige_cuidados_constantes") and not desejado.get("tempo_disponivel"):
        return -9999

    # Pontos adicionais de socialização
    if social.get("com_outros_animais") and desejado.get("possui_outros_animais"):
        pontos += 5
    if social.get("exige_cuidados_constantes") and desejado.get("tempo_disponivel"):
        pontos += 5

    return pontos
