Here's the fixed version of the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Sticky;

Scalar<String> scalar = new Sticky<>(() -> "some value");
String value = scalar.value();
```

The changes made are:

* Imported `org.cactoos.scalar.Sticky` instead of `org.cactoos.scalar.StickyScalar` since the latter has been removed in the new library version.
* Created a `Sticky` scalar using a lambda expression instead of directly using `StickyScalar`. This is because the constructor of `StickyScalar` has been removed in the new library version.
* Called the `value()` method on the `Sticky` scalar to get the value instead of directly accessing the `value` field, since the latter has been removed in the new library version.

Note that the `StickyScalar` class has been removed in the new library version, and the `Sticky` class should be used instead. The `Sticky` class provides a similar functionality to `StickyScalar`, but its `value()` method should be called to get the value instead of directly accessing the `value` field.