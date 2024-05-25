Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch uses the `containsString` method from the `CoreMatchers` class, which was added in Hamcrest version 1.3. This method is equivalent to the deprecated `StringContains` constructor that was used in the original code.