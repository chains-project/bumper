```java
  import org.cactoos.scalar.IoCheckedScalar;

  import java.io.IOException;
  import java.io.InputStream;

  public class WalletsIn {

    public WalletsIn(InputStream in) throws IOException {
      new IoCheckedScalar<>(in::close).value();
    }
  }
```