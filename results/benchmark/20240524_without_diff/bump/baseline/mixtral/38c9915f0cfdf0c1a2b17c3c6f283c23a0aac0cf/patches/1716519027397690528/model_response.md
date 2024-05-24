Here's the patched version of the failing client code:

```java
import org.cactoos.collection.Immutable;
import java.util.Collections;

// ...

public class Copies {
    // ...

    private static Immutable<Path> paths(final Iterable<Path> paths) {
        return new Immutable<>(Collections.unmodifiableCollection(paths));
    }

    // ...
}
```

I changed the `CollectionOf` import to `Immutable` and used `Collections.unmodifiableCollection` to make the collection immutable as the `CollectionOf` class is removed.