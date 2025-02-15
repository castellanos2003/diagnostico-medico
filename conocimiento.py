class SistemaExperto:
    def __init__(self):
        self.reglas = {
            frozenset(['fiebre', 'tos', 'dolor de cabeza']): {
                'enfermedad': 'Gripe',
                'descripcion': 'Una infección viral que afecta las vías respiratorias.',
                'recomendaciones': [
                    'Descansar y mantenerse hidratado',
                    'Tomar medicamentos para la fiebre si es necesario',
                    'Mantener buena higiene respiratoria',
                    'Consultar al médico si los síntomas empeoran'
                ]
            },
            frozenset(['fiebre', 'dolor de garganta', 'fatiga']): {
                'enfermedad': 'Amigdalitis',
                'descripcion': 'Inflamación de las amígdalas, puede ser viral o bacteriana.',
                'recomendaciones': [
                    'Hacer gárgaras con agua tibia y sal',
                    'Tomar abundantes líquidos',
                    'Descansar la voz',
                    'Consultar al médico para determinar si necesita antibióticos'
                ]
            },
            frozenset(['tos', 'dificultad para respirar']): {
                'enfermedad': 'Neumonía',
                'descripcion': 'Infección que inflama los sacos aéreos de los pulmones.',
                'recomendaciones': [
                    'Buscar atención médica inmediata',
                    'Seguir el tratamiento prescrito por el médico',
                    'Descansar y mantener buena hidratación',
                    'No automedicarse'
                ]
            }
        }

    def diagnosticar(self, sintomas):
        sintomas_set = frozenset([s.strip().lower() for s in sintomas])
        diagnosticos = []
        
        for regla_sintomas, info in self.reglas.items():
            if regla_sintomas.issubset(sintomas_set):
                diagnosticos.append(info)
        
        return diagnosticos if diagnosticos else [{
            'enfermedad': 'No se encontró un diagnóstico',
            'descripcion': 'Los síntomas proporcionados no coinciden con ninguna enfermedad en nuestra base de datos.',
            'recomendaciones': [
                'Consulte a un médico para una evaluación más detallada',
                'Monitoree sus síntomas',
                'Mantenga un registro de cualquier síntoma nuevo'
            ]
        }]
