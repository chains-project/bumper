```java
import org.cactoos.text.JoinedText;
// import org.cactoos.text.TextOf;

public class WalletsIn {

//  @Override
  public String walletsIn(String account) {
    // return new TextOf(account).asString();
    return new JoinedText(
            "{\"jsonrpc\":\"2.0\",\"method\":\"wallets_in\",\"params\":[",
            account,
            "]}",
            "\n"
    ).asString();
  }
}
```