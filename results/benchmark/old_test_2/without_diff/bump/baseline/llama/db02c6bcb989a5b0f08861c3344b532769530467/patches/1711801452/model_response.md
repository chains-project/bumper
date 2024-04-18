Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            true,
            " Pulled"
        )
    );
}
```
The `StringContains` constructor taking a single `String` argument has been removed in the latest version of the Hamcrest library. To fix the error, we can use the `AllOf` class from the same library, which allows us to combine multiple matchers into one. We create two `StringContains` matchers, one for the "Status: Downloaded newer image" string and another for the " Pulled" string, and combine them using `AllOf`.