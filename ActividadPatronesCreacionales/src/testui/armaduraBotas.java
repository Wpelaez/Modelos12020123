
package testui;


public class armaduraBotas extends armadura{
    
}

class armaduraBotasElfo extends armaduraBotas{
    public armaduraBotasElfo() {
        super.setAtaque(10);
        super.setDescripcion("Botas Elfo");
        super.setResistencia(20);
    }
}

class armaduraBotasOrco extends armaduraBotas{
    public armaduraBotasOrco() {
        super.setAtaque(5);
        super.setDescripcion("Botas Orco");
        super.setResistencia(5);
    }
}

class armaduraBotasEnano extends armaduraBotas{
    public armaduraBotasEnano() {
        super.setAtaque(2);
        super.setDescripcion("Botas Enano");
        super.setResistencia(2);
    }
}

class armaduraBotasHumano extends armaduraBotas{
    public armaduraBotasHumano() {
        super.setAtaque(20);
        super.setDescripcion("Botas Humano");
        super.setResistencia(50);
    }
}