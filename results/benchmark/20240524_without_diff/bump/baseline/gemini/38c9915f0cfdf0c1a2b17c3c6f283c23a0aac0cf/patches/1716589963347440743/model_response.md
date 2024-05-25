```java
  import org.cactoos.text.SplitText;
  import java.util.List;

  public class RtTransaction {

    public List<String> getTransactionList(String transaction) {
      return new SplitText(transaction, "\n").asList();
    }
  }
```