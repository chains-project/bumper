```java
import static java.lang.Math.exp;
public class Neuron {
    public double sigmoid(double x) {
        return 1 / (1 + exp(-x));
    }
}
```