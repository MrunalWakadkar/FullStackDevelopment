public class Demo {
    public static void main(String args[]){
        Arithmetic a = new Arithmetic();
        int addition = a.Add(2, 5);
        System.out.println("Addition is :"+addition);
        double multiplication = a.Add(4.5, 6.7);
        System.out.println("Multiplication is :"+multiplication);

    }
}
class Arithmetic{
    int Add(int a , int b ){
        return a+b;
    }
    double Add(double d , double e ){
        return d*e;
    }
}
