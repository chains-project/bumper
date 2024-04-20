Here is the proposed patch for the failing client code:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.MatcherAssert.assertThat(image, new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image)));
}
```
Explanation:
The error message indicates that the constructor for `StringContains` now requires only one argument, instead of two. Therefore, we need to modify the code to pass only one argument to the constructor.
To achieve this, we can use the `MatcherAssert.assertThat` method, which takes two arguments: the input value and a matcher. This allows us to pass the formatted string directly to the `StringContains` constructor.
Note: This assumes that the `MatcherAssert` class is available in the new library version. If not, you may need to find an alternative solution.