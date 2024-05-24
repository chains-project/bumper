```java
  import org.cactoos.text.UncheckedText;
  import org.cactoos.iterable.Mapped;
  import org.cactoos.iterable.StickyIterable;

  import java.util.List;
  import java.util.Map;

  import static java.util.stream.Collectors.toList;

  public class WalletsIn {

      public static final String WALLETS_IN = "/v1/wallets/in";

      private final ZoldApi api;

      public WalletsIn(ZoldApi api) {
          this.api = api;
      }

      public List<WalletIn> get(String address, Map<String, String> params) {
          return new StickyIterable<>(
                  new Mapped<>(
                          wallet -> new WalletIn(
                                  wallet.get("address").toString(),
                                  wallet.get("amount").toString(),
                                  wallet.get("blockHeight").toString(),
                                  wallet.get("confirmations").toString(),
                                  wallet.get("currency").toString(),
                                  wallet.get("fee").toString(),
                                  wallet.get("hash").toString(),
                                  wallet.get("id").toString(),
                                  wallet.get("time").toString(),
                                  wallet.get("transactionId").toString(),
                                  wallet.get("type").toString()
                          ),
                          api.get(WALLETS_IN, address, params)
                                  .stream()
                                  .filter(wallet -> !wallet.get("amount").toString().equals("0"))
                                  .collect(toList())
                  )
          ).stream().collect(toList());
      }
  }
```