```java
import static java.lang.Math.exp;
public class Neuron {
    public static double sigmoid(double x) {
        return 1 / (1 + exp(-x));
    }
    // rest of the class
}
```