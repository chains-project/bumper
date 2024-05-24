Here's the fixed version of the code:

```java
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(String id, String hash, long timestamp, User from, User to, Money amount, TextOf<String> input, TextOf<String> output) {
    this.id = new UncheckedText(id);
    this.hash = new UncheckedText(hash);
    this.timestamp = timestamp;
    this.from = from;
    this.to = to;
    this.amount = amount;
    this.input = input;
    this.output = output;
}
```

In this fixed version, I replaced the usage of `TrimmedText` with `UncheckedText` and `TextOf`. This is possible because `TrimmedText` is a subclass of `UncheckedText`, and `TextOf` can be used to create a text from a string.