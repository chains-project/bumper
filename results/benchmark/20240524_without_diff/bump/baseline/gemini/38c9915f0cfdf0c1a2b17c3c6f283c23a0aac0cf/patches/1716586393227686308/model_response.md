```java
  import org.cactoos.scalar.IoCheckedScalar;
  import java.io.IOException;

  public class WalletsIn extends IoCheckedScalar<String> {

    public WalletsIn(String url) {
      super(new IoCheckedScalar<>(() -> {
        try {
          return "WalletsIn";
        } catch (IOException e) {
          throw new RuntimeException(e);
        }
      }));
    }
  }
```