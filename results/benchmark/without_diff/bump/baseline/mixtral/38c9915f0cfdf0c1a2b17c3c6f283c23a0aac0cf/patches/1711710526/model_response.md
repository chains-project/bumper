Here's a patched version of the failing method that you can use to fix the error:

```java
import org.cactoos.scalar.UncheckedScalar;

@Override
public Currencies currencies() throws IOException {
  return new UncheckedScalar<>(() -> api.currencies());
}
```

This patch replaces the problematic import statement and uses a new class `UncheckedScalar` to handle any exceptions that might be thrown by the `api.currencies()` method. This should fix the "cannot find symbol" error you were seeing.