Here's the proposed patch for the failing client code:

```java
import org.cactoos.text.Texts;

// ...

@Override
public List<WalletDto> apply(List<String> ids) throws IOException {
  List<WalletDto> dtos = new ArrayList<>();
  for (String id : ids) {
    WalletDto dto = new WalletDto();
    dto.setId(id);
    dto.setAddress(String.join("", Texts.of(WALLET_ADDRESS_PREFIX, id)));
    dtos.add(dto);
  }
  return dtos;
}
```

In this patch, I replaced the `JoinedText` class with the `String.join` method and the `Texts.of` method from the `org.cactoos.text` package. This should resolve the "cannot find symbol" error caused by the missing `JoinedText` class.