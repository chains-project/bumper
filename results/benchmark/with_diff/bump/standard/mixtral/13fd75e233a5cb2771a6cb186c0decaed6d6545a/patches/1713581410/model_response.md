Here's a possible patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringStartsWith(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
Explanation:
The error message indicates that the `StringContains` constructor now requires a single `String` argument, instead of the previous `boolean` and `String` arguments. Therefore, we can replace `StringContains` with `StringStartsWith` or `StringEndsWith`, both of which take a single `String` argument. I chose `StringStartsWith` for this example.