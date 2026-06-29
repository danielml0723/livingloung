def calculate_payroll(data):

    salario_mensual = data["salario_mensual"]

    # base
    salario_diario = salario_mensual / 30
    salario_hora = salario_diario / 8

    # devengados
    salario_bruto = data["horas_bruto"] * salario_hora
    convenio = data["convenio_horas"] * salario_hora
    extra15 = data["extra15_horas"] * salario_hora * 1.5
    extra2 = data["extra2_horas"] * salario_hora * 2
    feriado = data["feriado_horas"] * salario_hora
    feriado2 = data["feriado2_horas"] * salario_hora * 2

    total_devengado = (
        salario_bruto +
        convenio +
        extra15 +
        extra2 +
        feriado +
        feriado2 +
        data["comisiones"]
    )

    # deducciones base Costa Rica
    sem = total_devengado * 0.055
    ivm = total_devengado * 0.0433
    banco = total_devengado * 0.01

    total_deducciones = sem + ivm + banco + data["renta"] + data["embargos"]

    salario_neto = total_devengado - total_deducciones

    return {
        "salario_hora": salario_hora,

        "devengados": {
            "salario_bruto": salario_bruto,
            "convenio": convenio,
            "extra15": extra15,
            "extra2": extra2,
            "feriado": feriado,
            "feriado2": feriado2,
        },

        "total_devengado": total_devengado,

        "deducciones": {
            "sem": sem,
            "ivm": ivm,
            "banco": banco,
            "renta": data["renta"],
            "embargos": data["embargos"],
            "total": total_deducciones
        },

        "salario_neto": salario_neto
    }