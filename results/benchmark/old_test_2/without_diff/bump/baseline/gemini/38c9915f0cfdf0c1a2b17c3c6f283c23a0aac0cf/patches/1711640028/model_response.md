```java
  import org.cactoos.text.Text;
  import org.cactoos.text.Texts;

  import java.util.List;

  import static java.util.stream.Collectors.joining;

  public final class WalletsIn implements Wallets {
    private final Text path;
    private final List<String> wallets;

    public WalletsIn(final Text path, final List<String> wallets) {
      this.path = path;
      this.wallets = wallets;
    }

    @Override
    public Text path() {
      return path;
    }

    @Override
    public Text wallets() {
      return new JoinedText(
          new Texts(wallets),
          ", "
      );
    }
  }
```