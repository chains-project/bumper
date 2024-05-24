```java
  import org.cactoos.text.FormattedText;

  import static org.cactoos.text.TextOf.textOf;

  public class WalletsIn {

    public String getWalletsIn(String walletsIn) {
      return new FormattedText(
          "Wallets: %s",
          textOf(walletsIn)
      ).asString();
    }
  }
```