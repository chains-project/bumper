```java
  import org.cactoos.scalar.IoCheckedScalar;
  import org.cactoos.text.TextOf;

  import java.io.IOException;

  import static org.cactoos.text.TextOf.textOf;

  public class WalletsIn {

    private final IoCheckedScalar<String> getWallets;

    public WalletsIn(final String url) {
      this.getWallets = new IoCheckedScalar<>(() -> new TextOf(url).asString());
    }

    public String getWallets() throws IOException {
      return this.getWallets.value();
    }

  }
```