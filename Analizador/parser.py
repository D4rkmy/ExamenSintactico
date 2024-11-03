import re
from datetime import datetime

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.curp_pattern = re.compile(r'^[A-Z]{4}\d{6}[HM][A-Z]{5}[0-9A-Z]{2}$')

    def parse(self, curp):
        if not self.validate_format(curp):
            raise ValueError("Formato de CURP no válido")

        self.lexer.tokenize(curp)
        tokens = self.lexer.get_tokens()  

        tokens['año_nacimiento'] = self.adjust_year(tokens['año_nacimiento'])

        if not self.validate_date(tokens['año_nacimiento'], tokens['mes_nacimiento'], tokens['dia_nacimiento']):
            raise ValueError("Fecha de nacimiento no válida en la CURP")

        total_letras = sum(c.isalpha() for c in curp) 
        total_numeros = sum(c.isdigit() for c in curp)  
        
        tokens['total_letras'] = total_letras
        tokens['total_numeros'] = total_numeros

        print(f"Analizando CURP: {curp}")
        print(f"Componentes extraídos: {tokens}")

        return tokens 
    
    def validate_format(self, curp):
        return bool(self.curp_pattern.match(curp))

    def adjust_year(self, year):
        if year >= 50:
            return 1900 + year
        else:
            return 2000 + year

    def validate_date(self, year, month, day):
        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False
