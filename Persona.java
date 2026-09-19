public class Persona {
    private int edad;
    private String nombre;
    private String dni;
    
    public Persona(String nombre, int edad, String dni) {
        edad = this.setedad;
        nombre = this.setnombre;
        dni = this.setdni;
    }

    public void hablar(){
        System.out.println("Hablando...");
    }

    public void gustar(String nombre){
        System.out.println("Me gusta " + nombre);
    }

    public void setedad(int edad) {
        this.setedad = edad;
    }

    public void getedad() {
        return edad;
    }

    public void setnombre(String nombre) {
        this.setnombre = nombre;
    }

    public void getnombre() {
        return nombre;
    }

    public void setdni(String dni) {
        this.setdni = dni;
    }

    public void getdni() {
        return dni;
    }
}