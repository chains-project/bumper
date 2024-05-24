Here's the patched version of the client code that should work with the new library version:

```java
import org.cactoos.text.UncheckedText;

// ...

@Override
public Text of(String text) {
    return new UncheckedText(text);
}
```

This patch replaces the usage of `RandomText` with `UncheckedText`, which is a new class in the updated library version. The `UncheckedText` class can be used similarly to the removed `RandomText` class, as it also takes a `CharSequence` as a constructor argument.