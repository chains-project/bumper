Here's a possible patch for the failing client code:

```java
import org.cactoos.text.TextCollector;

// ...

@Override
public List<String> ids() throws IOException {
  try (InputStream in = new URL(url(), "wallets").openStream()) {
    return new TextCollector(new InputStreamReader(in)).asList();
  }
}
```

In this patch, we replace the usage of `JoinedText` with `TextCollector` which is a new class added in the updated library version. The `TextCollector` class is used to collect a sequence of text objects into a single text object. In this case, we use it to collect a sequence of strings returned by the input stream into a list of strings.