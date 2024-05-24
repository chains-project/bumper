```java
  import org.cactoos.text.JoinedText;
  import org.cactoos.text.TextOf;

  public class WalletsIn {

    public String getWallets(String url, String accessToken) {
      return new JoinedText(
          new TextOf("GET "),
          new TextOf(url),
          new TextOf("/wallets"),
          new TextOf("?access_token="),
          new TextOf(accessToken)
      ).asString();
    }
  }
```