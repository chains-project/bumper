Here is a possible patch for the given code:
```java
private static Matcher<String> imagePulled(final String image) {
    StringContains stringContains = StringContains.containsString(image);
    return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image),
            stringContains
    );
}
```
Explanation:

* The `StringContains` constructor in Hamcrest 2.2 (which is the version with the added `StringContains(boolean, Matcher<String>, String)` constructor) requires a `Matcher<String>` object as its second argument.
* In the original code, the second argument of the `StringContains` constructor is a `String` literal, which causes the compilation error.
* To fix the error, we need to create a `Matcher<String>` object that matches the expected substring, and pass it as the second argument to the `StringContains` constructor.
* In this case, we can use the `StringContains.containsString(String)` method to create a `Matcher<String>` that matches the given `image` string.
* Note that we need to remove the `Override` decorator since the `imagePulled` method is not overriding any method in the new version.