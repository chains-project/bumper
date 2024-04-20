Here is the proposed patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(
        java.lang.String.format("Status: Downloaded newer image for %s", image)
    );
}
```
Explanation:
The error message indicates that the constructor for `StringContains` is expecting a single `String` argument, but is instead receiving a `boolean` and a `String`. This suggests that the API for `StringContains` has changed in the new library version.

In the new library version, the `StringContains` constructor has been removed (indicated by `--`), and a new method `containsString` has been added to `CoreMatchers` (indicated by `++`). The `containsString` method takes a single `String` argument and checks if the target string contains the specified substring.

In the patched code, we use `CoreMatchers.containsString` instead of `StringContains` to create a matcher that checks if the target string contains the specified substring. This should fix the error and allow the client code to work with the new library version.