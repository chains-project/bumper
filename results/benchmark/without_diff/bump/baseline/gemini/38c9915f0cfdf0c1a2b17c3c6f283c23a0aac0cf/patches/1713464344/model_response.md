```java
  import org.cactoos.text.JoinedText;
  import org.cactoos.text.TextOf;

  import java.util.List;
  import java.util.stream.Collectors;

  public class WalletsIn {
    public String walletsIn(List<String> wallets) {
      return new JoinedText(
          ",",
          wallets.stream()
              .map(new TextOf()::new)
              .collect(Collectors.toList())
      ).asString();
    }
  }
```