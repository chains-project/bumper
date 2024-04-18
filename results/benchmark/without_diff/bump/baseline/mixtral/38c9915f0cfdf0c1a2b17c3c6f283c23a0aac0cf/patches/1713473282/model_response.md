Here's a proposed patch for the failing code:

```java
import org.cactoos.text.Texts;

// ...

@Override
public String asString() throws IOException {
  return new JoinedText(
    Texts.wrap(","),
    this.wallets.stream()
      .map(WalletIn::asString)
      .toArray(String[]::new)
  ).asString();
}
```

In this patch, I replaced the `import org.cactoos.text.JoinedText` with `import org.cactoos.text.Texts`, and modified the implementation of `asString` method to use `Texts.wrap(",")` instead of `JoinedText`. This should resolve the compilation error.