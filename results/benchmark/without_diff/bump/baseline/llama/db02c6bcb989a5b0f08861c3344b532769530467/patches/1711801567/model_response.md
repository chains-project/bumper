Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            true,
            "pullImage"
        )
    );
}
```
The `StringContains` constructor taking two parameters is not available in the version of the Hamcrest library being used, that's why we're using the `AllOf` matcher instead, which is available in the same version. The `AllOf` matcher takes an array of matchers as its argument and returns a matcher that matches if all of the elements of the array match. In this case, we're using two `StringContains` matchers, one that looks for "Status: Downloaded newer image for" followed by the image name, and another that looks for the string "pullImage".

This change should fix the error and allow the code to compile.