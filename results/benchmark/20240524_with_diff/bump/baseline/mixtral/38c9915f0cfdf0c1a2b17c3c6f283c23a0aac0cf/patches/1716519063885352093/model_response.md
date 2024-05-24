Here's the fixed version of the failing method in `Copies.java`:

```java
import org.cactoos.collection.Immutable;
import org.cactoos.collection.NoNulls;

public CollectionOf<Bytes> copies(Collection<String> ids) {
    return new NoNulls<>(
        new Immutable<>(
            ids.stream().map(id -> new BytesOf(zdb().load(id))).collect(Collectors.toList())
        )
    );
}
```

This version replaces the use of the removed `CollectionOf` constructor with the `NoNulls` and `Immutable` classes, which were added in the new library version. It also uses the `BytesOf` constructor that was added in the new version.