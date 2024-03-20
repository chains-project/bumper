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
The `StringContains` class has been replaced with `AllOf`, which is a class from the Hamcrest library that allows combining multiple matchers. The `StringContains` matcher is used twice, once with the negative flag set to `false` to match the "Status: Downloaded newer image for" string and another with the positive flag set to `true` to match the " Pulled" string.


This patch should fix the error and allow the code to compile.

It's important to note that this patch assumes that the error message is caused by the dependency issue you mentioned, and that the `StringContains` class is not available in the version of the Hamcrest library that you're using. If the issue persists, it may be necessary to try a different approach.