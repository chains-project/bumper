Here's a fixed version of the method using a different Hamcrest matcher:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContainsIgnoringCase(
        String.format("status: downloaded newer image for %s", image)
    );
}
```

This version uses `StringContainsIgnoringCase` instead of `StringContains` to avoid the error. Note that I also changed the case of the "Status" string to "status" to match the expected output.