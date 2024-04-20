Here is the proposed patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
Explanation:
The error message indicates that the constructor for `StringContains` now requires only one argument (a `String`) instead of two (a `boolean` and a `String`).
Therefore, we can remove the first argument (`false`) from the constructor call.