Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "pulling image")
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a formatted string that includes the `image` variable. However, this causes a type mismatch because the formatted string is not a `String` object, but a `String` literal.

The proposed patch uses the `AllOf` class from the Hamcrest library, which allows combining multiple matchers using the `and` method. The first matcher is a `StringContains` matcher that looks for the presence of the string "Status: Downloaded newer image for " followed by the `image` variable. The second matcher is another `StringContains` matcher that looks for the presence of the string "pulling image".

This patch should fix the error and allow the code to compile successfully.