```java
  import org.cactoos.text.TextOf;

  import java.util.List;

  public class WalletsIn {

      public String apply(List<String> walletAddresses) {
          StringBuilder sb = new StringBuilder();
          for (String walletAddress : walletAddresses) {
              sb.append(new TextOf(walletAddress).asString()).append("\n");
          }
          return sb.toString();
      }
  }
```