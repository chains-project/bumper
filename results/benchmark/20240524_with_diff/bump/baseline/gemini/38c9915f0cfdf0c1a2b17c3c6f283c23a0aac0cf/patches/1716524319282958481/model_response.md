```java
  import org.cactoos.text.JoinedText;

  import java.util.Arrays;
  import java.util.List;
  import java.util.stream.Collectors;

  public class WalletsIn {

    public String[] wallets(String... wallets) {
      if (wallets.length == 0) {
        return new String[0];
      }
      List<String> walletsList = Arrays.asList(wallets);
      String joinedWallets = walletsList.stream().collect(Collectors.joining(","));
      return new JoinedText(joinedWallets, ",").asString().split(",");
    }
  }
```