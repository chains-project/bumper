```java
import static develop.p2p.lib.LearnMath.sigmoid;

public class Neuron {

    private double[] weights;
    private double bias;

    public Neuron(int numInputs) {
        weights = new double[numInputs];
        bias = 0;
    }

    public double output(double[] inputs) {
        double sum = 0;
        for (int i = 0; i < inputs.length; i++) {
            sum += weights[i] * inputs[i];
        }
        sum += bias;
        return sigmoid(sum);
    }
}
```