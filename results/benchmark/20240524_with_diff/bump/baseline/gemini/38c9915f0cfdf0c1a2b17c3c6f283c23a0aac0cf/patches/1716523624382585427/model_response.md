```java
  import org.cactoos.bytes.IoCheckedBytes;
  import org.cactoos.text.IoCheckedText;

  import java.io.IOException;

  public class WalletsIn {

      public WalletsIn(final IoCheckedText wallets) {
          new IoCheckedBytes(wallets).asBytes();
      }
  }
```