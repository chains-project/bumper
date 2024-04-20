Here's the patched code that should fix the error:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

The error occurs because the constructor for `StringContains` no longer accepts a boolean parameter in the new library version. Instead, we can use the `containsString` method from `Matchers` to achieve the same functionality.