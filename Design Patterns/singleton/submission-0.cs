public class Singleton {

    private static Singleton singletonInstance = null;
    private string value = null;

    private Singleton() {
      
    }

    public static Singleton getInstance() {
        if (singletonInstance == null) {
            singletonInstance = new Singleton();
        }

        return singletonInstance;
    }

    public string getValue() {
        return value;
    }

    public void setValue(string value){
        this.value = value;
    }
}
