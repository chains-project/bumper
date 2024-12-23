```java
  import org.cactoos.text.FormattedText;
  import org.cactoos.text.TextOf;
  import org.slf4j.Logger;
  import org.slf4j.LoggerFactory;

  import java.util.List;
  import java.util.stream.Collectors;

  public class WalletsIn {

    private static final Logger LOG = LoggerFactory.getLogger(WalletsIn.class);

    private final String address;
    private final String password;

    public WalletsIn(String address, String password) {
      this.address = address;
      this.password = password;
    }

    public List<Wallet> getWallets() {
      LOG.info("Getting wallets for address: {}", address);
      try {
        return new TextOf(new FormattedText(
          "curl -s -X POST -H 'Content-Type: application/json' -d '{\"address\":\"%s\",\"password\":\"%s\"}' %s/wallets",
          address,
          password,
          address
        )).asString().stream()
          .map(Wallet::new)
          .collect(Collectors.toList());
      } catch (Exception e) {
        LOG.error("Error getting wallets for address: {}", address, e);
        throw new RuntimeException(e);
      }
    }
  }
```