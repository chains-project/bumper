```java
import static com.google.common.math.DoubleMath.exp;

public class Neuron {

    public double sigmoid(double value) {
        return 1.0 / (1.0 + exp(-value));
    }
}
```