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
            " pulled"
        )
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a `String.format` expression that evaluates to a `String` containing the image name. However, this causes a type mismatch since the `String.format` expression is not a `String` literal.

The proposed patch uses the `AllOf` class from the Hamcrest library, which allows combining multiple matchers into a single matcher. The first matcher is the same as before, but the second matcher is a new `StringContains` matcher that looks for the string " pulled" (with a space before it). This should fix the type mismatch error and allow the code to compile.