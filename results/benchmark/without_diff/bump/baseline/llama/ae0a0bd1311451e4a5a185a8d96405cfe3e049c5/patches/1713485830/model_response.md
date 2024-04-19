Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "pulling image")
    );
}
```
This patch changes the `StringContains` constructor call to use the `AllOf` class from the Hamcrest library, which allows combining multiple matchers into a single matcher. The `StringContains` matcher is used twice, once to match the "Status: Downloaded newer image for" prefix and another to match the "pulling image" suffix.

The `AllOf` matcher takes two matchers as arguments and matches if both of the matchers match. This should fix the error and allow the code to compile.