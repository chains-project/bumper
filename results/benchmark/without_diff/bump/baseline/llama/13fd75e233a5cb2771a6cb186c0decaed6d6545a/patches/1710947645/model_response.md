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
                "Pulling image"
            )
        );
    }
```
The error message indicates that the `StringContains` constructor cannot be applied to the given types. This is because the `StringContains` class has been updated to require a `Pattern` argument in its constructor.

To fix this issue, we can replace the `StringContains` class with the `AllOf` class, which is a more flexible alternative that can handle multiple matchers. We create two `StringContains` matchers, one for the "Status: Downloaded newer image for" string and another for the "Pulling image" string. We then pass these matchers to the `AllOf` constructor to create a new matcher that matches both conditions.

This patch should fix the error and allow the code to compile successfully.