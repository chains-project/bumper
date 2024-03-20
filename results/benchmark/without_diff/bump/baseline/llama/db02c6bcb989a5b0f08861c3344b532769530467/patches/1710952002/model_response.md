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
The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of "Status: Downloaded newer image for" followed by the image name, and the second `StringContains` matcher checks for the presence of " Pulled" at the end of the string.

The reason for this change is that the `StringContains` constructor with two arguments is not available in the version of the Hamcrest library being used, and the `AllOf` class is used to combine multiple matchers instead.

This patch should fix the error and allow the code to compile without any issues.