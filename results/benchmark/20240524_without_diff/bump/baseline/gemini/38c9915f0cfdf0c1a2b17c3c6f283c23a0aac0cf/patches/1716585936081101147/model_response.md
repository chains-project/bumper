```java
  import org.cactoos.text.TextOf;
  import org.cactoos.text.JoinedText;

  import java.util.List;

  public class WalletsIn {

    public String request(String url, String apiKey, String filter, String limit, String offset, List<String> wallets) throws Exception {
      String walletsString = new JoinedText(
        ",",
        wallets
      ).asString();

      return new TextOf(
        new Post(
          url,
          new JsonBody(
            new JoinedText(
              ",",
              new JsonBody.Pair("api_key", apiKey),
              new JsonBody.Pair("filter", filter),
              new JsonBody.Pair("limit", limit),
              new JsonBody.Pair("offset", offset),
              new JsonBody.Pair("wallets", walletsString)
            )
          )
        )
      ).asString();
    }
  }
```