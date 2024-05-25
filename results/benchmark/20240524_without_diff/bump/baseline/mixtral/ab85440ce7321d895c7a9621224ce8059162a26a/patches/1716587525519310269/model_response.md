Here is a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with the `containsString` method from the `CoreMatchers` class, which is a part of the Hamcrest library. This should resolve the error message you provided.