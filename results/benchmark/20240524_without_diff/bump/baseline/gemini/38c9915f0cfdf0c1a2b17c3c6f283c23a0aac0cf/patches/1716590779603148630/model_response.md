```java
  import org.cactoos.scalar.IoCheckedScalar;

  import java.io.IOException;
  import java.io.InputStream;

  public class RtTransaction {

    public static IoCheckedScalar<InputStream> read(String path) throws IOException {
      return new IoCheckedScalar<>(() -> RtTransaction.class.getResourceAsStream(path));
    }

  }
```