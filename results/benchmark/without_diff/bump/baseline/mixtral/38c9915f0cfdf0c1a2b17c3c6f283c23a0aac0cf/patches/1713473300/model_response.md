Here's a possible patch for the failing code:

```java
import org.cactoos.text.Joined;

// ...

@Override
public List<WalletDto> getAll() throws IOException {
  List<WalletDto> result = new ArrayList<>();
  try (InputStream is = url.openStream()) {
    List<String> strings = new JsonInput(is).jsonArray();
    for (String string : strings) {
      result.add(new WalletDto(new JsonMap(new JsonInput(new StringReader(string)))));
    }
  }
  return result;
}
```

In this patch, I replaced the usage of `JoinedText` with `Joined` from the same library, as the former was removed in a later version. Additionally, I updated the imports accordingly.