
package testui;

public class armaduraPecho extends armadura{

}

class armaduraPechoElfo extends armaduraPecho{
    public armaduraPechoElfo() {
        super.setAtaque(100);
        super.setDescripcion("Pecho Elfo");
        super.setResistencia(50);
    }
}

class armaduraPechoOrco extends armaduraPecho{
    public armaduraPechoOrco() {
        super.setAtaque(100);
        super.setDescripcion("Pecho Orco");
        super.setResistencia(10);
    }
}

class armaduraPechoEnano extends armaduraPecho{
    public armaduraPechoEnano() {
        super.setAtaque(10);
        super.setDescripcion("Pecho Enano");
        super.setResistencia(10);
    }
}

class armaduraPechoHumano extends armaduraPecho{
    public armaduraPechoHumano() {
        super.setAtaque(200);
        super.setDescripcion("Pecho Humano");
        super.setResistencia(500);
    }
}


