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
            " Pulled"
        )
    );
}
```
The `StringContains` class has been replaced with `AllOf`, which is a class from the Hamcrest library that allows combining multiple matchers. The `StringContains` matcher is used twice, first to check for the presence of "Status: Downloaded newer image" and then to check for the presence of " Pulled". The `AllOf` matcher returns a matcher that matches if all of its components match.

This should fix the error and allow the code to compile.