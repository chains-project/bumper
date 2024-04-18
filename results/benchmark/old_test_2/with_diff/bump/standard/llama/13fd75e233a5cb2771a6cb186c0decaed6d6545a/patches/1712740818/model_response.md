Here's a possible patch to fix the error:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is to replace the `java.lang.String.format` method call with a lambda expression that uses the `String.format` method. This avoids the issue of the removed `StringContains` constructor that took a `boolean` and a `String` argument. Instead, we use the `StringContains` constructor that takes a `Supplier` of a `String`, which is the lambda expression that returns a `String` formatted with the given `image` argument.