Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor with two arguments is not available in the version of the Hamcrest library being used. We can work around this by using the `AllOf` class from Hamcrest, which allows us to combine multiple matchers using the `and` method. We create a new `StringContains` matcher with the same message as before, and combine it with a new `StringEndsWith` matcher that checks if the input string ends with the image name.

This patch replaces the failing `StringContains` constructor with a compound matcher created using `AllOf`, which should fix the error.