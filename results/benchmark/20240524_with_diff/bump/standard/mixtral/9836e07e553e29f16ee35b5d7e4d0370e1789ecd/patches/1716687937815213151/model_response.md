Here is the proposed patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```
Explanation:
The error message indicates that the `StringContains` constructor now requires only one argument (a `String`) instead of two (a `boolean` and a `String`). Therefore, we need to replace the use of `StringContains` with a different matcher that accepts a `String` argument.
In this case, we can use the `containsString` method from the `Matchers` class, which takes a `String` argument and checks if the input string contains the specified substring.
This should fix the error and allow the code to compile and run successfully with the new library version.