```java
import static java.lang.Math.exp;

public double sigmoid(double x) {
    return 1.0 / (1.0 + exp(-x));
}
```