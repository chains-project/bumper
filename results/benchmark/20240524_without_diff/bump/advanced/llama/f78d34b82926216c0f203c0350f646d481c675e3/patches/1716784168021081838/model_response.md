```java
import static java.lang.Math.exp;
import static java.lang.Math.pow;

public static double sigmoid(double x) {
    return 1.0 / (1.0 + pow(exp(1.0), -x));
}
```