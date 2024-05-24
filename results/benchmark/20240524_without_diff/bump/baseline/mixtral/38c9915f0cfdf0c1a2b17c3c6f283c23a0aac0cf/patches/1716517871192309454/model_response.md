Here's the fixed version of the code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Unchecked;

// ...

Scalar<Bytes> bytes = new Unchecked<>(() -> ...);
```

The `UncheckedScalar` class has been removed in the new library version, so you should replace its usage with the `Unchecked` class instead. The `Unchecked` class takes a `Callable` as its constructor argument, which can be used to wrap a code block that might throw an exception. In this case, the `Callable` wraps the creation of a `Bytes` object.

Note that I changed the import statement from `import org.cactoos.scalar.UncheckedScalar;` to `import org.cactoos.Scalar;` and `import org.cactoos.scalar.Unchecked;`. This is because the `UncheckedScalar` class is no longer available in the new library version, so we need to import the more generic `Scalar` interface instead. We also import the `Unchecked` class, which we will use to wrap the creation of the `Bytes` object.