from conocimiento import SistemaExperto

def obtener_diagnostico(sintomas_usuario):
    sistema = SistemaExperto()
    return sistema.diagnosticar(sintomas_usuario)
