Here's a possible patch to fix the error:

```java
import org.cactoos.scalar.StickyScalar;

// ...

@Override
public Scalar<List<Wallet>> apply(String... args) throws IOException {
  String url = String.format("http://localhost:%s/wallets", args[0]);
  HttpResponse response = new HttpClient(url).get();
  if (response.status() != HttpStatus.OK) {
    throw new IOException(String.format("Can't get wallets list: %s", response.body()));
  }
  return new StickyScalar<>(() -> {
    try {
      return objectMapper.readValue(response.body(), new TypeReference<List<Wallet>>() {});
    } catch (JsonProcessingException e) {
      throw new IOException(e);
    }
  });
}
```

This patch replaces the `SolidScalar` class with `StickyScalar`, which is a new class added in the external dependency. The `StickyScalar` class provides similar functionality to `SolidScalar`, but it allows for a supplier function to be passed in, which can provide a new value if the current value is stale. This can be useful in cases where the value may change over time, such as in this case where the value is being fetched from a remote API.