Here is a fixed version of the `input` method:
```java
import ml.peya.plugins.Learn.Input;
import org.apache.commons.math3.analysis.function.Sigmoid;

public void input(java.util.ArrayList<Input> inputData) {
    Sigmoid sigmoid = new Sigmoid();
    inputData.parallelStream().forEachOrdered((input) -> setValue(sigmoid.value(input.getWeightingValue())));
}
```
I replaced the call to `develop.p2p.lib.LearnMath.sigmoid` with a call to `org.apache.commons.math3.analysis.function.Sigmoid.value`. The `Sigmoid` function is a part of the Apache Commons Math library, which can be added as a dependency to your project.

The `setValue` method is assumed to take a `double` argument.

Note: I had to make an assumption about the type of the `sum` variable used in the original code, as it was not declared in the method. I assumed it is not used and removed it. If this is incorrect, please let me know.