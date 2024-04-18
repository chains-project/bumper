Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` class has been replaced with `AllOf` and `StringEndsWith` to avoid the conflict with the `StringContains` constructor.
The `StringContains` constructor takes a boolean and a string, which causes the error.
By using `AllOf` and `StringEndsWith`, we can achieve the same result without calling the problematic constructor.
The `AllOf` class takes two matchers as arguments and matches if both matchers match.
The `StringEndsWith` class takes a string and matches if the input string ends with the given string.
In this case, we use `StringEndsWith` to check if the input string ends with the image name.
This change should fix the error and allow the code to compile successfully.