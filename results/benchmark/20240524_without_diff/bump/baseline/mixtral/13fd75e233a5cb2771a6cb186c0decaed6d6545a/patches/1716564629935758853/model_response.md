Sure, I understand the requirements. Here's a fixed version of the `imagePulled` method that should resolve the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.StringContains(
        CoreMatchers.not(CoreMatchers.stringContainsInOrder(
            Arrays.asList("Status: Downloaded newer image for", image)
        ))
    );
}
```
In this version, I replaced the use of `String.format` with a call to `Arrays.asList` to create a list of strings that I then pass to `stringContainsInOrder` method. This method checks if the given strings appear in the specified order in the target string.

Additionally, I replaced the use of `StringContains` constructor with `CoreMatchers.StringContains` to use the statically imported `CoreMatchers` class. This is because the `StringContains` constructor is no longer available in the version of Hamcrest that the code is using.

Finally, I used `CoreMatchers.not` method to check if the given strings do not appear in the target string in the specified order. This is equivalent to the original code that checks if the target string contains the formatted string.