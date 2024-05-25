Here is a possible patch for the code you provided:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, I replaced the `StringContains` class from the `org.hamcrest.core` package with the `containsString` method from the `CoreMatchers` class in the same package.

This should fix the error you are seeing, as the `containsString` method is a more appropriate matcher for this use case than the `StringContains` constructor.

Note that the `CoreMatchers` class is part of the Hamcrest library, so it should be available in your project if you have a dependency on Hamcrest. If you don't have a dependency on Hamcrest, you may need to add one in order for this patch to work.