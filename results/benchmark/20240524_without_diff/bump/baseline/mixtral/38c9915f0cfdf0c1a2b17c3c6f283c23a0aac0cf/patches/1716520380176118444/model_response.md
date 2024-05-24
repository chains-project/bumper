Here's the proposed patch:

```java
import org.cactoos.text.TextOf;

import static java.nio.charset.StandardCharsets.UTF_8;

...

public RtTransaction(TransactionInput input, TransactionOutput output,
    TransactionLog log, TransactionPool pool, TransactionFactory factory)
    throws IOException, NoSuchAlgorithmException {
    super(input, output, log, pool, factory);
    this.amount = new TextOf(input.amount(), UTF_8).asString();
    // the rest of the method remains unchanged
}
```

This patch replaces the usage of `TrimmedText` with `TextOf`, which is a new method added in the updated library version. The `TextOf` method is used to create a `Text` instance from a given `CharSequence`, and it also accepts a `Charset` argument to specify the character encoding. In this case, `UTF_8` is used as the character encoding. The `asString()` method is then called on the `Text` instance to get the string value of the transaction amount.