Here is a possible patch for the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch uses the `containsString` method from the `CoreMatchers` class, which is an added library method identified with `++`. This method is equivalent to the `StringContains` constructor, but it takes a `String` argument instead of a `boolean` and a `String`.