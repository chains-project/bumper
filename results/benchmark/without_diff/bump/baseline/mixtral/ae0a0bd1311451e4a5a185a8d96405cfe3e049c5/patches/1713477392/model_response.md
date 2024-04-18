Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replaced the `StringContains` constructor with the `containsString` method from the `CoreMatchers` class, which is an added library method identified with `++`. This should fix the error caused by the constructor not being applicable to the given types.