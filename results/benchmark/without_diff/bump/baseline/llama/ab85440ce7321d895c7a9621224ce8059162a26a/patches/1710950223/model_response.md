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
            " Pulled"
        )
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the contains pattern, and the second is a `boolean` that indicates whether the pattern should be matched case-insensitively. In this case, the second parameter is not provided, which causes the error.

The proposed patch uses the `AllOf` class from the Hamcrest library, which allows combining multiple matchers into a single matcher. The `AllOf` matcher takes an array of matchers, and matches if all of the matchers in the array match.

In this case, we create two `StringContains` matchers, one that looks for "Status: Downloaded newer image for" and another that looks for " Pulled". The first matcher has the `ignoreCase` parameter set to `false`, which means that the match will be case-sensitive. The second matcher has the `ignoreCase` parameter set to `true`, which means that the match will be case-insensitive.

By using `AllOf`, we ensure that both matchers must match for the method to pass, which should fix the error.