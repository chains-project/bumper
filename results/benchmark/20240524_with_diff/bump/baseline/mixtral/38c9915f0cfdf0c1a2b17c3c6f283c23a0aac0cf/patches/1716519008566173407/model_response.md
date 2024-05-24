Here's a possible patch for the failing code:
```java
import org.cactoos.collection.Immutable;

// ...

public class Copies {
    // ...

    private Immutable<File> files(String path) {
        return new Immutable<>(filesByPath(path));
    }

    // ...
}
```
The change here is to replace the use of `CollectionOf` with `Immutable`. This is possible because the new version of the library includes an `Immutable` class that can take a `Collection` in its constructor.

Note that I made the assumption that `filesByPath` returns a `Collection` of `File` objects. If that's not the case, you may need to adjust the type parameter of `Immutable` accordingly.

Also note that I removed the `@Override` annotation from the `files` method because it's not overriding any method in the new version of the library.

Finally, note that this patch assumes that the rest of the code in the `Copies` class does not depend on any of the removed methods in the library. If it does, you may need to make additional changes to the code.