Here's a possible patch for the failing code:

```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.TextJoiner;

@Override
protected TextEnvelope<String> walletsJoined(List<Wallet> wallets) throws IOException {
  return new TextJoiner(" ", wallets.stream()
    .map(Wallet::id)
    .collect(Collectors.toList())
  ).join(TextEnvelope.empty());
}
```

In this patch, we replaced the usage of `JoinedText` with `TextJoiner`. The `TextJoiner` class is a new addition to the `cactoos-text` library and provides similar functionality to `JoinedText`. We also changed the import statement to reflect the new class.

Note that if there are any other usages of `JoinedText` in the codebase, they will need to be updated as well.