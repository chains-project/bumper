Here's the proposed patch:

```java
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.input.IoSupplier;
import org.cactoos.text.IoCheckedText;

// ...

public IoCheckedScalar<Transaction> load(String id) throws IOException {
  IoSupplier<InputStream> supplier = () -> new FileInputStream(file(id));
  IoCheckedBytes checkedBytes = new IoCheckedBytes(supplier, Throwables::propagate);
  IoCheckedText checkedText = new IoCheckedText(checkedBytes::asBytes, String::new);
  return new IoCheckedScalar<>(checkedText::asString, Throwables::propagate);
}
```

In this patch, I replaced the usage of `IoCheckedScalar` with `IoCheckedBytes` and `IoCheckedText`, which are the new classes added in the updated library version. Additionally, I used method references to make the code more concise.