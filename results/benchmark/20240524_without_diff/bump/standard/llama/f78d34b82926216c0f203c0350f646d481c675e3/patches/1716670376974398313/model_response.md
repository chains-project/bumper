```java
import static java.lang.Math.exp;
public float sigmoid(float x) {
    return (float) (1 / (1 + exp(-x)));
}
```