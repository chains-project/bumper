```java
import static java.lang.Math.exp;
import static java.lang.Math.pow;

public static double sigmoid(double x) {
    return 1 / (1 + exp(-x));
}
```