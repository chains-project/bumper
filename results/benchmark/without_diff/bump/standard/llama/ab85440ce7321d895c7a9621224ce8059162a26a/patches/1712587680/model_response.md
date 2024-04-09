Here's a possible patch to fix the issue:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is in the second argument of the `StringContains` constructor. Instead of passing a `java.lang.String` directly, we're now passing a function that returns a `java.lang.String`. This function takes no arguments and returns the formatted string using the `image` parameter.

This modification should fix the issue because the constructor `StringContains(boolean, Function<? super T, ? extends R>) ` takes a function as its second argument, which is what we're providing now.