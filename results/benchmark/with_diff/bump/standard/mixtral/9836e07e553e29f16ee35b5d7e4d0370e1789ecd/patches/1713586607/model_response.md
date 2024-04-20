Here is the fixed version of the code that should work with the new library version:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains.StringStartsWith(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
Explanation:
The error message indicates that the constructor for `StringContains` now requires only one argument (a `String`) instead of two (a `boolean` and a `String`). Therefore, we need to use a different constructor that matches the new signature.
The `StringStartsWith` constructor takes a single `String` argument and checks if the input string starts with the given substring, which should work for this case.