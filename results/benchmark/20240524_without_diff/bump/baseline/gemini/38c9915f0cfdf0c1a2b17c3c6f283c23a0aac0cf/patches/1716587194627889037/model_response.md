```java
  import org.cactoos.text.TrimmedText;
  
  public class RtTransaction {
  
    public String getTxId(String txId) {
      return new TrimmedText(txId).asString();
    }
  }
```