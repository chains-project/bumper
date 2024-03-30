Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "pulling image")
    );
}
```
The `StringContains` constructor takes two parameters, a `boolean` and a `String`, which makes the error go away.
The `AllOf` class is used to combine multiple matchers into one.
The `StringContains` matcher is used twice, once to match "Status: Downloaded newer image for " + image and once to match "pulling image".
This should fix the error and make the code compile.