Here is the proposed patch for the failing client code:
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
                                new IsEqual<String>(string)
                        )
                )
        );
    }
```
The changes I made are:

* Replace the `StringContains` constructor with `IsEqual` for the second argument of `AllOf`.

Note: I am assuming that the `IsEqual` matcher is available in the new library version (`++`). If not, you may need to use a different matcher to check for equality.