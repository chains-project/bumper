Here's a possible patch for the given code:
```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, I replaced `StringContains` with `CoreMatchers.containsString` which is an added library method identified with `++`. This should resolve the error message that indicates a failure due to the `StringContains` constructor not being applicable to the given types.