Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            true,
            " pulling image " + image + " latest"
        )
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the full match, and the second is a `String` that represents the partial match. In the original code, the second parameter is not a `String` but a `String.format()` call. This causes the error because `StringContains` expects a `String` as its second parameter.

The proposed patch uses the `AllOf` class from the Hamcrest library, which allows combining multiple matchers into one. The first matcher is the same as before, but the second matcher is new and checks for the presence of the string " pulling image " + image + " latest". This should fix the error and allow the code to compile.