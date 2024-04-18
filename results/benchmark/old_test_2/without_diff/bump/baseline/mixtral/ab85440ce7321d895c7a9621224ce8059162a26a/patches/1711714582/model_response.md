Here is a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image),
        true
    );
}
```

The only change I made was to add a third argument to the `StringContains` constructor, which is a boolean indicating whether or not to treat the contained string as a regular expression. By setting this to `true`, we ensure that the constructor can accept a string with special characters like the colon (`:`) and the percentage sign (`%`). This should resolve the error you were seeing.