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
                "downloaded"
            )
        );
    }
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a format string that contains a `%s` placeholder for the `image` parameter. However, this causes a type mismatch error because `image` is not a `String`.

The proposed patch uses the `AllOf` class from the Hamcrest library, which allows combining multiple matchers using logical AND. The first matcher is a `StringContains` matcher that looks for the presence of the string "Status: Downloaded newer image for" followed by the `image` parameter. The second matcher is another `StringContains` matcher that looks for the presence of the string "downloaded".

This patch should fix the error and allow the code to compile successfully.