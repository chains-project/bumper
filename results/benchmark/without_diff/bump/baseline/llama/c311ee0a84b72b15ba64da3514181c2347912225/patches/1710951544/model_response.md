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
The `StringContains` constructor takes two parameters: the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a formatted string that includes the image name, which causes the error.

The proposed patch uses the `AllOf` class from the Hamcrest library, which allows combining multiple matchers. The first matcher is the same as before, but the second matcher is new and checks if the string contains the word " Pulled". This should fix the error and allow the code to compile.