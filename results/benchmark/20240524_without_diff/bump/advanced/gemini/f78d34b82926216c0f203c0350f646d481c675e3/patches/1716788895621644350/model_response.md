```java
import static develop.p2p.lib.LearnMath.sigmoid;

import java.util.ArrayList;
import java.util.List;

public class Neuron {

    private double output;
    private List<Double> weights = new ArrayList<>();
    private List<Double> inputs = new ArrayList<>();

    public Neuron(int numInputs) {
        for (int i = 0; i < numInputs; i++) {
            weights.add(Math.random());
            inputs.add(0.0);
        }
    }

    public void setInputs(List<Double> inputs) {
        this.inputs = inputs;
    }

    public double getOutput() {
        return output;
    }

    public void calculateOutput() {
        double sum = 0.0;
        for (int i = 0; i < inputs.size(); i++) {
            sum += inputs.get(i) * weights.get(i);
        }
        output = sigmoid(sum);
    }

    public void updateWeights(double learningRate) {
        for (int i = 0; i < weights.size(); i++) {
            double delta = learningRate * (output - inputs.get(i));
            weights.set(i, weights.get(i) + delta);
        }
    }
}
```