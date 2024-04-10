Here's a proposed patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
We've replaced the `java.lang.String.format` method call with a lambda expression that formats the string using the `String.format` method. This avoids the issue of the removed `StringContains` constructor that took a boolean and a `String` argument. Instead, we're using the `StringContains` constructor that takes a `Supplier` of a `String`, which is the lambda expression in this case.