Here is a fixed version of the method using a different Hamcrest matcher:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContainsIgnoringCase(
        String.format("downloaded newer image for %s", image)
    );
}
```
This version uses the `StringContainsIgnoringCase` matcher instead of `StringContains` to avoid the error message. The `StringContainsIgnoringCase` matcher is a case-insensitive version of `StringContains` and should work in this case.