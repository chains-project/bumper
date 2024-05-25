Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor from the deprecated `org.hamcrest.core` package with the `containsString` method from the new `org.hamcrest.CoreMatchers` package, which provides the same functionality.