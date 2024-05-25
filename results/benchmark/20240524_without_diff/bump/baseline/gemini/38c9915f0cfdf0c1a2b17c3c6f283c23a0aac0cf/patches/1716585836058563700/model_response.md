```java
  import org.cactoos.text.JoinedText;
import org.cactoos.text.UncheckedText;

  public class WalletsIn {

    public String walletsIn(String url, String authorization) {
      String response = new UncheckedText(
          () -> new JoinedText(
              "\n",
              new String[]{
                  "GET /wallets HTTP/1.1",
                  "Host: " + url,
                  "Authorization: Basic " + authorization,
                  "",
                  ""
              }
          ).asString()
      ).asString();
      return response;
    }
  }
```