Here is the proposed patch for the failing method:
```java
    @ParameterizedTest
    @ValueSource(strings = {
            "",
            "a:b:c",
            ".123"
    })
    void failsToResolveInvalid(final String string) {
        final StringContains stringContains = new StringContains(string);
        final Throwable throwable = Assertions.assertThrows(
                IllegalStateException.class,
                () -> new ManifestRef.FromString(string).link().string()
        );
        MatcherAssert.assertThat(
                throwable.getMessage(),
                new AllOf<>(
                        Arrays.asList(
                                new StringContains(true, "Unsupported reference"),
                                stringContains
                        )
                )
        );
    }
```
In this patch, I created a separate variable for the `StringContains` matcher and passed the string value directly to its constructor. This way, the `StringContains` constructor will receive only one argument, which matches its definition in the new library version.