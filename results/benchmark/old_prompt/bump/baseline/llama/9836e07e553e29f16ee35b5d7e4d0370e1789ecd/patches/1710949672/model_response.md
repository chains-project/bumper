Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(true, "Image pulled successfully")
    );
}
```
The error is caused by the fact that the `StringContains` constructor takes two parameters of the same type, which is not allowed. To fix this, we can use the `AllOf` class from the same package, which allows us to combine multiple matchers into one. We create two `StringContains` matchers, one for the "Status: Downloaded newer image" string and one for the "Image pulled successfully" string, and combine them using the `AllOf` matcher. This should fix the error and allow the code to compile and run correctly.