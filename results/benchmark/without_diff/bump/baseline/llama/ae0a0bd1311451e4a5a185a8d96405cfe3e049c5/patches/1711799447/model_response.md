Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor taking a `String` and a `String` is not available in the version of the Hamcrest library being used. We can work around this by using the `AllOf` class from Hamcrest, which allows us to combine multiple matchers into one. We create a new `StringContains` matcher that checks for the presence of the image name at the end of the string, and combine it with the `StringEndsWith` matcher using `AllOf`. This should fix the error and make the code compile-time safe.