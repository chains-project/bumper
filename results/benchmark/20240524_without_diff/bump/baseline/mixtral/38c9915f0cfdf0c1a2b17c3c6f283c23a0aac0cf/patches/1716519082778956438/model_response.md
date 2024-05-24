Here's a patch that should fix the error:

```java
import org.cactoos.collection.Immutable;
```

The `CollectionOf` class has been removed in the new library version, but the `Immutable` class provides similar functionality. You can use `Immutable` to create an immutable collection from an iterable or a collection. Here's an example:

```java
Iterable<String> iterable = Arrays.asList("foo", "bar", "baz");
Immutable<String> immutable = new Immutable<>(iterable);
```

In this example, `immutable` is an immutable collection that contains the strings "foo", "bar", and "baz". You can use `Immutable` in the same way that you used `CollectionOf`.