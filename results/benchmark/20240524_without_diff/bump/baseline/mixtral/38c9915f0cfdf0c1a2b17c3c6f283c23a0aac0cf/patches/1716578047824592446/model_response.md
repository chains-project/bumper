Here's a patch that you can apply to fix the error:

```java
import org.cactoos.iterable.Joined;

// ...

@Override
public List<WalletDto> getAll() throws IOException {
  List<WalletDto> result = new ArrayList<>();
  try (
    InputStream input = connection().getResourceAsStream("/wallets.json");
    Reader reader = new InputStreamReader(input);
    JsonReader json = Json.createReader(reader)
  ) {
    JsonArray jsonArray = json.readArray();
    for (JsonValue value : new Joined<>(jsonArray)) {
      result.add(new WalletDto(value.asObject()));
    }
  }
  return result;
}
```

In this patch, we replaced the usage of `JoinedText` with a new class called `Joined` from the same library. This allows us to iterate over the elements of a JSON array and create a list of `WalletDto` objects.