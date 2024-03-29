Here is a fixed version of the method using a different Hamcrest matcher, `StringStartsWith`, instead of `StringContains`. This should resolve the error message you provided.
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringStartsWith(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```
This code uses the `StringStartsWith` matcher, which checks if a string starts with a certain prefix. This should work as a replacement for the `StringContains` matcher, which checks if a string contains a certain substring. The `StringStartsWith` matcher should be available in the same version of Hamcrest that provides the `StringContains` matcher.