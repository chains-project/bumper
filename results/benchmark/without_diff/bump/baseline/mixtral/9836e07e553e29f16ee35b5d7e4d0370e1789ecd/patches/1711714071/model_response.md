Here is a fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(false,
                              String.format("Status: Downloaded newer image for %s", image),
                              "Status:",
                              "Downloaded",
                              "image"
    );
}
```

In this version, I've added three additional arguments to the `StringContains` constructor: "Status:", "Downloaded", and "image". These arguments are used to specify a substring that the matcher should look for within the target string. By including these substrings, we can ensure that the matcher only matches the desired line in the output, even if the format of the line changes in the future.

I noticed that the original code used `String.format` to create the target string, which is a good practice. However, the `StringContains` constructor only accepts a plain string, not a formatted string. To work around this, I've included the fixed string "Status: Downloaded newer image for" as the second argument to the constructor, and then added the additional substrings as separate arguments.

This should allow the code to compile and run without errors, even if the format of the output from the external dependency changes in the future.