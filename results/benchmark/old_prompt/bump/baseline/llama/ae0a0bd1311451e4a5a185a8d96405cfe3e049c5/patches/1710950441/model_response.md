Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new AllOf(
            new StringContains(
                false,
                String.format("Status: Downloaded newer image for %s", image)
            ),
            new StringContains(
                false,
                " Pulled"
            )
        );
    }
```
The error message indicates that the `StringContains` constructor cannot be applied to the given types. This is because the `StringContains` class has been updated to expect a different type of argument.

To fix this issue, we can replace the `StringContains` class with the `AllOf` class, which is a newer version of the `StringContains` class. The `AllOf` class takes two arguments, the first is a collection of matchers, and the second is a description of the matcher.

In this case, we can create a new `AllOf` matcher that contains two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, and the second `StringContains` matcher checks for the presence of the string " Pulled".

This should fix the error and allow the code to compile without any issues.