Here's a possible patch for the failing code:

```java
import org.cactoos.text.Joined;

// ...

@Override
public List<WalletDto> all() throws IOException {
  List<WalletDto> result = new ArrayList<>();
  try (
    InputStream in = connection().input();
    Reader reader = new InputStreamReader(in, StandardCharsets.UTF_8);
    JsonReader json = Json.createReader(reader)
  ) {
    JsonArray jsonArray = json.readArray();
    for (JsonValue jsonValue : jsonArray) {
      result.add(new WalletDto(jsonValue.asObject()));
    }
  }
  return result;
}
```

In this patch, I replaced the `JoinedText` class with the `Joined` class from the same library (`org.cactoos.text.Joined`), as the former seems to have been removed. I also changed the way the JSON data is read, using the `Json` class from the `javax.json` package instead of the `JoinedText` class. This should fix the "cannot find symbol" error.

Note that I had to make some assumptions about the rest of the code, as the failing method was not provided in its entirety. In particular, I assumed that the `connection()` method returns an `InputStream` object, and that the `WalletDto` class takes a `JsonObject` object as its constructor argument. If these assumptions are incorrect, the patch may need to be adjusted accordingly.