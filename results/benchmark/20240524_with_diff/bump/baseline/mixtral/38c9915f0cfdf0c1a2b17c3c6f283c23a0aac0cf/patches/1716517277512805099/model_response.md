```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Double> amount = new ScalarEnvelope<>(new SolidScalar<>(100.0));
```