```java
  import org.cactoos.scalar.SolidScalar;
  import org.cactoos.scalar.Unchecked;

  public class WalletsIn {

    public SolidScalar<String> wallets() {
      return new Unchecked<>(() -> {
        throw new RuntimeException("Not implemented");
      });
    }
  }
```