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
The only change I made was to remove the `true` and `false` arguments from the `StringContains` constructor. According to the error message, these arguments are not expected by the constructor in the new library version. Instead, the constructor now only takes a single `String` argument. I assumed that the second argument is intended to be the expected substring, so I removed the `false` argument and left the `string` argument. I also removed the `true` argument because it is not clear what it is supposed to represent. If it is important, you may need to add it back or replace it with a different value.