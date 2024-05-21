Here is the proposed patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(
        java.lang.String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, we replaced the use of the deprecated `StringContains` constructor with the new `containsString` method from the `Matchers` class. This should resolve the error message indicating that the constructor cannot be applied to the given types.