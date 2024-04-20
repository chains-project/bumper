Here is the proposed patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(org.hamcrest.core.StringContains.containsString(java.lang.String.format("Status: Downloaded newer image for %s", image))));
}
```
Explanation:
The error message indicates that the `StringContains` constructor now requires only one argument, a `String`, instead of two. The previous code passed `false` as the first argument, but this is no longer allowed.

To fix the error, we can use the new `containsString` method, which takes a `String` argument and returns a `Matcher`. This method was added in the new library version.

By using `containsString`, we can create a `Matcher` that checks if the given string contains the specified substring, which is what the original code was trying to do.