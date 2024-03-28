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
                " pulling image " + image + " latest"
            )
        );
    }
```
The error message indicates that the constructor `StringContains` cannot be applied to the given types. This is because the `StringContains` class has been updated to require a `Pattern` argument in its constructor.

To fix this issue, we can create a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name. The second `StringContains` matcher checks for the presence of the string " pulling image " followed by the image name and the word "latest".

This patch should fix the error and allow the code to compile successfully.