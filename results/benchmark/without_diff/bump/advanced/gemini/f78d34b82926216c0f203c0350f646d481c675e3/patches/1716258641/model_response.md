```java
import org.apache.commons.math3.analysis.function.Sigmoid;

public class Neuron {

    private final Sigmoid sigmoidFunction = new Sigmoid();

    public double output(double input) {
        return sigmoidFunction.value(input);
    }
}
```