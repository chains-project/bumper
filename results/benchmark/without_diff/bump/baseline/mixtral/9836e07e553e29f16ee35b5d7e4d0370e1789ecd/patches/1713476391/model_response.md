Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we're using the `containsString` method from the `CoreMatchers` class, which is an added library method identified with `++`. This method can be used as a replacement for the deprecated `StringContains` constructor.