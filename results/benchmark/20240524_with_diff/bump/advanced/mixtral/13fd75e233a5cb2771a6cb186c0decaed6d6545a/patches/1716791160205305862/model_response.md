Here's the patched version of the `imagePulled` method that should fix the error:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(
        java.lang.String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In the new library version, the `StringContains` constructor has been removed and replaced with the `containsString` method in the `Matchers` class. The new method takes a single `String` argument, which matches the expected argument type in the error message.