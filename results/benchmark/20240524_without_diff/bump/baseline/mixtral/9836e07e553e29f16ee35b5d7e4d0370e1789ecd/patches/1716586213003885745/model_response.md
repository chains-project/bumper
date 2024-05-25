Here is a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch uses the `containsString` method from the `CoreMatchers` class, which is an added library method in the Hamcrest library (marked as `++`). This method can be used as a replacement for the deprecated `StringContains` constructor.