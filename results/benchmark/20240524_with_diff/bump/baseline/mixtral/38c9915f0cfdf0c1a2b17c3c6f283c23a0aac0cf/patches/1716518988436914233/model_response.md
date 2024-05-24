Here's the proposed patch for the failing client code:

```java
import org.cactoos.collection.Immutable;

// ...

public Collection<File> copies(String hash) {
  Collection<File> result = new CollectionOf<File>(files(hash));
  return new Immutable<>(result);
}
```

The `CollectionOf` class has been removed in the new library version, so we replace it with the new `Immutable` class. We create an intermediate collection `result` to wrap the files, and then wrap it again with an `Immutable` collection to ensure no further modifications can be made.