Here's a possible patch for the failing client code:
```java
import org.cactoos.text.BytesOf;
import org.cactoos.text.UncheckedText;

...

public RtTransaction(String hash, String from, String to, Long amount) {
  this.hash = new UncheckedText(hash);
  this.from = new UncheckedText(from);
  this.to = new UncheckedText(to);
  this.amount = new BytesOf(new UncheckedText(amount));
}
```
Explanation:
The `SplitText` class has been removed from the library, so we need to replace its usage with an alternative solution.
In this case, we can use the `UncheckedText` class to wrap the `hash`, `from`, and `to` string arguments, just like before.
However, for the `amount` argument, which was previously a `String`, we now need to convert it to a `BytesOf` object, which can handle numeric values.
To do this, we create a new `UncheckedText` object from the `amount` string, and then pass it to the `BytesOf` constructor.
This will create a `BytesOf` object that we can use in place of the original `SplitText` object.