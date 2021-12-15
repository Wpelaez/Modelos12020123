
package testui;

public class principal {

    public static void main(String[] args) {
        Interfaz ventanaPrincipal = new Interfaz();
        fabricaAbs fabrica;
        String descripcionPersonaje;
        armaduraPecho armPecho;    
        armaduraPantalon armPantalon;
        armaduraBotas armBotas;
        int resistenciaTotal;
        int ataqueTotal;
        
        int veces = 0;
        do{
            while(! ventanaPrincipal.isGenerar()){
                sleep(500);
                //System.out.println("No se ha Escojido Nada");
            }
            ventanaPrincipal.setGenerar(false);
            System.out.println("Personaje Escojido: " + ventanaPrincipal.getPersonajeEscojido());
            System.out.println("Cantidad Escojida: " + ventanaPrincipal.getCantidadEscojida());
            //veces ++;
            switch(ventanaPrincipal.getPersonajeEscojido()){
                case "Elfo":{
                    fabrica = new fabricaElfo();
                    break;
                }
                case "Humano":{
                    fabrica = new fabricaHumano();
                    break;
                }
                case "Orco":{
                    fabrica = new fabricaOrco();
                    break;
                }
                case "Enano":{
                    fabrica = new fabricaEnano();
                    break;
                }
                default:{
                    fabrica = new fabricaElfo();
                    break;
                }
            }
            descripcionPersonaje = fabrica.colocarDescripcion();
            armBotas = fabrica.colocarArmBotas();
            armPantalon = fabrica.colocarArmPantalon();
            armPecho = fabrica.colocarArmPecho();
            resistenciaTotal = armBotas.getResistencia() + armPantalon.getResistencia() + armPecho.getResistencia();
            ataqueTotal = armBotas.getAtaque()+ armPantalon.getAtaque() + armPecho.getAtaque();

            System.out.println("Descripcion: " + descripcionPersonaje);
            System.out.println("Ataque: " + ataqueTotal);
            System.out.println("Resistencia: " + resistenciaTotal);
            System.out.println("Descripcion Botas: " + armBotas.getDescripcion());
            System.out.println("Descripcion Armadura Pecho: " + armPecho.getDescripcion());
            System.out.println("Descripcion Armadura Pantalon: " + armPantalon.getDescripcion());
            
            ventanaPrincipal.ponerDatos(descripcionPersonaje, resistenciaTotal, ataqueTotal,
                                        armPecho.getDescripcion(), armPecho.getResistencia(), armPecho.getAtaque(), 
                                        armBotas.getDescripcion(), armBotas.getResistencia(), armBotas.getAtaque(),
                                        armPantalon.getDescripcion(), armPantalon.getResistencia(), armPantalon.getAtaque());
            //hacer copias
            fabricaAbs[] arrayFabricas = new fabricaAbs[ventanaPrincipal.getCantidadEscojida()];
            for(int i=0; i<ventanaPrincipal.getCantidadEscojida();i++){
                arrayFabricas[i] = fabrica.hacerCopia();//Uso de prototype
            }
            ventanaPrincipal.agregarDibujos(arrayFabricas);
        }while(veces < 100);
    }
    
    
    public static void sleep(int time){
        try{
            Thread.sleep(time);
        }catch (Exception e){}
    } 
}
