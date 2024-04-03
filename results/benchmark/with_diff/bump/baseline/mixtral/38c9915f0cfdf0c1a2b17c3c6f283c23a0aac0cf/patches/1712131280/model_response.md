Here's a proposed patch to fix the error:

```java
import org.cactoos.text.TextCollector;

// ...

@Override
public String allBalances() throws IOException {
  return new TextCollector(
    new Iterable<Text>() {
      @Override
      public Iterator<Text> iterator() {
        return new Iterator<Text>() {
          private final Iterator<Wallet> wallets = new WalletsOf(api).iterator();
          private Text current = EmptyText.INSTANCE;

          @Override
          public boolean hasNext() {
            return wallets.hasNext();
          }

          @Override
          public Text next() {
            current = wallets.next().balance();
            return current;
          }
        };
      }
    }
  ).get();
}
```

This patch replaces the usage of `JoinedText` with a combination of `TextCollector` and an anonymous `Iterable` implementation. It iterates over the wallets and collects their balances into a single text.