Here is a possible patch for the failing client code:
```java
    @ParameterizedTest
    @ValueSource(strings = {
            "",
            "a:b:c",
            ".123"
    })
    void failsToResolveInvalid(final String string) {
        final Throwable throwable = Assertions.assertThrows(
                IllegalStateException.class,
                () -> new ManifestRef.FromString(string).link().string()
        );
        MatcherAssert.assertThat(
                throwable.getMessage(),
                new AllOf<>(
                        Arrays.asList(
                                new StringContains("Unsupported reference"),
                                new StringContains(string)
                        )
                )
        );
    }
```
The only change I made is to remove the `true` argument from the first `StringContains` constructor. This is because the `StringContains` constructor that takes a `boolean` argument has been removed in the new library version. Instead, I used the `StringContains` constructor that takes a single `String` argument, which is the substring to search for. This constructor has been added in the new library version.

Note that I did not need to change the function signature or create any new variables. I also did not remove the `@Override` decorator because the method is still overriding a method in the new version. I also did not use any removed library methods, and I used the added `StringContains` constructor that takes a single `String` argument.

I hope this helps! Let me know if you have any questions or if you need further assistance.