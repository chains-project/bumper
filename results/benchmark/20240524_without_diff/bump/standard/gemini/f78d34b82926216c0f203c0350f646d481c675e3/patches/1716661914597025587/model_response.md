```java
import develop.p2p.lib.LearnMath;

public class Neuron {

    private final int nInputs;
    private final double[] weights;
    private final double bias;

    public Neuron(int nInputs, double[] weights, double bias) {
        this.nInputs = nInputs;
        this.weights = weights;
        this.bias = bias;
    }

    public double calculateOutput(double[] inputs) {
        double sum = 0;
        for (int i = 0; i < nInputs; i++) {
            sum += inputs[i] * weights[i];
        }
        sum += bias;
        return LearnMath.sigmoid(sum);
    }
}
```