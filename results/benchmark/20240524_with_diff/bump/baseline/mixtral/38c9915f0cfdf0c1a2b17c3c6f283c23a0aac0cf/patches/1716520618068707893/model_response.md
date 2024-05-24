Here's a possible patch for the client code:
```java
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(String id, TransactionType type, Amount amount, String... tags) {
  super(
    id,
    type,
    amount,
    new UncheckedText(tags)
  );
}
```
Explanation:
- The `SplitText` class has been removed in the new version of the library.
- Instead, we can use the `UncheckedText` class, which is a simple wrapper around a `CharSequence`.
- We can use it to convert the `tags` array to a `Text` object, which is expected by the superclass constructor.
- Note that this solution assumes that the `tags` array will never be `null`. If it can be `null`, you should add a null check before creating the `UncheckedText` object.