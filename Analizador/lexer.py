import re

class Lexer:
    def __init__(self):
        self.tokens = None 
    def tokenize(self, curp):
        if not curp.isupper():
            raise ValueError("CURP debe estar en mayúsculas")
        pattern = (
            r'^([A-Z]{2})([A-Z]{1})([A-Z]{1})' 
            r'(\d{2})(\d{2})(\d{2})'  
            r'([HM])'  
            r'([A-Z]{2})'  
            r'([ABCDFGHJKLMNPQRSTVWXYZ])' 
            r'([ABCDFGHJKLMNPQRSTVWXYZ])'  
            r'([ABCDFGHJKLMNPQRSTVWXYZ])' 
            r'([A-Z0-9]{2})$'  
        )
        match = re.fullmatch(pattern, curp)
        if match:
            self.tokens = {
                'apellido_paterno': match.group(1),  
                'apellido_materno': match.group(2),   
                'nombre': match.group(3),              
                'año_nacimiento': int(match.group(4)),  
                'mes_nacimiento': int(match.group(5)),   
                'dia_nacimiento': int(match.group(6)),   
                'sexo': match.group(7),
                'estado': match.group(8),
                'consonante_paterno': match.group(9),
                'consonante_materno': match.group(10),
                'consonante_nombre': match.group(11),
                'homoclave': match.group(12)
            }
        else:
            raise ValueError("CURP no válida")

    def get_tokens(self):
         return self.tokens  
