
package testui;


public class armaduraPantalon extends armadura{

}

class armaduraPantalonElfo extends armaduraPantalon{
    public armaduraPantalonElfo() {
        super.setAtaque(20);
        super.setDescripcion("Pantalon Elfo");
        super.setResistencia(50);
    } 
}

class armaduraPantalonOrco extends armaduraPantalon{
    public armaduraPantalonOrco() {
        super.setAtaque(10);
        super.setDescripcion("Pantalon Orco");
        super.setResistencia(10);
    } 
}

class armaduraPantalonEnano extends armaduraPantalon{
    public armaduraPantalonEnano() {
        super.setAtaque(5);
        super.setDescripcion("Pantalon Enano");
        super.setResistencia(5);
    } 
}

class armaduraPantalonHumano extends armaduraPantalon{
    public armaduraPantalonHumano() {
        super.setAtaque(20);
        super.setDescripcion("Pantalon Humano");
        super.setResistencia(50);
    } 
}