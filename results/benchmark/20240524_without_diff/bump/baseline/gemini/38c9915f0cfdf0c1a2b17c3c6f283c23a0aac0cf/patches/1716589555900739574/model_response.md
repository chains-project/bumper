```java
import org.cactoos.text.UncheckedText;
import com.google.common.collect.ImmutableList;

public interface RtTransaction {
    // ...
    
    default UncheckedText getTransactionId() {
        return new UncheckedText(ImmutableList.copyOf(getTransactions()).get(0).getTransactionId());
    }

    // ...
}
```