Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "pulling image")
    );
}
```
The `StringContains` constructor takes two parameters, a `boolean` and a `String`. The error message indicates that the constructor cannot be applied to the given types. It's likely that the `StringContains` class has been updated to require a different signature, which is not backward compatible.

The proposed patch uses the `AllOf` class from the same package to achieve the same result. The `AllOf` class takes an array of `Matcher` objects and matches if all of the elements match. In this case, we create two `StringContains` objects with the same logic as before, but this time we wrap them in an `AllOf` matcher. This should fix the error and allow the code to compile.