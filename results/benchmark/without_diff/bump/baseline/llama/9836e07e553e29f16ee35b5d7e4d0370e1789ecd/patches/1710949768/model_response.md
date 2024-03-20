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
The `StringContains` class has been replaced with `AllOf`, which is a class from the Hamcrest library that allows combining multiple matchers. The `StringContains` matcher is used twice, once to check for the presence of "Status: Downloaded newer image for" followed by the image name, and another to check for the presence of "pullImage". The `AllOf` matcher then combines these two matchers using the `AllOf` constructor.

This should fix the error and allow the code to compile successfully.