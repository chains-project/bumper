Here is a possible patch for the failing code:
```java
import org.cactoos.text.Joined;

//...

@Override
public List<WalletIn> findAll() throws IOException {
  return new IterableOf<File>(files())
    .stream()
    .map(file -> new WalletIn(file, new Joined(File.pathSeparator, new TextOf(file))))
    .collect(Collectors.toList());
}
```
In this patch, we replaced the usage of `JoinedText` with `Joined`, which is a new class added in the updated version of the library. We also replaced the usage of `TextOf` with `new TextOf(file)` to fix the compilation error.