```java
  import org.cactoos.scalar.ItemAt;
  import java.util.List;

  public class RtTransaction {

    public List<String> getOutputs(String txId) {
      return new ItemAt<>(0, RtApi.INSTANCE.getOutputs(txId));
    }
  }
```