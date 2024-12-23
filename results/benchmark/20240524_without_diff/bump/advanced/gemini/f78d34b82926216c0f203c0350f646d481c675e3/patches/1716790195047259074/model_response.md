```java
import com.google.common.math.IntMath;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import org.apache.commons.math3.util.FastMath;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Neuron {

    private static final Logger LOGGER = LoggerFactory.getLogger(Neuron.class);
    private final List<Double> weights;
    private final double bias;
    private final Activation activation;

    public Neuron(int numInputs, Activation activation) {
        this.weights = new ArrayList<>(numInputs);
        for (int i = 0; i < numInputs; i++) {
            this.weights.add(randomWeight());
        }
        this.bias = randomWeight();
        this.activation = activation;
    }

    public Neuron(List<Double> weights, double bias, Activation activation) {
        this.weights = weights;
        this.bias = bias;
        this.activation = activation;
    }

    public double calculateOutput(List<Double> inputs) {
        if (inputs.size() != this.weights.size()) {
            throw new IllegalArgumentException("Input size does not match the number of weights.");
        }
        double sum = 0.0;
        for (int i = 0; i < inputs.size(); i++) {
            sum += inputs.get(i) * this.weights.get(i);
        }
        sum += this.bias;
        return this.activation.apply(sum);
    }

    public List<Double> getWeights() {
        return Collections.unmodifiableList(this.weights);
    }

    public double getBias() {
        return this.bias;
    }

    public Activation getActivation() {
        return this.activation;
    }

    public void updateWeights(List<Double> inputs, double learningRate, double error) {
        if (inputs.size() != this.weights.size()) {
            throw new IllegalArgumentException("Input size does not match the number of weights.");
        }
        for (int i = 0; i < inputs.size(); i++) {
            double deltaWeight = learningRate * error * inputs.get(i);
            this.weights.set(i, this.weights.get(i) + deltaWeight);
        }
        this.bias += learningRate * error;
    }

    private static double randomWeight() {
        return (Math.random() - 0.5) * 2.0;
    }

    public enum Activation {
        SIGMOID {
            @Override
            public double apply(double x) {
                return 1.0 / (1.0 + Math.exp(-x));
            }

            @Override
            public double derivative(double x) {
                return x * (1.0 - x);
            }
        },
        RELU {
            @Override
            public double apply(double x) {
                return Math.max(0.0, x);
            }

            @Override
            public double derivative(double x) {
                return x > 0.0 ? 1.0 : 0.0;
            }
        },
        TANH {
            @Override
            public double apply(double x) {
                return Math.tanh(x);
            }

            @Override
            public double derivative(double x) {
                return 1.0 - Math.pow(Math.tanh(x), 2.0);
            }
        };

        public abstract double apply(double x);

        public abstract double derivative(double x);
    }
}
```