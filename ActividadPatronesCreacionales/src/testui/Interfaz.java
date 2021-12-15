
package testui;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JLayeredPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextPane;
import javax.swing.border.Border;

public class Interfaz implements ActionListener{
    
    private JFrame ventanaPrincipal;
    private JLayeredPane panelPrincipal, panelGenerador, panelDescripcion, panelDibujo;
    private JPanel ContendorDibujos = new JPanel();
    private JLabel panelTextoArmaduraPecho, panelTextoArmaduraPantalon, panelTextoArmaduraBotas;
    private JLabel panelTextoDescripcion;
    private JLabel tituloGenerador;
    private JLabel tituloDescripcion, tituloArmaduraPecho, tituloArmaduraPantalon, tituloArmaduraBotas;
    private JTextPane descripcion  = new JTextPane();
    private JTextArea descripcionArmaduraPecho = new JTextArea(), descripcionArmaduraBotas = new JTextArea();
    private JTextArea descripcionArmaduraPantalon = new JTextArea();
    private JScrollPane contenedorDescripcion = new JScrollPane(descripcion);
    private JComboBox seleccionable, cantidad;
    private JButton botonGenerar;
    private JLabel marcoPanelGeneradorLabel;
    private ImageIcon marcoPanelGeneradorImagen, marcoPanelDescripcionImagen;
    private ImageIcon marcoPanelPecho, marcoPanelBotas, marcoPanelPantalon;
    private String personajeEscojido = "";
    private int cantidadEscojida = 0;
    private boolean generar = false;
    private String fuente = "NewsGoth BT";
    private String fuente2 = "";
    
    public Interfaz(){
        iniciarVentanaPrincipal();
        crearPanelPrincipal();
        crearPanelGenerador();
        crearPanelDescripcion();
        crearPanelDibujo();
        
        ventanaPrincipal.add(panelPrincipal);
        ventanaPrincipal.setVisible(true);
    }
    
    private void iniciarVentanaPrincipal(){
        ventanaPrincipal = new JFrame();
        ventanaPrincipal.setTitle("Ejemplo Modelos 1");
        ventanaPrincipal.setSize(1000, 850);
        ventanaPrincipal.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventanaPrincipal.setResizable(false);
        ventanaPrincipal.setLocationRelativeTo(null);
    }
    
    private void crearPanelPrincipal(){
        panelPrincipal = new JLayeredPane();
        panelPrincipal.setBounds(0, 0, 1000, 800);
        //panelPrincipal.setBackground(Color.red);
        panelPrincipal.setOpaque(true);
    }
    
    private void crearPanelGenerador(){
        panelGenerador = new JLayeredPane();
        panelGenerador.setBounds(0, 0, 1000, 133);
        panelGenerador.setBackground(Color.green);
        panelGenerador.setOpaque(true);
        componentesPanelGenerador();
        panelPrincipal.add(panelGenerador, Integer.valueOf(0));
    }
    
    private void crearPanelDescripcion(){
        panelDescripcion = new JLayeredPane();
        panelDescripcion.setBounds(0, 133, 425, ventanaPrincipal.getHeight());
        //panelDescripcion.setBackground(Color.blue);
        panelDescripcion.setOpaque(true);
        componentesPanelDescripcion();
        panelPrincipal.add(panelDescripcion, Integer.valueOf(0));
    }
        
    private void crearPanelDibujo(){
        panelDibujo = new JLayeredPane();
        panelDibujo.setBounds(425, 133, ventanaPrincipal.getWidth() - 400, ventanaPrincipal.getHeight() - 163);
        //panelDibujo.setBackground(Color.white);
        panelDibujo.setOpaque(true);
        componentesPanelDibujo();
        panelPrincipal.add(panelDibujo, Integer.valueOf(0));
    }
    
    private void componentesPanelGenerador(){
        //Marco
        marcoPanelGeneradorLabel = new JLabel();
        marcoPanelGeneradorLabel.setBounds(0, 0, panelGenerador.getWidth(), panelGenerador.getHeight());
        marcoPanelGeneradorImagen = new ImageIcon("marcoGenerador.jpg");
        Image imagen = marcoPanelGeneradorImagen.getImage();
        imagen = imagen.getScaledInstance(marcoPanelGeneradorLabel.getWidth(), 
                                            marcoPanelGeneradorLabel.getHeight(),  java.awt.Image.SCALE_SMOOTH);
        marcoPanelGeneradorImagen = new ImageIcon(imagen);
        marcoPanelGeneradorLabel.setIcon(marcoPanelGeneradorImagen);
        panelGenerador.add(marcoPanelGeneradorLabel, Integer.valueOf(0));
        //Texto
        tituloGenerador = new JLabel("Escoja Personaje y Cantidad");
        tituloGenerador.setBounds(260, 20, 400, 40);
        tituloGenerador.setHorizontalAlignment(JLabel.CENTER);
        tituloGenerador.setFont(new Font(fuente, Font.PLAIN, 30));
        //tituloGenerador.setBackground(Color.black);
        tituloGenerador.setOpaque(true);
        panelGenerador.add(tituloGenerador, Integer.valueOf(1));
        //TerminaTexto
        //Desplegable
        String[] Personajes = {"Elfo", "Humano", "Orco", "Enano"};
        seleccionable = new JComboBox(Personajes);
        seleccionable.setBounds(100, 63, 370, 40);
        seleccionable.setFont(new Font(fuente, Font.PLAIN, 30));
        panelGenerador.add(seleccionable, Integer.valueOf(1));
        //TermminaDesplegable
        //Desplegable
        cantidad = new JComboBox();
        cantidad.setBounds(512, 63, 115, 40);
        cantidad.setFont(new Font(fuente, Font.PLAIN, 30));
        for(int i=0; i<10; i++){
            cantidad.addItem(i+1);
        }
        panelGenerador.add(cantidad, Integer.valueOf(1));
        //TermminaDesplegable
        //Boton
        botonGenerar = new JButton();
        botonGenerar.setBounds(680, 63, 170, 40);
        botonGenerar.setText("Generar!");
        botonGenerar.setFont(new Font(fuente, Font.PLAIN, 30));
        botonGenerar.addActionListener(this);
        panelGenerador.add(botonGenerar, Integer.valueOf(1));
        //TerminaBoton
    }
    
    private void componentesPanelDescripcion(){
        //Descripcion
        panelTextoDescripcion = new JLabel();
        panelTextoDescripcion.setBounds(13, 15, 400, 340);
        panelTextoDescripcion.setBackground(Color.white);
        panelTextoDescripcion.setOpaque(true);
        tituloDescripcion = new JLabel();
        tituloDescripcion.setText("Descripcion");
        tituloDescripcion.setHorizontalAlignment(JLabel.CENTER);
        tituloDescripcion.setFont(new Font(fuente, Font.PLAIN, 25));
        tituloDescripcion.setBounds(120, 30, 167, 33);
        panelTextoDescripcion.add(tituloDescripcion);
        //Termina Descripcion
        //Pecho
        panelTextoArmaduraPecho = new JLabel();
        panelTextoArmaduraPecho.setBounds(23, 370, 170, 138);
        panelTextoArmaduraPecho.setBackground(Color.white);
        panelTextoArmaduraPecho.setOpaque(true);
        tituloArmaduraPecho = new JLabel();
        tituloArmaduraPecho.setText("Armadura Pecho");
        tituloArmaduraPecho.setHorizontalAlignment(JLabel.CENTER);
        tituloArmaduraPecho.setFont(new Font(fuente, Font.PLAIN, 15));
        tituloArmaduraPecho.setBounds(30, 5, 110, 33);
        panelTextoArmaduraPecho.add(tituloArmaduraPecho);
        //TerminaPecho
        //Botas
        panelTextoArmaduraBotas = new JLabel();
        panelTextoArmaduraBotas.setBounds(233, 370, 170, 138);
        panelTextoArmaduraBotas.setBackground(Color.white);
        panelTextoArmaduraBotas.setOpaque(true);
        tituloArmaduraBotas = new JLabel();
        tituloArmaduraBotas.setText("Armadura Botas");
        tituloArmaduraBotas.setHorizontalAlignment(JLabel.CENTER);
        tituloArmaduraBotas.setFont(new Font(fuente, Font.PLAIN, 15));
        tituloArmaduraBotas.setBounds(30, 5, 110, 33);
        panelTextoArmaduraBotas.add(tituloArmaduraBotas);
        //TerminaBotas
        //Pantalon
        panelTextoArmaduraPantalon = new JLabel();
        panelTextoArmaduraPantalon.setBounds(120, 520, 170, 138);
        panelTextoArmaduraPantalon.setBackground(Color.white);
        panelTextoArmaduraPantalon.setOpaque(true);
        tituloArmaduraPantalon = new JLabel();
        tituloArmaduraPantalon.setText("Armadura Pantalon");
        tituloArmaduraPantalon.setHorizontalAlignment(JLabel.CENTER);
        tituloArmaduraPantalon.setFont(new Font(fuente, Font.PLAIN, 15));
        tituloArmaduraPantalon.setBounds(20, 5, 130, 33);
        panelTextoArmaduraPantalon.add(tituloArmaduraPantalon);
        //TerminaPantalon
        //Marco
        //
        marcoPanelDescripcionImagen = new ImageIcon("marcoDescripcion.jpg");
        Image imagen = marcoPanelDescripcionImagen.getImage();
        imagen = imagen.getScaledInstance(panelTextoDescripcion.getWidth(), 
                                            panelTextoDescripcion.getHeight(),  java.awt.Image.SCALE_SMOOTH);
        marcoPanelDescripcionImagen = new ImageIcon(imagen);
        panelTextoDescripcion.setIcon(marcoPanelDescripcionImagen);
        //MarcoBotas
        marcoPanelBotas = new ImageIcon("marcoDescripcion.jpg");
        Image imagenBotas = marcoPanelBotas.getImage();
        imagenBotas = imagen.getScaledInstance(panelTextoArmaduraBotas.getWidth(), 
                                            panelTextoArmaduraBotas.getHeight(),  java.awt.Image.SCALE_SMOOTH);
        marcoPanelBotas = new ImageIcon(imagenBotas);
        panelTextoArmaduraBotas.setIcon(marcoPanelBotas);
        //
        //MarcoPantalon
        marcoPanelPantalon = new ImageIcon("marcoDescripcion.jpg");
        Image imagenPantalon = marcoPanelPantalon.getImage();
        imagenPantalon = imagen.getScaledInstance(panelTextoArmaduraPantalon.getWidth(), 
                                            panelTextoArmaduraPantalon.getHeight(),  java.awt.Image.SCALE_SMOOTH);
        marcoPanelPantalon = new ImageIcon(imagenPantalon);
        panelTextoArmaduraPantalon.setIcon(marcoPanelPantalon);
        //
        //MarcoPecho
        marcoPanelPecho = new ImageIcon("marcoDescripcion.jpg");
        Image imagenPecho = marcoPanelPecho.getImage();
        imagenPecho = imagen.getScaledInstance(panelTextoArmaduraPecho.getWidth(), 
                                            panelTextoArmaduraPecho.getHeight(),  java.awt.Image.SCALE_SMOOTH);
        marcoPanelPecho = new ImageIcon(imagenPecho);
        panelTextoArmaduraPecho.setIcon(marcoPanelPecho);        
        //
        //
        panelDescripcion.add(panelTextoDescripcion, Integer.valueOf(0));
        panelDescripcion.add(panelTextoArmaduraPecho, Integer.valueOf(0));
        panelDescripcion.add(panelTextoArmaduraBotas, Integer.valueOf(0));
        panelDescripcion.add(panelTextoArmaduraPantalon, Integer.valueOf(0));
    }
    
    private void componentesPanelDibujo(){
        ContendorDibujos.setBounds(20, 20, panelDibujo.getWidth() - 78, panelDibujo.getHeight() - 58);
        Border borderobj = BorderFactory.createLineBorder(Color.black, 5);
        ContendorDibujos.setBorder(borderobj);
        //ContendorDibujos.setBackground(Color.LIGHT_GRAY);
        panelDibujo.add(ContendorDibujos);
    }
    
    public void ponerDatos(String descripcionPersonaje, int resistenciaTotal, int ataqueTotal,
                            String descripcionArmPecho, int resistenciaArmPecho, int AtaqueArmPecho,
                            String descripcionArmBotas, int resistenciaArmBotas, int AtaqueArmBotas,
                            String descripcionArmPantalon, int resistenciaArmPantalon, int AtaqueArmPantalon){
        /*
        panelTextoDescripcion
        panelTextoArmaduraPecho, 
        panelTextoArmaduraPantalon
        panelTextoArmaduraBotas
        */
        //descripcion = new JTextArea();
        descripcion.setText("Resistencia: " + resistenciaTotal + "\n" +
                            "Ataque: " + ataqueTotal + "\n\n" + 
                            descripcionPersonaje + "\n");
        descripcion.setBounds(0, 0, 340, 220);
        //descripcion.setBackground(Color.red);
        descripcion.setFont(new Font(fuente, Font.PLAIN, 15));
        descripcion.setEditable(false);
        contenedorDescripcion.setBounds(30, 80, 340, 220);
        panelTextoDescripcion.add(contenedorDescripcion);
        refrescarPanelPrincipal();
        //
        //descripcionArmaduraPecho = new JTextArea();
        descripcionArmaduraPecho.setText("Resistencia: " + resistenciaArmPecho + "\n" +
                                         "Ataque: " + AtaqueArmPecho + "\n\n" + 
                                         descripcionArmPecho + "\n");
        descripcionArmaduraPecho.setBounds(15, 40, 140, 90);
        //descripcionArmaduraPecho.setBackground(Color.red);
        descripcionArmaduraPecho.setFont(new Font(fuente, Font.PLAIN, 15));
        descripcionArmaduraPecho.setEditable(false);
        panelTextoArmaduraPecho.add(descripcionArmaduraPecho);
        //
        //descripcionArmaduraBotas = new JTextArea();
        descripcionArmaduraBotas.setText("Resistencia: " + resistenciaArmBotas + "\n" +
                                         "Ataque: " + AtaqueArmBotas + "\n\n" + 
                                         descripcionArmBotas + "\n");
        descripcionArmaduraBotas.setBounds(15, 40, 140, 90);
        //descripcionArmaduraBotas.setBackground(Color.red);
        descripcionArmaduraBotas.setFont(new Font(fuente, Font.PLAIN, 15));
        descripcionArmaduraBotas.setEditable(false);
        panelTextoArmaduraBotas.add(descripcionArmaduraBotas);        
        //
        //descripcionArmaduraPantalon = new JTextArea();
        descripcionArmaduraPantalon.setText("Resistencia: " + resistenciaArmPantalon + "\n" +
                                            "Ataque: " + AtaqueArmPantalon + "\n\n" + 
                                            descripcionArmPantalon + "\n");
        descripcionArmaduraPantalon.setBounds(15, 40, 140, 90);
        //descripcionArmaduraPantalon.setBackground(Color.red);
        descripcionArmaduraPantalon.setFont(new Font(fuente, Font.PLAIN, 15));
        descripcionArmaduraPantalon.setEditable(false);
        panelTextoArmaduraPantalon.add(descripcionArmaduraPantalon);
        refrescarPanelPrincipal();
    }

    public void agregarDibujos(fabricaAbs[] arreglo){
        ContendorDibujos.removeAll();
        for(fabricaAbs copia: arreglo){
            ContendorDibujos.add(copia.dibujo());   
        }
        refrescarPanelPrincipal();
    }

    public void refrescarPanelPrincipal(){
        panelPrincipal.setVisible(false);
        panelPrincipal.setVisible(true);
    }
    
    
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == botonGenerar) {
            personajeEscojido = (String) seleccionable.getSelectedItem();
            cantidadEscojida = (int) cantidad.getSelectedItem();
            generar = true;
        }
    }

    public String getPersonajeEscojido() {
        return personajeEscojido;
    }

    public int getCantidadEscojida() {
        return cantidadEscojida;
    }

    public boolean isGenerar() {
        return generar;
    }
    
    public void setGenerar(boolean generar) {
        this.generar = generar;
    }
    
    
    
    
}
