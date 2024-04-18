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
This patch replaces the `StringContains` class with the `AllOf` class, which is a part of the Hamcrest library. The `AllOf` class takes an array of matchers as its constructor argument and matches when all of the matchers match.

In this case, we create an `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of the string "pull".

By combining these two matchers, we ensure that the method will only return true if both conditions are met, which should fix the error caused by the external dependency.