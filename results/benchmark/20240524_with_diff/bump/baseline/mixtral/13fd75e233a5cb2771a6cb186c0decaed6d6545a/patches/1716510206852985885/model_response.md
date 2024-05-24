Here is a possible patch for the failing client code:
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
                        MatcherAssert.assertThat(e.getMessage(), matcher);
                        throw e;
                    }
                }
        );
    }
```
In this patch, I created a `Matcher` variable `matcher` that is used in the `assertThrows` method. This allows us to use the `MatcherAssert.assertThat` method with the correct number of arguments.

I also wrapped the code inside the `assertThrows` method in a try-catch block, so that we can catch the `IllegalStateException` and use the `MatcherAssert.assertThat` method on the exception message.

This patch should fix the error and allow the client code to compile and run with the new library version.