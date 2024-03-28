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
                "Image pulled successfully"
            )
        );
    }
```
The error message indicates that the `StringContains` constructor cannot be applied to the given types, which means that the `org.hamcrest.core.StringContains` class has been updated and the old constructor is not compatible with the new version.

To fix this issue, we can replace the `StringContains` class with the `AllOf` class, which is a newer version of the `StringContains` class. The `AllOf` class takes two or more matchers as arguments and matches if all of the matchers match.

In this case, we create a new `AllOf` matcher that takes two matchers: the first one matches the string "Status: Downloaded newer image for" followed by the image name, and the second one matches the string "Image pulled successfully".

By using the `AllOf` matcher, we can keep the same logic as before but with a compatible version of the Hamcrest library.