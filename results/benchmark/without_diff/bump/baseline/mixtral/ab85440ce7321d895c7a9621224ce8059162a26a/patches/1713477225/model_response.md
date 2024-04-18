Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new AbstractMatcher<String>("Status: Downloaded newer image for " + image) {
        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("Status: Downloaded newer image for %s", image));
        }
    };
}
```

In this patch, we're using a different constructor for the `Matcher` class, specifically the one that takes an abstract base matcher as an argument. We then implement the `matchesSafely` method to check if the given string contains the expected message.

Note that we're using the `String.contains` method instead of the `org.hamcrest.core.StringContains` class, as the latter seems to be causing the issue. The `String.contains` method should be available in any Java version that supports Lambdas.