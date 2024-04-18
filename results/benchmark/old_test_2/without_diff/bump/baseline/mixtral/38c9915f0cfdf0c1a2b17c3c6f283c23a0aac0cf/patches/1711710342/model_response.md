Here's a possible patch to fix the error:

```java
import org.cactoos.list.Joined;

// ...

@Override
public InputStream inputOfWallets() throws IOException {
  return new Joined<>(
    inputOfWalletsSupplier()
  ).stream();
}
```

In this patch, we replace the usage of `JoinedText` with `Joined`, which is a part of the same library (`cactoos`) and provides similar functionality. We then use the `stream()` method to convert the `Joined` object to an `InputStream`, which is what the original method was supposed to return. Note that the `JoinedText` class seems to have been removed in a recent version of the library, which is why the original code no longer works.