Here is a possible patch for the failing code:
```java
    @ParameterizedTest
    @ValueSource(strings = {
            "",
            "a:b:c",
            ".123"
    })
    void failsToResolveInvalid(final String string) {
        final Matcher<String> matcher = new AllOf<>(
                Arrays.asList(
                        new StringContains("Unsupported reference"),
                        new StringContains(string)
                )
        );
        final Throwable throwable = Assertions.assertThrows(
                IllegalStateException.class,
                () -> {
                    try {
                        new ManifestRef.FromString(string).link().string();
                    } catch (IllegalStateException e) {
                        Assertions.assertThat(e.getMessage(), matcher);
                        throw e;
                    }
                }
        );
    }
```
The changes made in this patch are:

* The `StringContains` constructor that takes a boolean argument has been removed in the new library version. To fix the error, we can create a separate `Matcher<String>` object for the `StringContains` matcher, and use it in the `assertThrows` method.
* The `MatcherAssert.assertThat` method has been removed in the new library version. To fix the error, we can use the `Assertions.assertThat` method instead.
* To make the code more readable, we can extract the creation of the `Matcher<String>` object into a separate variable.
* We can wrap the body of the lambda expression in a try-catch block, so that we can check the message of the `IllegalStateException` before rethrowing it. This way, we can use the `Matcher<String>` object to check the message of the exception.

Note that this patch may not be the only possible solution, and other valid patches may exist.