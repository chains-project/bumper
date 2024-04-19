```java
import org.cactoos.text.TextOf;

  public String walletsIn(String walletId) {
    return new TextOf("{\"walletId\":\"" + walletId + "\"}").asString();
  }
```