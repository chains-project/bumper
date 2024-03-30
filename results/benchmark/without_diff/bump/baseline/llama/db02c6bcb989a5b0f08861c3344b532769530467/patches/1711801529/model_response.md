Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new AllOf(
            new StringContains(false, "Status: Downloaded newer image for "),
            new StringEndsWith(image)
        );
    }
```
The `StringContains` constructor takes two parameters, a `boolean` and a `String`, and cannot be applied to the given types `false` and `String.format("Status: Downloaded newer image for %s", image)`.


The proposed patch replaces the `StringContains` constructor with the `AllOf` class from the same package, which takes two `Matcher` objects and returns a `Matcher` that matches if both of the given matchers match.

The first argument to `AllOf` is a new `StringContains` matcher that searches for the literal string "Status: Downloaded newer image for ".
The second argument is a new `StringEndsWith` matcher that searches for the image name.

This should fix the error and allow the code to compile.