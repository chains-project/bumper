Here's a potential patch for the failing client code:

```java
import org.cactoos.text.Joined;

// ...

@Override
public InputStream walletsIn(String id) throws IOException {
  List<String> urls = new ArrayList<>();
  // ... populate urls with appropriate values ...
  return new URLsInputStream(new Joined(urls));
}
```

In this patch, we replace the `JoinedText` class with the `Joined` class, which provides similar functionality. We also replace `URLsInputStream` with its equivalent constructor that takes a `Joined` object. This should resolve the "cannot find symbol" error.