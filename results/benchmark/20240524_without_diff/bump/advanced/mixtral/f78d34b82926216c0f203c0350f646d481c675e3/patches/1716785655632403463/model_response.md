Here's the patched version of the `input` method:
```java
import org.apache.commons.math3.ml.distance.EuclideanDistance;

public void input(java.util.ArrayList<ml.peya.plugins.Learn.Input> inputData) {
    inputData.parallelStream().forEachOrdered(( input) -> input(input.getWeightingValue()));
    setValue(develop.p2p.lib.LearnMath.sigmoid(sum));
}

private double sigmoid(double value) {
    EuclideanDistance distance = new EuclideanDistance();
    return 1 / (1 + Math.exp(-value));
}
```
I added a new `sigmoid` method to calculate the sigmoid function. This should fix the "cannot find symbol" error.

Please note that I had to make an assumption about the `sum` variable used in the original code. I assumed it is a `double` variable. If it's not the case, please adjust the `sigmoid` method accordingly.