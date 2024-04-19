```java
import org.cactoos.scalar.Scalar;

  public Scalar<String> getWallets(String seed) {
    return new SolidScalar<>(seed);
  }
```