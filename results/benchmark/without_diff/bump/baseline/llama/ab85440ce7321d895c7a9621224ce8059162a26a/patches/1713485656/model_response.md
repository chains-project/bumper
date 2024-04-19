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
            "pull"
        )
    );
}
```
The `StringContains` constructor takes two parameters, a `String` and a `boolean`. The error message indicates that the constructor cannot be applied to the given types. We can fix this by creating a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, and the second `StringContains` matcher checks for the presence of the string "pull".

By using `AllOf` matcher, we can combine multiple matchers and make the method more readable.

Please note that this is a simple example, you may want to add more logic to the matcher to make it more robust.