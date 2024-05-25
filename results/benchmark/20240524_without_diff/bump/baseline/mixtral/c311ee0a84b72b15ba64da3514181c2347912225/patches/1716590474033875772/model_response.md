Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with the `containsString` method from the `CoreMatchers` class, which is an added library method identified with `++`. This should fix the error message you received.