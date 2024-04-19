Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "Image pulled successfully")
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a formatted string that includes the `image` variable. When the formatted string is created, the `image` variable is not yet known, so the compiler cannot infer the type of the variable.

The proposed patch uses the `AllOf` class from the Hamcrest library, which allows combining multiple matchers. The first matcher is the same as before, but the second matcher is a new `StringContains` matcher that searches for the string "Image pulled successfully". This should fix the error and allow the code to compile.