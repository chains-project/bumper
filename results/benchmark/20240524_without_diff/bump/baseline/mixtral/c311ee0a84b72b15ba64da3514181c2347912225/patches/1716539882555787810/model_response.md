Here is a possible patch for the failing method:
```java
    @ParameterizedTest
    @ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
    })
    void failsToResolveInvalid(final String string) {
        final HamcrestMatcher<String> matcher = new StringContains(string);
        final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
        );
        MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                Arrays.asList(
                    new StringContains("Unsupported reference"),
                    matcher
                )
            )
        );
    }
```
The changes I made are:

* I created a local variable `matcher` of type `HamcrestMatcher<String>` and initialized it to a new `StringContains` instance with the `string` argument.
* I replaced the second argument of the `new AllOf<>(...)` constructor with the `matcher` variable.

This patch should fix the error by using the new `StringContains` constructor that takes a single `String` argument. The `MatcherAssert.assertThat` method can take a `HamcrestMatcher` instance as its second argument, so there is no need to use the `MatcherAssert.assertThat` overload that takes a `Matcher` instance and a `String` argument.

Note that I did not remove the `@Override` decorator because the method is still overriding a method in the new version of the library. I also did not use any removed library methods (`--`) or added library methods (`++`) in the patch.

I hope this helps! Let me know if you have any questions or if you need further assistance.