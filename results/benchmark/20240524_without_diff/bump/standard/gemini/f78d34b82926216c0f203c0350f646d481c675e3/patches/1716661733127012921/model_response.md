```java
import static com.google.common.math.IntMath.pow;

public class Neuron {

    private final double[] weights;
    private final double bias;

    public Neuron(double[] weights, double bias) {
        this.weights = weights;
        this.bias = bias;
    }

    public double output(double[] input) {
        double sum = 0;
        for (int i = 0; i < input.length; i++) {
            sum += input[i] * weights[i];
        }
        sum += bias;
        return sigmoid(sum);
    }

    private static double sigmoid(double x) {
        return 1 / (1 + Math.exp(-x));
    }
}
```