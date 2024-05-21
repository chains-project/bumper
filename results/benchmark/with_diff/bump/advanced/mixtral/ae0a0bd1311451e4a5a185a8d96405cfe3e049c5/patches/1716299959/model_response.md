Here is the proposed patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + image);
}
```
In the original code, the `StringContains` constructor was being called with two arguments, but the updated library version only accepts one argument. To fix the issue, I have removed the `false` argument from the constructor call, and concatenated the `image` argument with the rest of the string. This should allow the code to compile and run successfully with the updated library version.