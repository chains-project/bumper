```java
  import org.cactoos.bytes.BytesOf;
  import org.cactoos.text.Joined;

  import java.nio.charset.StandardCharsets;

  public class WalletsIn {

      public WalletsIn(String url, String apiKey, String walletId) {
          BytesOf body = new BytesOf(new Joined(
                  "{\"walletId\": \"",
                  walletId,
                  "\"}"
          ).asString(), StandardCharsets.UTF_8);

          // ...
      }
  }
```