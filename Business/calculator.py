class cuilCalculator():
    def __init__(self,dni,genre):
        self.dni = dni;
        self.genre = genre;
        self.genreDigits = "00";
    
    def validateDNI(self):
        try:
            self.dni = int(self.dni);
            self.dni = abs(self.dni);#Valor absoluto, maneja errorres si es negativo 
        except ValueError:
            raise Exception('Ha ingresado letras en el DNI');
        self.dni = str(self.dni);
        long = len(self.dni);
        if(long > 8):
            raise Exception('El DNI debe ocupar como máximo 8 digitos.');
        
        cant = 8 - long;
        while(cant > 0):
            self.dni = "0" + self.dni;
            cant -= 1;
                
    def calculate(self):
        if self.genre.upper() == 'M':
            self.genreDigits = "20";
        if self.genre.upper() == 'F':
            self.genreDigits = "27";
            
        partial = self.genreDigits + self.dni;
        constants = (5,4,3,2,7,6,5,4,3,2);
        result = 0;
        i = 0;
        
        for digit in partial:
            result += constants[i] *int(digit)
            i += 1;  
            
        verifDigit = result % 11;
        if verifDigit > 1:
            verifDigit = 11 - verifDigit;
            
        if verifDigit == 1:
            self.genreDigits = "23";
            if self.genre.upper() == "M":
                verifDigit = 9;
            if self.genre.upper() == "F":
                verifDigit = 4;
            
        return self.genreDigits + "-" + self.dni + "-" + str(verifDigit);        

    def alghoritm(self):
        pass;
        #Hombre: 20
        #Mujer: 27
        #Empresa: 30
        
        # XY-12345678-VERIFICADOR