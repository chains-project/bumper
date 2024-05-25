```java
  import org.cactoos.text.Text;
  import org.cactoos.text.UncheckedText;

  public class RtTransaction {

    // ...

    private Text transactionId;

    // ...

    public RtTransaction(String transactionId) {
      this.transactionId = new UncheckedText(transactionId);
    }

    // ...

  }
```