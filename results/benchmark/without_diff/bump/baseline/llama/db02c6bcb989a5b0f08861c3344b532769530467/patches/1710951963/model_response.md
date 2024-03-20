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
The `StringContains` class has been replaced with `AllOf`, which is a class from the Hamcrest library that allows combining multiple matchers. The `StringContains` matcher is used twice, with the first argument set to `false` to indicate that the matcher should not match the entire input, but rather a substring of it. The first `StringContains` matcher looks for the substring " Status: Downloaded newer image for " followed by the image name, while the second `StringContains` matcher looks for the substring " Pulled".

By using `AllOf`, we ensure that both substrings must be present in the input string for the matcher to match, which should fix the error.