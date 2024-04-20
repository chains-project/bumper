Here's the fixed method using a different approach to create the `Matcher`:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matcherators.hasItem(
        org.hamcrest.core.StringStartingWith.startingWith(
            java.lang.String.format("Status: Downloaded newer image for %s", image)
        )
    );
}
```

This solution uses `Matcherators.hasItem` and `StringStartingWith` to achieve a similar result, avoiding the need for `StringContains.containsString`.