Here is the proposed patch:
```java
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(TransactionInput input, TransactionOutput output) {
  this.input = new UncheckedText(input::asString);
  this.output = new UncheckedText(output::asString);
  // ...
}
```
Explanation:
The `TrimmedText` class has been removed in the new library version. Instead, we can use the `UncheckedText` class which takes a `CharSequence` as input and can be used in a similar way. We can wrap the `input` and `output` objects with `UncheckedText` to use them in the rest of the class.