```java
  import org.cactoos.scalar.StickyScalar;
import com.google.common.base.Strings;

  public class RtTransaction {

    ...

    public RtTransaction(String txHash) {
      this.txHash = Strings.isNullOrEmpty(txHash) ? null : txHash;
    }

    ...
  }
```