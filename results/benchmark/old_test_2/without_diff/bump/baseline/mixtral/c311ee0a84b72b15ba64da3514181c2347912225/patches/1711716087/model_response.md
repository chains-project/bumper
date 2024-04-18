Here is a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image),
        true
    );
}
```

In this version, I added a third argument `true` to the `StringContains` constructor. According to the Hamcrest library documentation, this argument indicates that the matcher should match substrings. This should resolve the error, as the constructor is now being called with the correct number and types of arguments.