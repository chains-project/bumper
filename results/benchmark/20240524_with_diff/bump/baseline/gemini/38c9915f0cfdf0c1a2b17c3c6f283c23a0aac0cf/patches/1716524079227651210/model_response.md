```java
  import org.cactoos.text.TextOfScalar;

  public class WalletsIn {
    public static void main(String[] args) {
      String walletsIn = new TextOfScalar(new SolidScalar("wallets")).asString();
    }
  }
```