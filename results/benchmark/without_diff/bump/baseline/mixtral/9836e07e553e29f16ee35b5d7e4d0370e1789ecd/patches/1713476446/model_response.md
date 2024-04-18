Here's a possible patch for the code:
```java
private static Matcher<String> imagePulled(final String image) {
    return new ContainsPattern(
        Pattern.compile(String.format("Status: Downloaded newer image for %s", image))
    );
}
```
In this patch, we replace the `StringContains` constructor with a new `ContainsPattern` constructor that takes a `Pattern` argument. The `Pattern` is compiled from the same string that was used in the original code. This should fix the error by using an added library method `Pattern.compile` instead of the removed `StringContains` constructor.